from django.shortcuts import render, redirect, reverse
from fundstrackerapp.models import JournalEntry, FinancialGoal
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def journal_list(request):

    # render a list of journal entries as well as the goals
    # that belong to each entry

    if request.method == 'GET':
        all_entries = JournalEntry.objects.filter(user=request.user.id)
        goals = FinancialGoal.objects.filter(user=request.user.id)
        user = User.objects.get(pk=request.user.id)

        template = 'journal/list.html'
        context = {
            'user': user,
            'all_entries': all_entries,
            'goals': goals
        }

        return render(request, template, context)
      
    # checking to see if a financial goal has been selected from the
    # journal entry form, and if so will add an entry with a financial
    # goal FK tagged to it, and if not will just add a new journal 
    # entry without a financial_goal FK

    elif request.method == 'POST':
        form_data = request.POST
        form_data_dict = dict(form_data)

        if len(form_data_dict) == 3:
        
            new_entry = JournalEntry.objects.create(
                entry = form_data['entry'],
                user_id = request.user.id, 
                financial_goal_id = form_data['goal']
            )        

        else:

            new_entry = JournalEntry.objects.create(
                entry = form_data['entry'],
                user_id = request.user.id
            )

        return redirect(reverse('fundstrackerapp:journal_list'))