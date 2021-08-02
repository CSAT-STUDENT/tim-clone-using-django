from django.db import models

# Create your models here.

#we are not going to use this model, I just wanted to test out things.... NO need to worry about that
class Simple(models.Model):
    test = models.CharField(max_length=100)
    newfld = models.CharField(max_length=100)



#just a type of Drink, Hot, cold, Smoothie
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
# class Items(models.Model):
#     item_type = models.CharField(max_length=255, choices=DRINK_TYPE, default='COLD')

