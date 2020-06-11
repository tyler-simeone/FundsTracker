from django.db import models
from django.contrib.auth.models import User

class JournalEntry (models.Model):

    entry = models.CharField(max_length=250)
    user = models.ManyToOneRel(User, on_delete=models.CASCADE)