from django.shortcuts import render, redirect, get_object_or_404
from studentCrud.forms import StudentForm
from django.http import *
from .forms import *
from .models import StudentModel
from django.contrib import messages
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.models import User

def registerform(request):
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        if form1.is_valid():
            username = form1.cleaned_data['username']
            email = form1.cleaned_data['email']
            firstname = form1.cleaned_data['first_name']
            lastname = form1.cleaned_data['last_name']
            password = form1.cleaned_data['password']
            roles = form1.cleaned_data['role']
            User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
            messages.success(request,'Registration is Successfull...')
            return redirect('studentCrud:login')

    else:
        form1 = UserForm()
    return render(request,'registration_form.html', {'frm':form1})


def login(request, template_name='login.html'):
    if request.method == "POST":
        username = request.POST['user']
        password = request.POST['pas']
        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('studentCrud:success')
            else:
                messages.error(request, 'Username and Password did not match')

        except auth.ObjectNotExist:
            print("Invalid User")

    return render(request, template_name)


def add_student(request, template_name='student_add.html'):
    if request.user.is_authenticated:
        if request.role == 'Principal':
            context = {}
            if request.method == 'POST':
                user_form = UserForm(request.POST or None)
                context['user_form'] = user_form
        #        form = User.objects.values('first_name', 'last_name')
                if user_form.is_valid():
                    user_form.save()
                    return redirect('studentCrud:success')
                return render(request, template_name, {'user_form': user_form})
            else:
                user_form = UserForm()
                context['user_form'] = user_form
                return render(request, template_name, {'user_form': user_form})
        else:
            return redirect('studentCrud:success')

    else:
        return redirect('studentCrud:login')


def success(request, template_name='student_manage.html'):
    if request.user.is_authenticated:
        print(request.role)
        context = {}
        context['users'] = User.objects.all()
        return render(request, template_name, context)
    else:
        return redirect('studentCrud:login')


def student_edit(request, pk, template_name='student_add.html'):
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=pk)
        if request.method == 'POST':
            user_form = UserForm(request.POST or None, instance=user)
            if user_form.is_valid():
                user_form.save()
                return redirect('studentCrud:success')
            else:
                return render(request, template_name, {'user_form': user_form})
        else:
            user_form = UserForm(instance=user)
            return render(request, template_name, {'user_form': user_form})
    else:
        return redirect('studentCrud:login')


def student_delete(request, pk):
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=pk)
        user.delete()
        messages.success(request,"Data Deleted Successfully...")
        return redirect('studentCrud:success')
    else:
        return redirect('studentCrud:login')


def logout(request):
    auth.logout(request)
    return redirect('studentCrud:login')





