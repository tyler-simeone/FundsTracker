from django.db import models
from django.contrib.auth.models import User

class MonthlyExpense (models.Model):

    name = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=None, decimal_places=2)
    user = models.ManyToOneRel(User, on_delete=models.CASCADE)