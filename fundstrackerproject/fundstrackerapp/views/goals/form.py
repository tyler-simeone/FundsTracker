from django.shortcuts import render, redirect, reverse
from fundstrackerapp.models import FinancialGoal
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# these views will render the goal form template and
# the edit form view will pass in a goal object so the 
# form knows to display values to be edited when in edit mode

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
