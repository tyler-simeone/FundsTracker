from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# from .journalentry import JournalEntry

class FinancialGoal (models.Model):

    goal = models.CharField(max_length=250)
    timeframe = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_count = 0

    class Meta:
        verbose_name = ("financial goal")
        verbose_name_plural = ("financial goals")

    def __str__(self):
        return f'{self.goal}'

    def get_absolute_url(self):
        return reverse("financialgoal_detail", kwargs={"pk": self.pk})

    # @property
    # def entry_count(self):
    #     entries = JournalEntry.objects.filter(financial_goal_id = self.id)

    #     return len(entries)