from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from fundstrackerapp.models import MonthlyIncome, MonthlyExpense

@login_required
def net_income(request):
    
    all_incomes = MonthlyIncome.objects.filter(user=request.auth.user.id)