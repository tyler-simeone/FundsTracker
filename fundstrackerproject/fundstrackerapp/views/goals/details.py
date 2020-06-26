from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from fundstrackerapp.models import FinancialGoal

def get_financial_goal(goal_id):

    # returns one financial goal based on the PK
    # passed in as an argument

    return FinancialGoal.objects.get(pk=goal_id)

@login_required
def goal_details(request, goal_id):
    
    # update or delete a financial goal in the DB based
    # on actual method in the form making the POST request
    
    goal = get_financial_goal(goal_id)

    if request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            goal.delete()

            return redirect(reverse('fundstrackerapp:goals'))
            
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            goal.goal = form_data['name']
            goal.timeframe = form_data['time_horizon']
            goal.save()

            return redirect(reverse('fundstrackerapp:goals'))

            