from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from fundstrackerapp.models import MonthlyIncome, MonthlyExpense, FinancialGoal

@login_required
def net_income_list(request):

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

        # Now need to get completed vs current goals for the user

        # ONE MONTH PROGRESS %
        one_month_incomplete_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=1, is_completed=0)
        one_month_incomplete_goals_length = len(one_month_incomplete_goals)

        one_month_completed_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=1, is_completed=1)
        one_month_completed_goals_length = len(one_month_completed_goals)

        one_month_progress_percentage_deci = one_month_completed_goals_length / one_month_incomplete_goals_length
        one_month_progress_percentage = int(one_month_progress_percentage_deci * 100)

        # THREE MONTH PROGRESS %
        three_month_incomplete_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=3, is_completed=0)
        three_month_incomplete_goals_length = len(three_month_incomplete_goals)

        three_month_completed_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=3, is_completed=1)
        three_month_completed_goals_length = len(three_month_completed_goals)

        three_month_progress_percentage_deci = three_month_completed_goals_length / three_month_incomplete_goals_length
        three_month_progress_percentage = int(three_month_progress_percentage_deci * 100)
        
        # SIX MONTH PROGRESS %
        six_month_incomplete_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=6, is_completed=0)
        six_month_incomplete_goals_length = len(six_month_incomplete_goals)

        six_month_completed_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=6, is_completed=1)
        six_month_completed_goals_length = len(six_month_completed_goals)

        six_month_progress_percentage_deci = six_month_completed_goals_length / six_month_incomplete_goals_length
        six_month_progress_percentage = int(six_month_progress_percentage_deci * 100)
        
        # TWELVE MONTH PROGRESS %
        twelve_month_incomplete_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=12, is_completed=0)
        twelve_month_incomplete_goals_length = len(twelve_month_incomplete_goals)

        twelve_month_completed_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=12, is_completed=1)
        twelve_month_completed_goals_length = len(twelve_month_completed_goals)

        twelve_month_progress_percentage_deci = twelve_month_completed_goals_length / twelve_month_incomplete_goals_length
        twelve_month_progress_percentage = int(twelve_month_progress_percentage_deci * 100)

        template = 'netincome/list.html'
        
        context = {
            'net_income': net_income,
            'one_month_progress_percentage': one_month_progress_percentage,
            'three_month_progress_percentage': three_month_progress_percentage,
            'six_month_progress_percentage': six_month_progress_percentage,
            'twelve_month_progress_percentage': twelve_month_progress_percentage,
        }

        return render(request, template, context)