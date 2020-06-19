from django.shortcuts import render, redirect, reverse
from fundstrackerapp.models import JournalEntry, FinancialGoal
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def journal_list(request):

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
      
    elif request.method == 'POST':
        form_data = request.POST
        
        new_entry = JournalEntry.objects.create(
            entry = form_data['entry'],
            user_id = request.user.id, 
            financial_goal_id = form_data['goal']
        )        

        return redirect(reverse('fundstrackerapp:journal_list'))