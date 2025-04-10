from django.db import models

# Parent Table - Categories
class Category(models.Model):
    name = models.CharField(max_length=50)
  
    def __str__(self):
     return self.name


# Child Table - Products
class Product(models.Model):
    name = models.CharField(max_length=50)  
    color = models.CharField(max_length=50)  
    price = models.DecimalField(max_digits=10, decimal_places=5)  
    qty = models.IntegerField()  
    tax = models.DecimalField(max_digits=10, decimal_places=5)  
    total = models.DecimalField(max_digits=10, decimal_places=5)  
    date = models.DateTimeField(auto_now_add=True)  
    net = models.DecimalField(max_digits=10, decimal_places=5, default=0.00)  
    notes = models.TextField(max_length=50, default='')  
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)  
    
    # Image field added here
    
    image = models.ImageField(upload_to='images/', default='images/default.jpg')

    def __str__(self):
        return self.name

  