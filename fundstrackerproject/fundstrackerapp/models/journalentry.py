from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class JournalEntry (models.Model):

    entry = models.CharField(max_length=250)
    user = models.ManyToOneRel(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("journal entry")
        verbose_name_plural = ("journal entries")

    def __str__(self):
        return self.entry

    def get_absolute_url(self):
        return reverse("journalentry_detail", kwargs={"pk": self.pk})