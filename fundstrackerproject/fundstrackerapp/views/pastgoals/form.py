from django.shortcuts import render, redirect, reverse
from fundstrackerapp.models import FinancialGoal
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def past_goal_edit_form(request, goal_id):

    if request.method == 'GET':
        financial_goal = FinancialGoal.objects.get(pk=goal_id)

        template = 'pastgoals/form.html'
        context = {
            'financial_goal': financial_goal
        }

        return render(request, template, context)
