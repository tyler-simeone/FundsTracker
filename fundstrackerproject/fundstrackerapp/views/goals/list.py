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
    
    elif request.method == 'POST':
        form_data = request.POST

        new_goal = FinancialGoal.objects.create(
            goal = form_data['name'],
            timeframe = form_data['time_horizon'],
            user_id = request.user.id
        )

        return redirect(reverse('fundstrackerapp:goals'))