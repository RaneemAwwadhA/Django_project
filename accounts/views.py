from django.shortcuts import render , redirect
from django.contrib.auth import login , logout
from .form import RegisterForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def login_view(request):
  if request.method=='POST':
    form=AuthenticationForm(request , data=request.POST)    # Check if the data is correct
    if form.is_valid():                                     # Check if the data is valid and not empty 
      user=form.get_user()
      login(request,user)
      return redirect('checkout')
  else:   
    form=AuthenticationForm()
  return render(request , 'accounts/login.html' , {'form':form})
      
def sign_up(request):
    if request.method=='POST':
      form=RegisterForm(request.POST)   
      if form.is_valid(): 
        user=form.save()
        login(request,user)
        return redirect('homee')
    else:
      form=RegisterForm()
    return render(request , 'accounts/signup.html' , {'form':form})



def logout_view(request):
   logout(request)
   return redirect('login')
    
  

  
  
