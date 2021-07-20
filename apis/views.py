from django.shortcuts import render

# Create your views here.

def login(request):
    data = {
        'msg': 'Login Page....',
        'name'  :'Ashik'
    }
    print("logges in user", request.user)
    return render(request, 'webpages/login.html', data)