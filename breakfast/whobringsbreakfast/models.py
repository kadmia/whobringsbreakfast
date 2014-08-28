from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date created')
    change_date = models.DateTimeField('date changed')
    active = models.BooleanField()
    group = models.ForeignKey('Group')


class Group(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date created')
    change_date = models.DateTimeField('date changed')
    active = models.BooleanField()
    users = models.ManyToManyField(User)

