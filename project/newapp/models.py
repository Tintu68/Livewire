from django.db import models

# Create your models here.
class Hotel(models.Model):
    food_name=models.CharField(max_length=100)
    img=models.ImageField(upload_to="pics")
    food_desc=models.TextField()
    food_price=models.IntegerField()
    
    """def __str__(self):
        return self.food_name"""
