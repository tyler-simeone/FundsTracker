from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class MonthlyExpense (models.Model):

    name = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=None, decimal_places=2)
    user = models.ManyToOneRel(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("monthly expense")
        verbose_name_plural = ("monthly expenses")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("monthlyexpense_detail", kwargs={"pk": self.pk})