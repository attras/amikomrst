from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.views import View 
from django.contrib import messages
from admin_setori.models import *
import re

def check_is_email(email):

    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return bool(re.match(email_regex,email))


class LogViews(View):
    def get(self, request):
        return render(request, 'admin/login.html')
    
class User(View):
    def get(self, request):
        user = Account.objects.all()
        data = {
            'user': user
        }
        return render(request, 'admin/login/user.html', data)
    
    def __str__(self):
        return f"{self.username} {self.email}"
    
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('admin_setori:dashboard')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('admin_setori:login')