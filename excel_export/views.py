from django.http import JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, render_to_response  
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from .models import ExcelExport
from .forms import ExcelExportForm
from .excel_utils import WriteToExcel

from . import attrs_override as attr


def demo_home(request):
    try:
        demo_list = ExcelExport.objects.all().defer('id', 'demo_part_number').order_by('id')
        
    except ExcelExport.DoesNotExist:
        raise Http404("The Prodcut does not exist")
        
    return render(request, 'part_num_list.html', {'demo_list': demo_list})   
        
def demo_details(request):
    
    if request.method == 'POST':
        demo_list = []
        searched_sb_list = []
        part_num_str = request.POST.get('id_part_num', '')
        part_num_list = [num.strip() for num in part_num_str.split(',') if num]
        part_num_list = list(set(part_num_list))
        for num in part_num_list:
            try:
                demo_row = ExcelExport.objects.get(demo_part_number = num)
                searched_sb_list.append(demo_row.pk)
            except ExcelExport.DoesNotExist:
                messages.add_message(request, messages.ERROR, 'the Part Number: [%s] does not exist in database.'  % num)
            else:    
                demo_list.append(demo_row)
                
        if 'searched_sb_list' in request.session:
            del request.session['searched_sb_list']
        request.session['searched_sb_list'] = searched_sb_list
            
    else:
        messages.add_message(request, messages.WARNING, 'Your Part Number was lost, please re-fill it.')
        return HttpResponseRedirect(reverse('home'))
                
    return render(request, 'smart_buy_detail.html', {'demo_list': demo_list, 'export_all': True})    

def demo_detail_id(request, pk):
    try:
       
        demo_list = []
        demo_row = ExcelExport.objects.get(pk = pk)
        demo_list.append(demo_row)
        
    except ExcelExport.DoesNotExist:
        raise Http404("The Prodcut does not exist")
        
    return render(request, 'smart_buy_detail.html', {'demo_list': demo_list})    


def demo_edit_id(request, pk):
    
    demo_obj = get_object_or_404(ExcelExport, pk = pk)
    form = ExcelExportForm(request.POST or None, instance = demo_obj)
    
    if request.method == 'POST': 
        if form.is_valid():
            post = form.save(commit = False)
            
            post.save()
            
            messages.add_message(request, messages.SUCCESS, 'Update successfully.')
            return HttpResponseRedirect(reverse(demo_detail_id, kwargs = {'pk' : pk}))
            
    else:
#         return render(request, 'demo_edit_form.html', {'form': form})
        return render(request, 'demo_add_form.html', {'form': form, 'type': 'edit'})              
    

def demo_add(request):
    if request.method == 'POST':
        form = ExcelExportForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit = False)
            tmp = False
            try:
                # search part number in database
                tmp = ExcelExport.objects.get(demo_part_number = post.demo_part_number)
            except ExcelExport.DoesNotExist:
                pass
            if tmp:
                messages.add_message(request, messages.ERROR, 'the Part Number of [%s] has existed in database, Please check it again or contact with adminitrator.'  % post.demo_part_number)
                return render(request, 'demo_add_form.html', {'form': form, 'type': 'add'})      
            
            post.save()
            messages.add_message(request, messages.SUCCESS, 'A new form have been added successfully.')
            return HttpResponseRedirect(reverse('demo_detail_id', args=[post.pk]))
        
    else:
        form = ExcelExportForm()
    return render(request, 'demo_add_form.html', {'form': form, 'type': 'add'})      
                

def export_sig_to_excel(request, pk):

    if request.method == 'GET':
        demo_list = []
        try:
            demo_row = ExcelExport.objects.get(pk = pk)
        except ExcelExport.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'the Part Number: [%s] does not exist in database.'  % str(pk))
        else:    
            demo_list.append(demo_row)
              
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=demo_%s.xlsx' % demo_row.demo_part_number 
        xlsx_data = WriteToExcel(demo_list)
        response.write(xlsx_data)
        return response
                
                
def export_all_to_excel(request):
    if request.method == 'GET':
        if 'store_modi_id' in request.session:
             messages.add_message(request, messages.ERROR, 'The Part Number have been lost, please re-search them.')
             return HttpResponseRedirect(reverse('home'))
            
        demo_list = []
        pn_id_list =  request.session['searched_sb_list']
        for id in pn_id_list:
            try:
                demo_row = ExcelExport.objects.get(pk = id)
            except ExcelExport.DoesNotExist:
                messages.add_message(request, messages.ERROR, 'the Part Number does not exist in database.' )
            else:    
                demo_list.append(demo_row)
              
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=demo_list_%s.xlsx' % attr.get_current_timestamp() 
        xlsx_data = WriteToExcel(demo_list)
        response.write(xlsx_data)
        return response
                
                

