from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from fundstrackerapp.models import MonthlyIncome, MonthlyExpense

@login_required
def net_income_list(request):

    if request.method == 'GET':
        
        all_incomes = MonthlyIncome.objects.filter(user=request.auth.user.id)
        all_expenses = MonthlyExpense.objects.filter(user=request.auth.user.id)

        total_income = 0
        total_expense = 0

        for income in all_incomes:
            total_income += income.total

        for expense in all_expenses:
            total_expense += expense.total

        net_income = total_income - total_expense

        template = 'netincome/list.html'
        context = {
            'net_income': net_income
        }

        return render(request, template, context)