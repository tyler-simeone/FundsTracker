from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from fundstrackerapp.models import MonthlyExpense

def get_monthly_expense(expense_id):

    # returns a monthly expense object based on expense_id arg

    return MonthlyExpense.objects.get(pk=expense_id)

@login_required
def expense_details(request, expense_id):

    # deletes expense if actual method in the form contains
    # DELETE value, and editing the expense's name and new
    # cost value if the actual method contains PUT value
    
    monthly_expense = get_monthly_expense(expense_id)

    if request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            monthly_expense.delete()

            return redirect(reverse('fundstrackerapp:account'))
            
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            total = form_data['total']
            split_total = total.split(',')
            new_total = ''.join(split_total)

            monthly_expense.name = form_data['name']
            monthly_expense.total = new_total
            monthly_expense.save()

            return redirect(reverse('fundstrackerapp:account'))

            