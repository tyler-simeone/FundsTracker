from django.shortcuts import render, redirect, reverse
from fundstrackerapp.models import FinancialGoal
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def past_goals_list(request):

    if request.method == 'GET':

        one_month_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=1)
        past_one_month_goals = []
        
        # Seeing if the goal's expiration date has been reached
        # (making it a past goal)
        #   getting created_at month, adding the timeframe int,
        #   now try to rejoin and parse date it to hopefully
        #   convert the > 12 nums to new year nums
        for goal in one_month_goals:
            goal_date_str = str(goal.created_at)
            goal_created_date = goal_date_str.split('-')
            goal_date_sliced = goal_created_date[0:3:2]
            
            exp_month = int(goal_created_date[1]) + goal.timeframe

            goal_date_sliced.insert(1, str(exp_month))
            goal_date = '-'.join(goal_date_sliced)
            

            # so I need to come up with a way to convert any exp month
            # that is > 12 into the correct next year's month
            if (exp_month > 12):
                # will add one year to the goal
                goal_year = str(int(goal_created_date[0]) + 1)

                # ie. 12 + 3 = 15 exp month, 10 + 6 = 16 exp month
                new_year_months = exp_month - goal.timeframe


            current_date = str(datetime.datetime.now())
            current_month = int(current_date.split('-')[1])
            print(goal_created_date, goal_date)

            # if (exp_month < current_month):
            #     past_one_month_goals.append(goal)
        
        print(past_one_month_goals)

        past_one_month_goals = 0
        past_three_month_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=3)
        past_six_month_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=6)
        past_twelve_month_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=12)

        template = 'goals/list.html'
        context = {
            'past_one_month_goals': past_one_month_goals,
            'past_three_month_goals': past_three_month_goals,
            'past_six_month_goals': past_six_month_goals,
            'past_twelve_month_goals': past_twelve_month_goals
        }

        return render(request, template, context)
    
    # elif request.method == 'POST':
    #     form_data = request.POST

    #     new_goal = FinancialGoal.objects.create(
    #         goal = form_data['name'],
    #         timeframe = form_data['time_horizon'],
    #         user_id = request.user.id
    #     )

    #     return redirect(reverse('fundstrackerapp:goals'))