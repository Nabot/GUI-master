from django.db import models


# the following lines added:
import datetime
from django.utils import timezone


# class Tasks(models.Model):
#    task_name = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('Date to do task')
#
#    def __str__(self):
#        return self.task_name

# def was_published_recently(self):
#     now = timezone.now()
#     return now - datetime.timedelta(days=1) <= self.pub_date <= now
#
# was_published_recently.admin_order_field = 'pub_date'
# was_published_recently.boolean = True
# was_published_recently.short_description = 'Published recently?'
#

# class Choice(models.Model):
#    question = models.ForeignKey(Tasks)
#    choice_test = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)
#
#    def __str__(self):
#        return self.choice_test

# class roomdata(models.model):
#     temperature = models.IntegerField(default=0)
#     humidity = models.IntegerField(default=0)
#
#     def __str__(self):
#          return self.temperature

    




