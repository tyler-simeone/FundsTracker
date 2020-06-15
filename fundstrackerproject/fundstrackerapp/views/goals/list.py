from django.shortcuts import render, redirect, reverse
from fundstrackerapp.models import FinancialGoal
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def goal_list(request):

    if request.method == 'GET':
        one_month_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=1)
        three_month_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=3)
        six_month_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=6)
        twelve_month_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=12)

        template = 'goals/list.html'
        context = {
            'one_month_goals': one_month_goals,
            'three_month_goals': three_month_goals,
            'six_month_goals': six_month_goals,
            'twelve_month_goals': twelve_month_goals
        }

        return render(request, template, context)
