from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Product

# Create your views here.

def list_electronic(request):
  electronic=[
        {'id':1,'name':'Laptop Dell 14 inspiron', 'price':3700,'description':'Laptop Dell 14 inspiron core i7 SSD RAM 16 GB','image':'https://img.freepik.com/free-vector/laptop-realistic_78370-511.jpg?t=st=1741896494~exp=1741900094~hmac=1b6560556aba5b7350c761743f6a80cb85c293fe473ded85d7fe505691288dea&w=826'},
        {'id':2,'name':'Laptop Lenovo', 'price':3800,'description':'Laptop Lenovo core i7 SSD RAM 16 GB','image':'https://img.freepik.com/free-vector/laptop-realistic_78370-511.jpg?t=st=1741896494~exp=1741900094~hmac=1b6560556aba5b7350c761743f6a80cb85c293fe473ded85d7fe505691288dea&w=826'},
        {'id':3,'name':'iPhone 16 pro', 'price':4800,'description':'iPhone 16 pro SSD RAM 16 GB','image':'https://img.freepik.com/premium-vector/phone-mockup-realistic-mockup-purple-color-vector-illustration_797816-206.jpg?w=740'},
        {'id':4,'name':'Samsung S 24 ', 'price':3500,'description':'Samsung S 24 SSD RAM 16 GB','image':'https://img.freepik.com/free-vector/realistic-style-new-smartphone-model_23-2148380821.jpg?t=st=1741897540~exp=1741901140~hmac=8c4a8993c4b4abfe4c2732fa264df5538b078b6330ef7cad3a67855574673bdc&w=826'},

    ]
  
  contex={
    'electronic':electronic
  }
  #print(request)
  template=loader.get_template('list_electronic.html')
  return HttpResponse(template.render(contex))

def showphone(request,phone):
  template=loader.get_template('phone.html')
  value={
    'ph': phone

  }
  #print(phone)
  return HttpResponse(template.render(value))

@csrf_exempt
def categories(requset):
  template=loader.get_template('categories.html')
  x=requset.POST.get('title')
  y=requset.POST.get('address')
  value={
    'title': x,
    'address':y
  }

  return HttpResponse(template.render(value))

def products(request):
  template=loader.get_template('product.html')
  prd= Product.objects.all()
  value={
    'prod': prd
  }


  return HttpResponse(template.render(value))






