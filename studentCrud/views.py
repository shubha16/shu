from django.shortcuts import render, redirect, get_object_or_404
from studentCrud.forms import StudentForm
from django.http import *
from .models import StudentModel
from django.contrib import messages
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


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

        form = StudentForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('studentCrud:success')
        return render(request, template_name, {'form':form})
    else:
        return redirect('studentCrud:login')



def success(request, template_name='student_manage.html'):
    if request.user.is_authenticated:
        context = {}
        context['user'] = request.user
        std_data = StudentModel.objects.all()
        data = {}
        data['object_list'] = std_data
        return render(request, template_name, data, context)
    else:
        return redirect('studentCrud:login')


def student_edit(request, pk, template_name='student_add.html'):
    if request.user.is_authenticated:
        book = get_object_or_404(StudentModel, pk=pk)
        form = StudentForm(request.POST or None, instance=book)
        if form.is_valid():
            form.save()
            return redirect('studentCrud:success')
        return render(request, template_name, {'form':form})
    else:
        return redirect('studentCrud:login')


def student_delete(request, pk, template_name='student_add.html'):
    if request.user.is_authenticated:
        book = get_object_or_404(StudentModel, pk=pk)
        book.delete()
        messages.success(request,"Data Deleted Successfully...")
        return redirect('studentCrud:success')
    else:
        return redirect('studentCrud:login')


def logout(request):
    auth.logout(request)
    return redirect('studentCrud:login')





