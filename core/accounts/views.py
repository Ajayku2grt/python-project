from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse # to return jsonresponse

#for 
from table import Table
from table.columns import Column


from django.contrib.auth.models import User # use to import use models
from django.contrib.auth.hashers import make_password #use to encrpt password
from django.contrib.auth import authenticate, login #use for login
# Create your views here.


def home(request):
    return render(request,'account_detail.html')

def signup(request):
    return render(request,'register.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = make_password(request.POST['pwd'])
        User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username, password=password)
        return redirect('login')  # Redirect to the login page after successful registration
    return render(request, 'register.html')


def auth(request):
    return render(request,'login.html')


def authenticate(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['email'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
