from django.shortcuts import render, redirect, reverse
from fundstrackerapp.models import MonthlyIncome
from django.contrib.auth.decorators import login_required


@login_required
def income_list(request):

    if request.method == 'GET':
        all_incomes = MonthlyIncome.objects.all(user=request.user.id)

        template = 'monthlyincome/list.html'
        context = {
            'all_books': all_incomes
        }

        return render(request, template, context)
      
    elif request.method == 'POST':
        form_data = request.POST
        
        new_income = MonthlyIncome.objects.create(
            name = form_data['name'],
            total = form_data['total'],
            user_id = form_data['user']
        )        

        # return redirect(reverse('fundstrackerapp:income_list'))