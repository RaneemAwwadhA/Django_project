from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from django.template import loader
from .models import Product , Categories
# Create your views here.

def showland(request):
  if 'cart_count' not in request.session:
    request.session['cart_count']=0

  template=loader.get_template('landpage.html')
  
  #print(request.session['x'])
  categories=Categories.objects.all()
  data={
    'categories': categories,
    'cart_count' : request.session['cart_count']
  }
  return HttpResponse(template.render(data , request))




def about(request):
  if 'cart_count' not in request.session:
    request.session['cart_count']=0

  template=loader.get_template('aboutus.html')
  data = {
    'cart_count' : request.session['cart_count']
    }
  return HttpResponse(template.render(data , request))



def contact(request):
  if 'cart_count' not in request.session:
    request.session['cart_count']=0

  template=loader.get_template('contactus.html')
  data = {
    'cart_count' : request.session['cart_count']
    }
  return HttpResponse(template.render(data , request))




#def list_product(request,id):
    #template=loader.get_template('list_products.html')
    #products=Product.objects.filter(categories_id=id)
    #data={
    #'product': products
    #}

    #return HttpResponse(template.render(data))



#def product_details(request):
    #count=0
    #count=count+1
    #template=loader.get_template('productdetails.html')

    #return HttpResponse(template.render())





