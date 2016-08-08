try:
    from BytesIO import BytesIO
except ImportError:
    from io import BytesIO
    
import xlsxwriter
from django.utils.translation import ugettext as _

from .models import ExcelExport
from .attrs_override import *


def WriteToExcel(excel_export_list):
    
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet_s = workbook.add_worksheet('Excel_Export_Sheet_name')
    worksheet_b = workbook.add_worksheet('Part Number List')
    
    # excel styles
    title = workbook.add_format({
        'bold': True,
        'font_size': 14,
        'align': 'center',
        'valign': 'vcenter'
    })
    header = workbook.add_format({
        'bg_color': '#F7F7F7',
        'color': 'black',
        'align': 'center',
        'valign': 'top',
        'border': 1
    })
    
    bold_header = workbook.add_format({
        'bold': True,
        'bg_color': '#F7F7F7',
        'color': 'black',
        'align': 'center',
        'valign': 'top',
        'border': 1
    })
    
    cell = workbook.add_format({
        'align': 'left',
        'valign': 'top',
        'text_wrap': True,
        'border': 1
    })
    
    bold_cell = workbook.add_format({
        'bold': True,
        'align': 'left',
        'valign': 'top',
        'text_wrap': True,
        'border': 1
    })
    
    cell_center = workbook.add_format({
        'align': 'center',
        'valign': 'top',
        'border': 1
    })
    
    # write header, this is row 1 in excel
    worksheet_s.write(0, 0, _(HEADER_ITEM_TXT), header)
    worksheet_s.write(0, 1, _(QTY_TXT), header)
    worksheet_s.write(0, 2, _(PART_NUM_TXT), header)
    worksheet_s.write(0, 3, _(NONFIO_SKU), header)
    worksheet_s.write(0, 4, _(DESC_TXT), header)
    worksheet_s.write(0, 5, _(COST_TXT), header)
    worksheet_s.write(0, 6, _(EX_COST_TXT), header)
    worksheet_s.write(0, 7, _(MSRP_TXT), bold_header)
    worksheet_s.write(0, 8, _(EX_MSRP_TXT), header)
    
    # column widths 
    item_name_col_width = 20
    qty_col_width = 10
    part_num_col_width = 20
    nonfio_sku_col_width = 30
    desc_col_width = 80
    cost_col_width = 10
    ex_cost_col_width= 10
    msrp_col_width = 10
    ex_msrp_col_width = 10
    
    # add data into the table
    data_row = 1
    second_sheet_data_row = 0
    for sb in smartbuy_list:
        
        if data_row is not 1:
            for index in range(9):
                worksheet_s.write(data_row, index, '', cell)
            data_row += 1
        
        # this is for smartbuy row, row 2 in excel
        worksheet_s.write_string(data_row, 0, _(SMART_BUY_TXT), cell)
        if not sb.smartbuy_qty:  
            sb.smartbuy_qty = ''
        worksheet_s.write(data_row, 1, sb.smartbuy_qty, cell)
        if not sb.smartbuy_part_number:
            sb.smartbuy_part_number = '' 
        worksheet_s.write_string(data_row, 2, sb.smartbuy_part_number, bold_cell)
        worksheet_b.write_string(second_sheet_data_row, 0, sb.smartbuy_part_number, cell)
        second_sheet_data_row += 1
        if not sb.smartbuy_nonfio_sku:
             sb.smartbuy_nonfio_sku = ''
        worksheet_s.write_string(data_row, 3, sb.smartbuy_nonfio_sku, cell)
        if not sb.smartbuy_desc:
            sb.smartbuy_desc = '' 
        worksheet_s.write_string(data_row, 4, sb.smartbuy_desc, cell)
        if not sb.smartbuy_cost: 
            sb.smartbuy_cost = ''
        worksheet_s.write(data_row, 5, sb.smartbuy_cost, cell)
        if not sb.smartbuy_ex_cost: 
            sb.smartbuy_ex_cost = ''
        worksheet_s.write(data_row, 6, sb.smartbuy_ex_cost, cell)
        if not sb.smartbuy_msrp: 
            sb.smartbuy_msrp = ''
        worksheet_s.write(data_row, 7, sb.smartbuy_msrp, bold_cell)
        if not sb.smartbuy_ex_msrp:
             sb.smartbuy_ex_msrp = ''
        worksheet_s.write(data_row, 8, sb.smartbuy_ex_msrp, cell)

        
        # change column widths
        if sb.smartbuy_qty:  worksheet_s.set_column('A:A', item_name_col_width)
        if sb.smartbuy_qty:  worksheet_s.set_column('B:B', qty_col_width)
        if sb.smartbuy_qty:  worksheet_s.set_column('C:C', part_num_col_width)
        if sb.smartbuy_qty:  worksheet_s.set_column('D:D', nonfio_sku_col_width)
        if sb.smartbuy_qty:  worksheet_s.set_column('E:E', desc_col_width)
        if sb.smartbuy_qty:  worksheet_s.set_column('F:F', cost_col_width)
        if sb.smartbuy_qty:  worksheet_s.set_column('G:G', ex_cost_col_width)
        if sb.smartbuy_qty:  worksheet_s.set_column('H:H', msrp_col_width)
        if sb.smartbuy_qty:  worksheet_s.set_column('I:I', ex_msrp_col_width)
        
        #  for each smart buy data end <<<------
        
        # change column widths
        worksheet_s.set_column('A:A', item_name_col_width)
        worksheet_s.set_column('B:B', qty_col_width)
        worksheet_s.set_column('C:C', part_num_col_width)
        worksheet_b.set_column('A:A', part_num_col_width)
        worksheet_s.set_column('D:D', nonfio_sku_col_width)
        worksheet_s.set_column('E:E', desc_col_width)
        worksheet_s.set_column('F:F', cost_col_width)
        worksheet_s.set_column('G:G', ex_cost_col_width)
        worksheet_s.set_column('H:H', msrp_col_width)
        worksheet_s.set_column('I:I', ex_msrp_col_width)
       
    # close workbook
    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data



