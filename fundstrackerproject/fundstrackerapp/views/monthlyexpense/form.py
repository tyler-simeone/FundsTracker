from django.shortcuts import render, redirect, reverse
from fundstrackerapp.models import MonthlyExpense
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def expense_form(request):

    if request.method == 'GET':

        template = 'expenses/form.html'
        context = {}

        return render(request, template, context)
      
@login_required
def expense_edit_form(request, expense_id):

    if request.method == 'GET':
        income_source = MonthlyExpense.objects.get(pk=income_id)

        template = 'incomesources/form.html'
        context = {
            'income_source': income_source
        }

        return render(request, template, context)
