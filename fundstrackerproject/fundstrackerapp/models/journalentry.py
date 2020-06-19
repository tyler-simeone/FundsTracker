from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .financialgoal import FinancialGoal

class JournalEntry (models.Model):

    entry = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    financial_goal = models.ForeignKey(FinancialGoal, default=4, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("journal entry")
        verbose_name_plural = ("journal entries")

    def __str__(self):
        return self.entry

    def get_absolute_url(self):
        return reverse("journalentry_detail", kwargs={"pk": self.pk})