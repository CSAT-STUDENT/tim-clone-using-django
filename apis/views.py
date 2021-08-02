from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib import auth
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_page(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
    

        user = authenticate(request=request, username = username , password = password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else:
            return redirect('login_page')
        
    return render(request, 'webpages/login.html')



def logout_page(request):
    logout(request)
    return redirect('login_page')
    

