from django.shortcuts import render, redirect, reverse
from fundstrackerapp.models import FinancialGoal
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def goal_list(request):

    if request.method == 'GET':

        one_month_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=1, is_completed=0)
        past_one_month_goals = []
        
        # Seeing if the goal's expiration date has been reached
        # (making it a past goal)
        for goal in one_month_goals:

            # getting date from when goal was created
            goal_date_str = str(goal.created_at)
            goal_created_date = goal_date_str.split('-')
            goal_created_month = int(goal_created_date[1])   
            goal_created_day_list = goal_created_date[2].split()
            goal_created_day = int(goal_created_day_list[0])

            # creating expiration dates for the goal
            exp_month = goal_created_month + goal.timeframe
            exp_year = int(goal_created_date[0])
    

            # updating the year if the expiration month is past Dec.
            if (exp_month > 12):
                exp_year += 1
                exp_month -= 12

            # grabbing current date to check against the goal created
            current_date = str(datetime.datetime.now())
            current_month = int(current_date.split('-')[1])
            current_year = int(current_date.split('-')[0])
            current_day_list = current_date.split('-')[2]
            current_day = int(current_day_list.split()[0])

            if (exp_year < current_year):
                past_one_month_goals.append(goal)

            elif (exp_year == current_year and exp_month < current_month):
                past_one_month_goals.append(goal)
            
            elif (exp_year == current_year and exp_month == current_month and goal_created_day < current_day):
                past_one_month_goals.append(goal)
       
        one_month_current_goals = []

        for goal in one_month_goals:

            if goal not in past_one_month_goals:
                one_month_current_goals.append(goal)



        three_month_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=3, is_completed=0)
        past_three_month_goals = []
        
        # Seeing if the goal's expiration date has been reached
        # (making it a past goal)
        for goal in three_month_goals:

            # getting date from when goal was created
            goal_date_str = str(goal.created_at)
            goal_created_date = goal_date_str.split('-')
            goal_created_month = int(goal_created_date[1])   
            goal_created_day_list = goal_created_date[2].split()
            goal_created_day = int(goal_created_day_list[0])

            # creating expiration dates for the goal
            exp_month = goal_created_month + goal.timeframe
            exp_year = int(goal_created_date[0])
    

            # updating the year if the expiration month is past Dec.
            if (exp_month > 12):
                exp_year += 1
                exp_month -= 12

            # grabbing current date to check against the goal created
            current_date = str(datetime.datetime.now())
            current_month = int(current_date.split('-')[1])
            current_year = int(current_date.split('-')[0])
            current_day_list = current_date.split('-')[2]
            current_day = int(current_day_list.split()[0])

            if (exp_year < current_year):
                past_three_month_goals.append(goal)

            elif (exp_year == current_year and exp_month < current_month):
                past_three_month_goals.append(goal)
            
            elif (exp_year == current_year and exp_month == current_month and goal_created_day < current_day):
                past_three_month_goals.append(goal)
       
        three_month_current_goals = []

        for goal in three_month_goals:

            if goal not in past_three_month_goals:
                three_month_current_goals.append(goal)

        
        six_month_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=6, is_completed=0)
        past_six_month_goals = []
        
        # Seeing if the goal's expiration date has been reached
        # (making it a past goal)
        for goal in six_month_goals:

            # getting date from when goal was created
            goal_date_str = str(goal.created_at)
            goal_created_date = goal_date_str.split('-')
            goal_created_month = int(goal_created_date[1])   
            goal_created_day_list = goal_created_date[2].split()
            goal_created_day = int(goal_created_day_list[0])

            # creating expiration dates for the goal
            exp_month = goal_created_month + goal.timeframe
            exp_year = int(goal_created_date[0])
    

            # updating the year if the expiration month is past Dec.
            if (exp_month > 12):
                exp_year += 1
                exp_month -= 12

            # grabbing current date to check against the goal created
            current_date = str(datetime.datetime.now())
            current_month = int(current_date.split('-')[1])
            current_year = int(current_date.split('-')[0])
            current_day_list = current_date.split('-')[2]
            current_day = int(current_day_list.split()[0])

            if (exp_year < current_year):
                past_six_month_goals.append(goal)

            elif (exp_year == current_year and exp_month < current_month):
                past_six_month_goals.append(goal)
            
            elif (exp_year == current_year and exp_month == current_month and goal_created_day < current_day):
                past_six_month_goals.append(goal)
       
        six_month_current_goals = []

        for goal in six_month_goals:

            if goal not in past_six_month_goals:
                six_month_current_goals.append(goal)
        
        
        twelve_month_goals = FinancialGoal.objects.filter(user=request.user.id, timeframe=12, is_completed=0)
        past_twelve_month_goals = []
        
        # Seeing if the goal's expiration date has been reached
        # (making it a past goal)
        for goal in twelve_month_goals:

            # getting date from when goal was created
            goal_date_str = str(goal.created_at)
            goal_created_date = goal_date_str.split('-')
            goal_created_month = int(goal_created_date[1])   
            goal_created_day_list = goal_created_date[2].split()
            goal_created_day = int(goal_created_day_list[0])

            # creating expiration dates for the goal
            exp_month = goal_created_month + goal.timeframe
            exp_year = int(goal_created_date[0])
    

            # updating the year if the expiration month is past Dec.
            if (exp_month > 12):
                exp_year += 1
                exp_month -= 12

            # grabbing current date to check against the goal created
            current_date = str(datetime.datetime.now())
            current_month = int(current_date.split('-')[1])
            current_year = int(current_date.split('-')[0])
            current_day_list = current_date.split('-')[2]
            current_day = int(current_day_list.split()[0])

            if (exp_year < current_year):
                past_twelve_month_goals.append(goal)

            elif (exp_year == current_year and exp_month < current_month):
                past_twelve_month_goals.append(goal)
            
            elif (exp_year == current_year and exp_month == current_month and goal_created_day < current_day):
                past_twelve_month_goals.append(goal)
       
        twelve_month_current_goals = []

        for goal in twelve_month_goals:

            if goal not in past_twelve_month_goals:
                twelve_month_current_goals.append(goal)

        template = 'goals/list.html'
        context = {
            'one_month_current_goals': one_month_current_goals,
            'three_month_current_goals': three_month_current_goals,
            'six_month_current_goals': six_month_current_goals,
            'twelve_month_current_goals': twelve_month_current_goals
        }

        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST

        new_goal = FinancialGoal.objects.create(
            goal = form_data['name'],
            timeframe = form_data['time_horizon'],
            user_id = request.user.id,
            is_completed = 0
        )

        return redirect(reverse('fundstrackerapp:goals'))