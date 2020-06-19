from django.shortcuts import render, redirect, reverse
from fundstrackerapp.models import FinancialGoal
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime


@login_required
def journal_entry_form(request):

    if request.method == 'GET':

        incomplete_financial_goals = FinancialGoal.objects.filter(user=request.user.id, is_completed=0)
        current_goals = []
        past_goals = []
        
        for goal in incomplete_financial_goals:
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

        for goal in incomplete_financial_goals:
            for past_goal in past_goals:
                if goal != past_goal:
                    current_goals.append(goal)

        print(past_goals)
        print(current_goals)


        template = 'journal/form.html'
        context = {}

        return render(request, template, context)
      
# @login_required
# def journal_entry_edit_form(request, goal_id):

#     if request.method == 'GET':
#         financial_goal = FinancialGoal.objects.get(pk=goal_id)

#         template = 'goals/form.html'
#         context = {
#             'financial_goal': financial_goal
#         }

#         return render(request, template, context)
