from django.shortcuts import render, redirect, reverse
from fundstrackerapp.models import MonthlyIncome, MonthlyExpense
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def income_list(request):

    # passes all incomes and expenses for the logged-in user
    # into the list template (account page)

    if request.method == 'GET':
        all_incomes = MonthlyIncome.objects.filter(user=request.user.id)
        all_expenses = MonthlyExpense.objects.filter(user=request.user.id)
        user = User.objects.get(pk=request.user.id)

        template = 'incomesources/list.html'
        context = {
            'user': user,
            'all_incomes': all_incomes,
            'all_expenses': all_expenses
        }

        return render(request, template, context)
      
    elif request.method == 'POST':

        # creates a new expense if hidden input in the form 
        # contains "expense" value

        form_data = request.POST

        if ("expense" in form_data):
            total = form_data['total']
            split_total = total.split(',')
            new_total = ''.join(split_total)

            new_expense = MonthlyExpense.objects.create(
                name = form_data['name'],
                total = new_total,
                user_id = request.user.id
            )
        
        # creates a new income for user

        else:
            total = form_data['total']
            split_total = total.split(',')
            new_total = ''.join(split_total)

            new_income = MonthlyIncome.objects.create(
                name = form_data['name'],
                total = new_total,
                user_id = request.user.id
            )        

        return redirect(reverse('fundstrackerapp:account'))