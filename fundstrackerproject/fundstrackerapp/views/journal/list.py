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
      
    # Need to figure out how to add new entry's ID as FK to 
    # financial goal
    elif request.method == 'POST':
        form_data = request.POST
        
        new_entry = JournalEntry.objects.create(
            entry = form_data['entry'],
            user_id = request.user.id
        )        

        return redirect(reverse('fundstrackerapp:journal_list'))