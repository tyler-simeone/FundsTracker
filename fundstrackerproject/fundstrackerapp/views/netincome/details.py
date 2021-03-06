from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from fundstrackerapp.models import MonthlyIncome, MonthlyExpense

@login_required
def net_income_details(request):

    # getting all incomes and expenses for the logged-in user,
    # finding the difference between the two totals to get net
    # income, passing in the total income, expenses and the net
    # bottom-line so user can see the calculations

    if request.method == 'GET':

        all_incomes = MonthlyIncome.objects.filter(user=request.user.id)
        all_expenses = MonthlyExpense.objects.filter(user=request.user.id)

        total_income = 0
        total_expense = 0

        for income in all_incomes:
            total_income += income.total

        for expense in all_expenses:
            total_expense += expense.total

        net_income = total_income - total_expense

        template = 'netincome/details.html'
        context = {
            'total_income': total_income,
            'total_expense': total_expense,
            'net_income': net_income
        }

        return render(request, template, context)