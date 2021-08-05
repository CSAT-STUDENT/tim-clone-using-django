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

DONUT_TYPE=(
    ('SPECIALITY', 'SPECIALITY'),
    ('RING FILLED', 'RING FILLED'),
    ('CLASSIC', 'CLASSIC')
)

QUANTITY =(
    ('1KG','1KG'),
    ('5KG','2KG'),
    ('10KG','10KG')
)

SANDWITHCHES = (
    ('WHITE','WHITE'),
    ('WHOLE WHEAT','WHOLE WHEAT'),
    ('MULTIGRAIN','MULTIGRAIN'),
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


class Donut(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(choices=DONUT_TYPE,max_length=255)
    price = models.FloatField()
    desc = models.TextField()
    calories = models.FloatField()


    def __str__(self):
        return self.name


class Retail(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.CharField(choices=QUANTITY,max_length=255)
    price = models.FloatField()
    desc = models.TextField()

    def __str__(self):
        return self.name
    


    