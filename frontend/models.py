from django.db import models

# Create your models here.
DRINK_TYPE = (
    ('COLD','COLD'),
   ('HOT','HOT'),
   ('SMOOTHIE','SMOOTHIE'),
   ('PROMO','PROMO'),
   ('LUNCH', 'LUNCH'),
   ('BREAKFAST', 'BREAKFAST'),
   ('SPECIAL','SPECIAL'),
   ('DONUT','DONUT')
)
class Item(models.Model):
    item_type = models.CharField(max_length=200, choices=DRINK_TYPE )

    def __str__(self):
        return self.item_type
    

class Beverages(models.Model):
    name = models.CharField(max_length=256)
    price_s = models.IntegerField()
    price_m = models.IntegerField()
    price_l = models.IntegerField()
    desc = models.IntegerField()
    type = models.CharField(max_length=200, choices=DRINK_TYPE )


    def __str__(self):
        return self.name

