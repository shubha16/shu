from django.shortcuts import render
from .models import *
from .forms import *
from django.http import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    obj = Student1.objects.all()
    return render(request, 'index.html',{'obj':obj})


def student(request):
    obj1 = Student1.objects.all().order_by('-dat')
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/studentform/')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form':form, 'std':obj1})


def register(request):
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        if form1.is_valid():
            username = form1.cleaned_data['username']
            firstname = form1.cleaned_data['first_name']
            lastname = form1.cleaned_data['last_name']
            email = form1.cleaned_data['email']
            password = form1.cleaned_data['password']
            User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password = password)
            messages.success(request,'Registration is Successfull...')
            return HttpResponseRedirect('/registrationform')


    else:
        form1 = UserForm()
    return render(request,'registration_form.html', {'frm':form1})

def login(request):
    if request.method == "POST":
        username = request.POST['user']
        password = request.POST['pas']
        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return render(request, 'welcome.html')
            else:
                messages.error(request, 'Username and Password did not match')

        except auth.ObjectNotExist:
            print("Invalid User")

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')