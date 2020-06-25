from django.shortcuts import render, redirect, reverse
from fundstrackerapp.models import FinancialGoal
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def goal_completed_list(request):

    # get all financial goals whose is_completed field is True
    # and pass them to the completed list template

    if request.method == 'GET':

        completed_goals = FinancialGoal.objects.filter(user=request.user.id, is_completed=1)

        template = 'goals/completed.html'
        context = {
            'completed_goals': completed_goals
        }

        return render(request, template, context)