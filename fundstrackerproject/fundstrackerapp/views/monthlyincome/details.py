from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from fundstrackerapp.models import MonthlyIncome

def get_income_source(income_id):

    # returns an income source object from DB based
    # on income_id argument

    return MonthlyIncome.objects.get(pk=income_id)

@login_required
def income_details(request, income_id):

    # deletes an income source if the actual method in
    # the form has a DELETE value, updates the income
    # source's name and total value in the actual method
    # in the form has a PUT value
    
    income_source = get_income_source(income_id)

    if request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            income_source.delete()

            return redirect(reverse('fundstrackerapp:account'))
            
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            total = form_data['total']
            split_total = total.split(',')
            new_total = ''.join(split_total)

            income_source.name = form_data['name']
            income_source.total = new_total
            income_source.save()

            return redirect(reverse('fundstrackerapp:account'))

            