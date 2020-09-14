from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def register(request):

    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            
            return redirect(reverse('fundstrackerapp:home'))

    else:
        f = UserCreationForm()

    template = 'registration/register.html'
    context = {'form': f}
 
    return render(request, template, context)