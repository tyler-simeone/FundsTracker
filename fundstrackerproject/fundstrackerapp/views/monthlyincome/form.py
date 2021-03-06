from django.shortcuts import render, redirect, reverse
from fundstrackerapp.models import MonthlyIncome
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def income_form(request):

    # renders a form to add income source

    if request.method == 'GET':

        template = 'incomesources/form.html'
        context = {}

        return render(request, template, context)
      
@login_required
def income_edit_form(request, income_id):

    # renders form to update existing income source values
    # being passed in
    
    income_source = MonthlyIncome.objects.get(pk=income_id)

    if income_source.user_id == request.user.id:

        if request.method == 'GET':

            template = 'incomesources/form.html'
            context = {
                'income_source': income_source
            }

            return render(request, template, context)

    else:

            return redirect(reverse('fundstrackerapp:home'))
