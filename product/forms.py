from django.forms import ModelForm
from .models import Product , Category
from django import forms

class  productForm(ModelForm):
     class Meta:
       model=Product
       fields=('name', 'color', 'price' , 'qty', 'tax' , 'total', 'net' , 'notes' ,'categories' ,'image')
       
       
       
       widgets={
           'name':forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
           'color':forms.TextInput(attrs={'class': 'form-control'}),
           'price':forms.TextInput(attrs={'class': 'form-control'}),
           'qty':forms.TextInput(attrs={'class': 'form-control'}),
           'tax':forms.TextInput(attrs={'class': 'form-control'}),
           'total':forms.TextInput(attrs={'class': 'form-control'}),  
           'net': forms.NumberInput(attrs={'class': 'form-control'}),
           'notes': forms.TextInput(attrs={'class': 'form-control'}),
           'categories': forms.Select(attrs={'class': 'form-select'}),
           'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),

    }
  


