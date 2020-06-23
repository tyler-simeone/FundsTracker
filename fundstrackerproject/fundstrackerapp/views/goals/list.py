from django.shortcuts import render, redirect, reverse
from fundstrackerapp.models import FinancialGoal, JournalEntry
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def goal_list(request):

    if request.method == 'GET':

        journal_entries = JournalEntry.objects.filter(user=request.user.id)
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
            if goal not in past_goals:
                current_goals.append(goal)
    
        template = 'goals/list.html'
        context = {
            'current_goals': current_goals,
            'journal_entries': journal_entries,
        }

        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST

        new_goal = FinancialGoal.objects.create(
            goal = form_data['name'],
            timeframe = form_data['time_horizon'],
            user_id = request.user.id,
            is_completed = 0
        )

        return redirect(reverse('fundstrackerapp:goals'))