from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class FinancialGoal (models.Model):

    goal = models.CharField(max_length=250)
    timeframe = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("financial goal")
        verbose_name_plural = ("financial goals")

    def __str__(self):
        return f'{self.goal}'

    def get_absolute_url(self):
        return reverse("financialgoal_detail", kwargs={"pk": self.pk})