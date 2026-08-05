from django.db import models

# Create your models here.
class Product(models.Model):
    pname = models.CharField(max_length=30)
    pprice = models.IntegerField()
    image = models.ImageField(upload_to='images/',null=True)