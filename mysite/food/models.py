from django.db import models

# Create your models here.
class Item(models.Model):
   
    item_name = models.CharField(max_length=50)
    item_disc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqFOSj56PX7k71VGMxiVcwc8uXc3mLk78vyg&s")
    def __str__(self):
        return self.item_name

    