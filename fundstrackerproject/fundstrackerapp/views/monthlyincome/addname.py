from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def add_name(request, user_id):

    if request.method == 'POST':

        form_data = request.POST
        
        full_name = form_data['name']
        first_name = full_name.split()[0]
        last_name = full_name.split()[1]

        user = User.objects.get(pk=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return redirect(reverse('fundstrackerapp:account'))