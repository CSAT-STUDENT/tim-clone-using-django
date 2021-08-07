from django.shortcuts import render
from .models import Employee
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login_page')
def listemp(request):
    emps = Employee.objects.all()
    data ={
        'emps':emps
    }
    return render(request, 'webpages/listemp.html', data)

@login_required(login_url='login_page')
def addemp(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        dob = request.POST['dob']
        position = request.POST['position']
        pincode = request.POST['pincode']
        age = request.POST['age']
        obj   = Employee(name=name, email_id=email, age=age, pincode=pincode, dob=dob, position=position)
        obj.save()

    
    return render(request, 'webpages/addemp.html')
    

def listempspecific(request,name):
    emp = Employee.objects.filter(name=name)
    print("Employee Fpound :", emp)
    data = {
        'emps': emp
    }
    return render(request,'webpages/listempspecific.html', data)