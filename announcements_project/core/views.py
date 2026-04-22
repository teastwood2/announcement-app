from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from .models import User
from .forms import UserRegForm
# Create your views here.
def register(request):
    if request.method == "GET":
        form = UserRegForm()
        return render(request, 'core/register.html', {'form' : form})
    elif request.method == "POST":
        form = UserRegForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.role == 'teacher':
                teacher_group = Group.objects.get(name = 'Teacher Permissions')
                user.groups.add(teacher_group)
            elif user.role == 'student':
                student_group = Group.objects.get(name = 'Student Permissions')
                user.groups.add(student_group)
            user.save()
            login(request, user)
            return redirect('announcement_list')
        else:
            return render(request, 'core/register.html', {'form' : form})

def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username = username, password = password)
            if user:
                next_url = request.GET.get('next')
                login(request, user)
                return redirect(next_url if next_url else 'announcement_list')
    form = AuthenticationForm()
    return render(request, 'core/login.html', {'form' : form })