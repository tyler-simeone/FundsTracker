from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class MonthlyIncome (models.Model):

    name = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=None, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("monthly income")
        verbose_name_plural = ("monthly incomes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("monthlyincome_detail", kwargs={"pk": self.pk})
    