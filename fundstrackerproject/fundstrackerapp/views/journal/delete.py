from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from fundstrackerapp.models import JournalEntry


@login_required
def journal_entry_delete(request, entry_id):

    entry = JournalEntry.objects.get(pk=entry_id)

    if request.method == 'POST':
        
        form_data = request.POST
        
        if (
                "actual_method" in form_data
                and form_data["actual_method"] == "DELETE"
            ):
                entry.delete()

                return redirect(reverse('fundstrackerapp:journal_list'))