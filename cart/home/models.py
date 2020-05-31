from django.db import models

# Create your models here.


class Item(models.Model):
    item_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    descrp = models.TextField(max_length=300, default="")
    price = models.FloatField(default=0)
    top_selling = models.BooleanField(default=False)
