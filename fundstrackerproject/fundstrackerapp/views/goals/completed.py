from django.shortcuts import render, redirect, reverse
from fundstrackerapp.models import FinancialGoal
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def goal_completed(request, goal_id):

    if request.method == 'GET':

        # goal = FinancialGoal.objects.get(pk=goal_id)
        # goal.is_completed = 1
        # goal.save()

        completed_goals = FinancialGoal.objects.filter(user=request.user.id, is_completed=1)



        template = 'goals/completed.html'
        context = {
            'completed_goals': completed_goals
        }

        return render(request, template, context)

    if request.method == 'POST':
        form_data = request.POST
            
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            goal = FinancialGoal.objects.get(pk=goal_id)
            goal.is_completed = 1
            goal.save()

            return redirect(reverse('fundstrackerapp:goals'))

            