from django.urls import path, include
# from views import *

app_name = "fundstrackerapp"

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
]
