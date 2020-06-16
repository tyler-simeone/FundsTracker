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
        expense = MonthlyExpense.objects.get(pk=expense_id)

        template = 'expenses/form.html'
        context = {
            'expense': expense
        }

        return render(request, template, context)