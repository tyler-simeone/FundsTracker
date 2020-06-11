from django.db import models
from django.contrib.auth.models import User

class FinancialGoal (models.Model):

    goal = models.CharField(max_length=250)
    timeframe = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ManyToOneRel(User, on_delete=models.CASCADE)