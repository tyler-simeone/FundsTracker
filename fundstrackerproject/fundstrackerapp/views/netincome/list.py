from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from fundstrackerapp.models import MonthlyIncome, MonthlyExpense, FinancialGoal
import datetime

@login_required
def net_income_list(request):

    # getting all incomes and expenses for the logged-in user,
    # finding the difference between the two totals to get net
    # income, then filtering past vs present goals, then getting
    # percentage of total current goals vs total completed goals,
    # then passing the net-income, the negatively-formatted net-income,
    # and the percentages for all timeframes into the homepage template

    if request.method == 'GET':

        all_incomes = MonthlyIncome.objects.filter(user=request.user.id)
        all_expenses = MonthlyExpense.objects.filter(user=request.user.id)

        total_income = 0
        total_expense = 0

        for income in all_incomes:
            total_income += income.total

        for expense in all_expenses:
            total_expense += expense.total

        net_income = total_income - total_expense

        new_net_income_str = ''
        if net_income < 0:
            net_income_str = str(net_income)
            new_net_income_str = net_income_str[1:]

        financial_goals = FinancialGoal.objects.filter(user=request.user.id)
        current_goals = []
        past_goals = []
        
        for goal in financial_goals:
            goal_date_str = str(goal.created_at) 
            exp_year = int(goal_date_str.split('-')[0])
            exp_month = int(goal_date_str.split('-')[1]) + goal.timeframe
            if exp_month > 12:
                exp_year += 1
                exp_month -= 12
            exp_day_str = goal_date_str.split('-')[2]
            exp_day = int(exp_day_str.split()[0])

            curr_date = str(datetime.datetime.now())
            curr_date_str = curr_date.split()[0]
            curr_year = int(curr_date_str.split('-')[0])
            curr_month = int(curr_date_str.split('-')[1])
            curr_day = int(curr_date_str.split('-')[2])

            if exp_year < curr_year:
                past_goals.append(goal)
            elif exp_year == curr_year and exp_month < curr_month:
                past_goals.append(goal)
            elif exp_year == curr_year and exp_month == curr_month and exp_day < curr_day:
                past_goals.append(goal)

        for goal in financial_goals:
            if goal not in past_goals:
                current_goals.append(goal)

    

        # ONE MONTH PROGRESS 
        one_month_total_goals = []
        one_month_progress_percentage = 0

        for goal in current_goals:
            if goal.timeframe == 1:
                one_month_total_goals.append(goal)
    

        if one_month_total_goals:
            one_month_total_goals_length = len(one_month_total_goals)

            one_month_completed_goals = []
            for goal in one_month_total_goals:
                if goal.is_completed == True:
                    one_month_completed_goals.append(goal)

            one_month_completed_goals_length = len(one_month_completed_goals)


            one_month_progress_percentage_deci = one_month_completed_goals_length / one_month_total_goals_length
            one_month_progress_percentage = int(one_month_progress_percentage_deci * 100)


        # THREE MONTH PROGRESS 
        three_month_total_goals = []
        three_month_progress_percentage = 0

        for goal in current_goals:
            if goal.timeframe == 3:
                three_month_total_goals.append(goal)

        if three_month_total_goals:
            three_month_total_goals_length = len(three_month_total_goals)

            three_month_completed_goals = []
            for goal in three_month_total_goals:
                if goal.is_completed == True:
                    three_month_completed_goals.append(goal)

            three_month_completed_goals_length = len(three_month_completed_goals)


            three_month_progress_percentage_deci = three_month_completed_goals_length / three_month_total_goals_length
            three_month_progress_percentage = int(three_month_progress_percentage_deci * 100)
        
        # SIX MONTH PROGRESS 
        six_month_total_goals = []
        six_month_progress_percentage = 0

        for goal in current_goals:
            if goal.timeframe == 6:
                six_month_total_goals.append(goal)

        if six_month_total_goals:
            six_month_total_goals_length = len(six_month_total_goals)

            six_month_completed_goals = []
            for goal in six_month_total_goals:
                if goal.is_completed == True:
                    six_month_completed_goals.append(goal)

            six_month_completed_goals_length = len(six_month_completed_goals)


            six_month_progress_percentage_deci = six_month_completed_goals_length / six_month_total_goals_length
            six_month_progress_percentage = int(six_month_progress_percentage_deci * 100)
        
        # TWELVE MONTH PROGRESS 
        twelve_month_total_goals = []
        twelve_month_progress_percentage = 0

        for goal in current_goals:
            if goal.timeframe == 12:
                twelve_month_total_goals.append(goal)

        if twelve_month_total_goals:
            twelve_month_total_goals_length = len(twelve_month_total_goals)

            twelve_month_completed_goals = []
            for goal in twelve_month_total_goals:
                if goal.is_completed == True:
                    twelve_month_completed_goals.append(goal)

            twelve_month_completed_goals_length = len(twelve_month_completed_goals)


            twelve_month_progress_percentage_deci = twelve_month_completed_goals_length / twelve_month_total_goals_length
            twelve_month_progress_percentage = int(twelve_month_progress_percentage_deci * 100)

        template = 'netincome/list.html'
        
        context = {
            'net_income': net_income,
            'new_net_income_str': new_net_income_str,
            'one_month_progress_percentage': one_month_progress_percentage,
            'three_month_progress_percentage': three_month_progress_percentage,
            'six_month_progress_percentage': six_month_progress_percentage,
            'twelve_month_progress_percentage': twelve_month_progress_percentage,
        }

        return render(request, template, context)