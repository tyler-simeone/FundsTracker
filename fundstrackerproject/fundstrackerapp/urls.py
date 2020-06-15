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
    path('account/<int:income_source_id>/', income_edit_form, name='income_source'),
]
