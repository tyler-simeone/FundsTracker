from django.shortcuts import render, redirect, reverse
from fundstrackerapp.models import MonthlyIncome
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def income_list(request):

    if request.method == 'GET':
        all_incomes = MonthlyIncome.objects.filter(user=request.user.id)
        user = User.objects.get(pk=request.user.id)

        template = 'incomesources/list.html'
        context = {
            'user': user,
            'all_incomes': all_incomes
        }

        return render(request, template, context)
      
    elif request.method == 'POST':
        form_data = request.POST
        
        new_income = MonthlyIncome.objects.create(
            name = form_data['name'],
            total = form_data['total'],
            user_id = request.user.id
        )        

        return redirect(reverse('fundstrackerapp:account'))