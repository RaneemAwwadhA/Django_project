"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from home import views as _home
from electronic import views as _electronic
from beauty import views as _beauty
from django.conf import settings
from django.conf.urls.static import static
from product import views as _product




  

#For each page, we create a function and a path to connect the Back-End with the Front-End
urlpatterns = [    
    path("",_home.showland,name='homee'),
    path('aboutus/',_home.about,name='aboutt'),
    path('contactus/',_home.contact,name='contacct'),
    path('prod/',_product.index, name='index'),
    path('create/',_product.create, name='create'),
    path('prod/delete/<int:id>/',_product.delete,name='delete'),
    path('edit/<int:id>/',_product.edit,name='edit'),
    path('update/',_product.update,name='update'),
    path('admin/', admin.site.urls),

    
   # Display products for the category
    path('products/<int:id>/', _product.list_product, name='list_product'),
    
    # Display products details 
    path('details/<int:id>/',_product.product_details, name='product_detail'),

    # Add product to cart
    path('addtocart/',_product.add_to_cart, name='add_to_cart'),
    
   path('checkout/',_product.checkout, name='checkout'),


   path('account/', include('accounts.urls')),
   
    #path('details/',_product.product_details, name='details'),
    #path('electronic/',_electronic.list_electronic,name='listelectronic'),
    #path('beauty/',_beauty.list_beauty,name='listbeauty'),
    #path('showphone/<str:phone>/',_electronic.showphone,name='showphone'),
    #path('categories/',_electronic.categories,name='categories'),
    #path('Products/',_electronic.products),
    
    
    
    
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
