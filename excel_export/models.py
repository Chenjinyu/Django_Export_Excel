from django.db import models

# Create your models here.
class ExcelExport(models.Model):
    
    # ---- this is demo scope ---- 
    demo_qty = models.PositiveIntegerField(blank = True, null=True)
    demo_part_number = models.CharField(max_length = 20, blank = True, null=True) 
    demo_nonfio_sku = models.CharField(max_length = 200, blank = True, null=True)
    demo_desc = models.CharField(max_length = 500, blank = True, null=True)
    demo_cost = models.DecimalField(max_digits=15, decimal_places=2, blank = True, null=True)
    demo_ex_cost = models.DecimalField(max_digits=15, decimal_places=2, blank = True, null=True)
    demo_msrp = models.DecimalField(max_digits=15, decimal_places=2, blank = True, null=True)
    demo_ex_msrp = models.DecimalField(max_digits=15, decimal_places=2, blank = True, null=True)


    
    def __str__(self):
        return str(self.pk) + ' Part Number: ' + self.demo_part_number 

