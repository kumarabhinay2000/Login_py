from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm

def main_page(request):
    return render(request,"main.html")

def register_view(request):
    if request.user.is_authenticated:
        return redirect('welcome')
    
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            logout(request,user)
            messages.success(request,"Registration successfully. Welcome!")
            return redirect('welcome')
        else:
            messages.error(request,'Please correct the erros below.')

    else:
        form=RegisterForm()
    return render(request,"register.html",{'form':form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('welcome')
    
    if request.method=='POST':
        form=LoginForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request, f"Welcome back,{user.username}! ")
                return redirect('welcome')
            else:
                messages.error(request,'Invalid username or password')

        else:
            messages.error(request,"Invalid username or password.")
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

@login_required
def welcome_view(request):
    return render(request,"welcome.html")

def logout_view(request):
    logout(request)
    messages.info(request,'you have been logged out')
    return redirect('main')