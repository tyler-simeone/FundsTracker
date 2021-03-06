from django.shortcuts import render, redirect, reverse
from fundstrackerapp.models import MonthlyExpense
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def expense_form(request):

    # rendering the expense form template

    if request.method == 'GET':

        template = 'expenses/form.html'
        context = {}

        return render(request, template, context)
      
@login_required
def expense_edit_form(request, expense_id):

    # rendering the expense form template with an expense
    # object passed in so form has values to edit
        
    expense = MonthlyExpense.objects.get(pk=expense_id)

    if expense.user_id == request.user.id:

        if request.method == 'GET':

            template = 'expenses/form.html'
            context = {
                'expense': expense
            }

            return render(request, template, context)

    else:

        return redirect(reverse('fundstrackerapp:home'))
