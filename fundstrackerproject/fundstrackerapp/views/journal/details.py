from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from fundstrackerapp.models import FinancialGoal, JournalEntry
from django.contrib.auth.models import User

def get_financial_goal(goal_id):
    
    # returns one goal based on goal_id argument

    return FinancialGoal.objects.get(pk=goal_id)

@login_required
def journal_entry_details(request, goal_id):

    # gets all journal entries that belong to a specific
    # financial goal, based on the goal_id argument, then
    # passing those matching entries into the template,
    # along with data for the logged-in user
    #       runs when entries btn clicked from current
    #       goals list
    
    user = User.objects.get(pk=request.user.id)
    financial_goal = get_financial_goal(goal_id)
    journal_entries = JournalEntry.objects.filter(user=request.user.id, financial_goal_id=financial_goal.id)

    
    if request.method == 'GET':
        
        template = 'journal/details.html'
        context = {
            'user': user,
            'journal_entries': journal_entries
        }

        return render(request, template, context)