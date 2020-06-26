from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from fundstrackerapp.models import FinancialGoal
from datetime import datetime

def get_financial_goal(goal_id):
    # returns one financial goal based on goal_id argument

    return FinancialGoal.objects.get(pk=goal_id)

@login_required
def past_goal_details(request, goal_id):
    
    # deletes a financial goal based on goal_id arg
    # if actual method in form is DELETE, and updates
    # the goal if actual method in form is PUT
    
    goal = get_financial_goal(goal_id)

    if request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            goal.delete()
            
            return redirect(reverse('fundstrackerapp:past_goals_list'))
            
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            goal.goal = form_data['name']
            goal.created_at = datetime.now()
            goal.timeframe = form_data['time_horizon']
            goal.is_completed = 0
            goal.save()

            return redirect(reverse('fundstrackerapp:goals'))

            