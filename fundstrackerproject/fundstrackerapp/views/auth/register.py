from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError

def register(request):
    
    if request.method == 'POST':
        f = UserCreationForm(request.POST)

        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')
 
        else:
            f = UserCreationForm()

    template = 'registration/register.html'    
 
    return render(request, template, {'form': f})