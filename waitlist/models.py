from __future__ import unicode_literals

from django.db import models

class WaitlistEntry(models.Model):
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.email

class Notification(models.Model):
    pass
