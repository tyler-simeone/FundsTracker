from django.shortcuts import render, redirect, reverse
from fundstrackerapp.models import FinancialGoal
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def past_goals_list(request):

    if request.method == 'GET':

        one_month_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=1)
        past_one_month_goals = []
        
        # Seeing if the goal's expiration date has been reached
        # (making it a past goal)
        for goal in one_month_goals:
            goal_date_str = str(goal.created_at)
            goal_month = goal_date_str.split('-')[1]

            exp_month = int(goal_month) + goal.timeframe

            current_date = str(datetime.datetime.now())
            current_month = int(current_date.split('-')[1])
            print(exp_month, current_month)

            if (exp_month < current_month):
                past_one_month_goals.append(goal)
        
        print(past_one_month_goals)

        past_one_month_goals = 0
        past_three_month_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=3)
        past_six_month_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=6)
        past_twelve_month_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=12)

        template = 'goals/list.html'
        context = {
            'past_one_month_goals': past_one_month_goals,
            'past_three_month_goals': past_three_month_goals,
            'past_six_month_goals': past_six_month_goals,
            'past_twelve_month_goals': past_twelve_month_goals
        }

        return render(request, template, context)
    
    # elif request.method == 'POST':
    #     form_data = request.POST

    #     new_goal = FinancialGoal.objects.create(
    #         goal = form_data['name'],
    #         timeframe = form_data['time_horizon'],
    #         user_id = request.user.id
    #     )

    #     return redirect(reverse('fundstrackerapp:goals'))