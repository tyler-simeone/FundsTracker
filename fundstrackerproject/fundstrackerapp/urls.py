from django.urls import path, include
from fundstrackerapp.views import *

app_name = "fundstrackerapp"

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login', include('django.contrib.auth.urls'), name='login'),
    path('accounts/register', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('', net_income_list, name='home'),
    path('incomecalculation/', net_income_details, name='netincome_details'),
    path('account/', income_list, name='account'),
    path('account/addincome/', income_form, name='income_form'),
    path('account/updateincome/<int:income_id>/', income_edit_form, name='income_edit_form'),
    path('account/<int:income_id>/', income_details, name='income_source'),
    path('account/addexpense/', expense_form, name='expense_form'),
    path('account/updateexpense/<int:expense_id>/', expense_edit_form, name='expense_edit_form'),
    path('account/expense/<int:expense_id>/', expense_details, name='expense_details'),
    path('goals/', goal_list, name='goals'),
    path('goals/addgoal', goal_form, name='goal_form'),
    path('goals/<int:goal_id>/editgoal', goal_edit_form, name='goal_edit_form'),
    path('goals/<int:goal_id>', goal_details, name='goal_details'),
    path('goals/<int:goal_id>/complete', goal_completed, name='goal_completed'),
    path('goals/completed', goal_completed_list, name='goal_completed_list'),
    path('pastgoals/', past_goals_list, name='past_goals_list'),
    path('pastgoals/<int:goal_id>/form', past_goal_edit_form, name='past_goal_edit_form'),
    path('pastgoals/<int:goal_id>/', past_goal_details, name='past_goal_details'),
    path('journal/', journal_list, name='journal_list'),
    path('journal/addentry', journal_entry_form, name='journal_entry_form'),
    path('journal/<int:goal_id>/', journal_entry_details, name='journal_entry_details'),
    
]
