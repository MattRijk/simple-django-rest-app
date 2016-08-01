from __future__ import unicode_literals
from django.contrib.auth.models import User, Group
from django.db import models



YEAR_IN_SCHOOL_CHOICES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
)

from django.db import models

class Project(models.Model):
    NOT_STARTED_YET = 'NOT_STARTED_YET'
    ON_GOING = 'ON_GOING'
    JUST_STARTED = 'JUST_STARTED'
    ENDED = 'ENDED'
    LESS_THAN_WEEK = 'LESS_THAN_WEEK'
    
    STATUS_CHOICES = (
        (NOT_STARTED_YET, 'not_started_yet'),
        (ON_GOING, 'on_going'),
        (JUST_STARTED, 'just_started'),
        (ENDED, 'ended'),
        (LESS_THAN_WEEK, 'less_than_week'),
    )
    
    title = models.CharField(max_length = 50)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=NOT_STARTED_YET)
    group = models.ForeignKey('auth.Group')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.title
    
   
# class Team(models.Model):
#     group = models.CharField(max_length = 50)
#     email = models.CharField(max_length = 50)
    
#     def __str__(self):
#         return self.group