from .auth.register import register
from .auth.logout import logout_user
from .home import home
from .netincome.list import net_income_list
from .netincome.details import net_income_details
from .monthlyincome.list import income_list
from .monthlyincome.form import income_form, income_edit_form
from .monthlyincome.details import income_details
from .monthlyexpense.form import expense_form, expense_edit_form
from .monthlyexpense.details import expense_details
from .goals.list import goal_list
from .goals.form import goal_form, goal_edit_form
from .goals.details import goal_details
from .pastgoals.list import past_goals_list