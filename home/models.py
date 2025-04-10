from django.db import models

# Create your models here.

#Table parents
class Categories(models.Model):
  name=models.CharField(max_length=50)
  icon=models.CharField(max_length=50)
    
  def __str__(self):
    return self.name


#Table child
class Product(models.Model):
  name=models.CharField(max_length=50) #string
  color=models.CharField(max_length=50) #string
  price=models.DecimalField(max_digits=10,decimal_places=5) #decimal
  qty=models.IntegerField() #int
  tax=models.FloatField() #float
  total=models.DecimalField(max_digits=10,decimal_places=5) #decimal
  date=models.DateTimeField(auto_now_add=True)
  net=models.DecimalField(max_digits=10,decimal_places=5,default=0.00) #decimal
  notes=models.CharField(max_length=50,default='') #string
  image=models.ImageField(upload_to='images/')
  categories=models.ForeignKey(Categories,on_delete=models.CASCADE) 


    
  def __str__(self):
   return self.name