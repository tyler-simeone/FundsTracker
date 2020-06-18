from django.shortcuts import render, redirect, reverse
from fundstrackerapp.models import JournalEntry
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def journal_list(request):

    if request.method == 'GET':
        all_entries = JournalEntry.objects.filter(user=request.user.id)
        user = User.objects.get(pk=request.user.id)

        template = 'journal/list.html'
        context = {
            'user': user,
            'all_entries': all_entries,
        }

        return render(request, template, context)
      
    # elif request.method == 'POST':
    #     form_data = request.POST

    #     if ("expense" in form_data):
    #         new_expense = MonthlyExpense.objects.create(
    #             name = form_data['name'],
    #             total = form_data['total'],
    #             user_id = request.user.id
    #         )
        
    #     else:
    #         new_income = MonthlyIncome.objects.create(
    #             name = form_data['name'],
    #             total = form_data['total'],
    #             user_id = request.user.id
    #         )        

    #     return redirect(reverse('fundstrackerapp:account'))