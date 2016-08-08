from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import ExcelExport

from .attrs_override import *

 
class ExcelExportForm(forms.ModelForm):
     
    class Meta:
        model = SmartBuy
        
        widgets = {
            # ----- demo ------
            'demo_qty': forms.NumberInput(attrs = {'class': INPUT_CSS}),
            'demo_part_number': forms.TextInput(attrs = {'class': INPUT_CSS}),
            'demo_nonfio_sku': forms.TextInput(attrs = {'class': INPUT_CSS}),
            'demo_desc': forms.TextInput(attrs = {'class': SELECT_CSS}),
            'demo_cost': forms.TextInput(attrs = {'class': INPUT_CSS}),
            'demo_ex_cost': forms.TextInput(attrs = {'class': INPUT_CSS}),
            'demo_msrp': forms.TextInput(attrs = {'class': INPUT_CSS}),
            'demo_ex_msrp': forms.TextInput(attrs = {'class': INPUT_CSS}),
        }
        
        labels = {
            # ----- demo ------
            'demo_qty': _(SMART_BUY_TXT + ' ' + QTY_TXT),
            'demo_part_number': _(SMART_BUY_TXT + ' ' + PART_NUM_TXT),
            'demo_nonfio_sku': _(SMART_BUY_TXT + ' ' + NONFIO_SKU),
            'demo_desc': _(SMART_BUY_TXT + ' ' + DESC_TXT),
            'demo_cost': _(SMART_BUY_TXT + ' ' + COST_TXT),
            'demo_ex_cost': _(SMART_BUY_TXT + ' ' + EX_COST_TXT),
            'demo_msrp': _(SMART_BUY_TXT + ' ' + MSRP_TXT),
            'demo_ex_msrp': _(SMART_BUY_TXT + ' ' + EX_MSRP_TXT),
            

        }
        
        exclude = ['create_datetime', 'modify_datetime']