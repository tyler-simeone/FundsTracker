from django.shortcuts import render, redirect, reverse
from fundstrackerapp.models import FinancialGoal
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def past_goals_list(request):

    if request.method == 'GET':

        users_goals = FinancialGoal.objects.filter(user=request.user.id)
        past_goals = []
        
        for goal in users_goals:
            goal_date_str = str(goal.created_at) 
            exp_year = int(goal_date_str.split('-')[0])
            exp_month = int(goal_date_str.split('-')[1]) + goal.timeframe
            if exp_month > 12:
                exp_year += 1
                exp_month -= 12
            exp_day_str = goal_date_str.split('-')[2]
            exp_day = int(exp_day_str.split()[0])

            curr_date = str(datetime.datetime.now())
            curr_date_str = curr_date.split()[0]
            curr_year = int(curr_date_str.split('-')[0])
            curr_month = int(curr_date_str.split('-')[1])
            curr_day = int(curr_date_str.split('-')[2])

            if exp_year < curr_year:
                past_goals.append(goal)
            elif exp_year == curr_year and exp_month < curr_month:
                past_goals.append(goal)
            elif exp_year == curr_year and exp_month == curr_month and exp_day < curr_day:
                past_goals.append(goal)
        

        template = 'pastgoals/list.html'
        context = {
            'past_goals': past_goals
        }

        return render(request, template, context)