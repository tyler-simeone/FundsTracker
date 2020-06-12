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
    # Below endpoint will trigger when Account page is viewed
    path('account/', income_list, name='account'),
    # path('incomes/add/', add_income, name='income_form'),
]
