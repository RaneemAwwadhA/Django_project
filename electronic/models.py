from django.db import models

# Create your models here.

class Product(models.Model):
  name=models.CharField(max_length=50)
  color=models.CharField(max_length=50)
  price=models.DecimalField(max_digits=10, decimal_places=5 , default=0.00)
  qty=models.IntegerField()
  tax=models.FloatField()
  total=models.DecimalField(max_digits=10, decimal_places=5 , default=0.00)
  date=models.DateTimeField(auto_now_add=True)
  net=models.DecimalField(max_digits=10, decimal_places=5 , default=0.00)
  notes=models.CharField(max_length=50, default='')


class categories(models.Model):
  name=models.CharField(max_length=50)
  description=models.CharField(max_length=50)
  notes=models.CharField(max_length=50)

  
def __str_(self):
  return self.name
