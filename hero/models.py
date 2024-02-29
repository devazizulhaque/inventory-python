from django.db import models

# Create your models here.
# class Hero(models.Model):
#     name = models.CharField(max_length=120)
#     alias = models.CharField(max_length=120)
    
#     def __str__(self):
#         return self.name

class Destination:
    id: int
    name: str
    img: str
    desc: str
    price: int
    offer: bool