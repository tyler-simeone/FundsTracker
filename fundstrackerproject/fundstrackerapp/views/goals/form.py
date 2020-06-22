from django.shortcuts import render, redirect, reverse
from fundstrackerapp.models import FinancialGoal
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def goal_form(request):

    if request.method == 'GET':

        template = 'goals/form.html'
        context = {}

        return render(request, template, context)
      
@login_required
def goal_edit_form(request, goal_id):

    financial_goal = FinancialGoal.objects.get(pk=goal_id)
    
    if financial_goal.user_id == request.user.id:

        if request.method == 'GET':

            template = 'goals/form.html'
            context = {
                'financial_goal': financial_goal
            }

            return render(request, template, context)


    else:
        return redirect(reverse('fundstrackerapp:home'))
