from django.shortcuts import render, redirect, reverse
from fundstrackerapp.models import FinancialGoal
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def goal_list(request):

    if request.method == 'GET':
        goals = FinancialGoal.objects.get(user=request.user.id)

        template = 'goals/list.html'
        context = {
            'goals': goals
        }

        return render(request, template, context)
