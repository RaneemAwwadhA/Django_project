from django.shortcuts import render,redirect
from django.http import HttpResponse ,JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .forms import productForm
from .models import Product , Category
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db import connection
from django.contrib.auth.decorators import login_required



# Create your views here.

@csrf_exempt
def index(request):
    if 'cart_count' not in request.session:
     request.session['cart_count']=0

    val = request.GET.get('val')
    if not val:
        product = Product.objects.all()   # All products
    else:
      product = Product.objects.filter(name=val)   # For search filter
    categories = Category.objects.all()  
    template = loader.get_template('index.html')
    form = productForm()
    context = {
        'form': form,
        'prd': product,
        'categories': categories , 
        'cart_count' : request.session['cart_count']
    }
    
    return render(request, 'index.html', context)


#To view products by category
def list_product(request, id):
    if 'cart_count' not in request.session:
     request.session['cart_count']=0

    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(categories_id=id)
    return render(request, 'list.html', {
        'product': products,
        'category': category , 
        'cart_count' : request.session['cart_count']
    })


#To view product_details 
def product_details(request, id):
    if 'cart_count' not in request.session:
        request.session['cart_count']=0

    product = get_object_or_404(Product, id=id)
    
    cart_count = request.session.get('cart_count', 0)  

    context = {
        'product': product,
        'cart_count': cart_count
    }

    return render(request, 'product_details.html', context)


#Add product to cart
def add_to_cart(request):
   request.session['cart_count']=request.session.get('cart_count',0)+1
   request.session.modified=True
   return JsonResponse({'cart_count': request.session['cart_count']})



#chech_Out page
@csrf_exempt
@login_required
def checkout(request):
    if 'cart_count' not in request.session:
        request.session['cart_count'] = 0

    cart = request.session.get('cart', {})

# Make sure each item in the cart is a dict containing price and quantity
    total = 0
    for item in cart.values():
        if isinstance(item, dict) and 'price' in item and 'quantity' in item:
            total += item['price'] * item['quantity']

    shipping = 5 # Fixed shipping price, for example
    grand_total = total + shipping

    context = {
        'cart': cart,
        'cart_count': request.session.get('cart_count', 0),
        'total': total,
        'shipping': shipping,
        'grand_total': grand_total,
    }
    print("User:", request.user)



    return render(request, 'checkout.html', context)



#To create a new product

@csrf_exempt
def create(request):
    name = request.POST.get('name')
    color = request.POST.get('color')
    price = request.POST.get('price')  
    qty = request.POST.get('qty')
    tax = request.POST.get('tax')
    total = request.POST.get('total')
    net = request.POST.get('net')
    notes = request.POST.get('notes')
    category_id = request.POST.get('category')  
    image = request.FILES.get('image')  

    
    # Make sure category_id exists and is a valid number
    try:
        categories = get_object_or_404(Category, id=(category_id))
    except (ValueError, Category.DoesNotExist):
        messages.error(request, "Invalid category selected.")
        return redirect('/prod/')

    
    prod = Product(
        name=name,
        color=color,
        price=price,
        qty=qty,
        tax=tax,
        total=total,
        net=net,
        notes=notes,
        categories=categories,
        image=image  
    )
    prod.save()
    reset_product_ids()
    
    messages.success(request, "Product added successfully !")
    return redirect('/prod/')




#To delete a product
def delete(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()

    
    # Reorder IDs after deletion
    reset_product_ids()
    
    return redirect('/prod/')
   
    
  

#Reorder ID after deleting product
def reset_product_ids():
    with connection.cursor() as cursor:
        cursor.execute("""
            SET @count = 0;
            UPDATE product_product SET id = @count := (@count + 1);
        """)

    
        
#To edit a product
def edit(request,id):
     if 'cart_count' not in request.session:
      request.session['cart_count']=0

     template=loader.get_template('edit.html')
     prd=Product.objects.get(id=id)
     categories = Category.objects.all() 
     items={
         'produc':prd,
         'categories': categories, 
         'cart_count' : request.session['cart_count']
     }
     #return HttpResponse(template.render(items))
     return render(request, 'edit.html', items)



#To update a product
@csrf_exempt
def update(request):
    if request.method == 'POST':
     id=request.POST.get('id')
     name=request.POST.get('name')
     color=request.POST.get('color')
     price=request.POST.get('price')
     qty=request.POST.get('qty')
     tax=request.POST.get('tax')
     total=request.POST.get('total')
     net=request.POST.get('net')
     notes=request.POST.get('notes')
     category_id = request.POST.get('category') 
     image = request.FILES.get('image')  
     


    categories = Category.objects.get(id=category_id)
    
    
  
    prd = Product.objects.get(id=id)
    prd.name=name 
    prd.color=color
    prd.price=price 
    prd.qty=qty 
    prd.tax=tax
    prd.total=total
    prd.net=net
    prd.notes=notes
    prd.categories=categories

    if image:                # Update image only if a new one is uploaded
            prd.image = image

    prd.save()
    # Send message after product modification
    messages.info(request, "The product has been updated successfully !")
    return redirect('/prod/') 



