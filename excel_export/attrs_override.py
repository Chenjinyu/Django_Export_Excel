"""
fireracker URL Configuration

author: jinyu2010.chen@gmail.com
date: 08/02/2016
"""

from datetime import datetime


# smartbuy form CSS 
INPUT_CSS = 'form-control input-lg'
INPUT_NUM_CSS = 'form-control input-lg input_num_width'

SELECT_CSS = 'form-control input-lg dropdown-toggle'

HEADER_ITEM_TXT = 'Item Name'
SMART_BUY_TXT = 'Item One'
CHASSIS_TXT = 'Item Two'
PROCESSOR_TXT = 'Item Three'
HEATSINK_TXT = 'Item Four'
FANS_TXT = 'Item Five'
MEMORY_TXT = 'Item Six'
STORAGE_CONTR_TXT = 'Item Seven'
POWER_SUPPLY_TXT = 'Item Eight'
RAIL_KIT_TXT = 'Item Nine'
HEATSINK2_TXT = 'Item Ten'


QTY_TXT = 'Qty'
PART_NUM_TXT = 'Part Number'
NONFIO_SKU = 'SKU'
DESC_TXT = 'Description'
COST_TXT = 'Cost'
EX_COST_TXT = 'Ex.Cost'
MSRP_TXT = 'MSRP'
EX_MSRP_TXT = 'ex.MSRP'


MODIFY_DATETIME = 'Update Datetime'



def get_current_timestamp():
    return datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]


