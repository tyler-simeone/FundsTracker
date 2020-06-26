from django.shortcuts import render, redirect, reverse
from fundstrackerapp.models import FinancialGoal
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def past_goal_edit_form(request, goal_id):

    # renders form to re-open a past goal, with the
    # goal passed into the form being based on the goal_id
    
    financial_goal = FinancialGoal.objects.get(pk=goal_id)

    if financial_goal.user_id == request.user.id:

        if request.method == 'GET':

            template = 'pastgoals/form.html'
            context = {
                'financial_goal': financial_goal
            }

            return render(request, template, context)

    else:

        return redirect(reverse('fundstrackerapp:home'))
