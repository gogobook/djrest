from django.db import models
from django.contrib.postgres.fields import JSONField
class Manufacturer(models.Model): # 製造廠
    name = models.CharField(max_length=20) 
  
class TrafficTools(models.Models):
    CAR_MOTORCYCLE_BICYCLE=(
        ('M','Motorcycle'),
        ('C','Car'),
        ('T','Truck'),
        ('B','Bicycle'),
    )
    traffictool = models.CharField(max_length=1, choices=CAR_MOTORCYCLE_BICYCLE)
    manufacturer = models.ForeignKey(Manufacturer)
    anymodel = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    anyimage = ImageField([upload_to=None, height_field=None, width_field=None, max_length=100, **options])

class FuelRecord(models.Models):
    adding_oil_time = models.DateTimeField([auto_now=True, auto_now_add=False, **options])
    mileage = models.DecimalField(max_digits=None, max_digits=6, decimal_places=1)
    fuels = models.DecimalField(max_digits=None, max_digits=2, decimal_places=2)
    add_oil_image = ImageField([upload_to=None, height_field=None, width_field=None, max_length=100, **options])
    traffic_tool = models.ForeignKey(TrafficTools)

class Maintenance(models.Models):
    maintenance_time = models.DateTimeField([auto_now=True, auto_now_add=False, **options])
    traffic_tool = models.ForeignKey(TrafficTools)
    garage = models.ForeignKey(Garage)

class MaintenanceItem(models.Models):
    maintenance = models.Foreignkey(Maintenance)
    item = JSONField() # 用json來存維修的細項，但這樣的話下面的PartNo class 的意義就不大了。
    

class PartNo(models.Models): # 零件的名稱及價格
    CATEGORY = ( # 零件屬於那一個類別
        ('L','lubricating oil'),
        ('E','Engine'),
        ('C','Consumables'),
        ('E','配件'),
        ('A','冷氣'),
        ('T','傳動'),
        ('O','其他'),

    )
    part_name = models.CharField(max_length=20)
    part_category = models.CharField(max_length=1,choices=CATEGORY)
    part_no = models.CharField(max_length=30, blank = True)
    origin = models.BooleanField(default=False) # 是否為原廠零件
    price = models.DecimalField(max_digits=None, max_digits=6, decimal_places=1) #單價




