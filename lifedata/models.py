from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from datetime import timedelta, datetime

class Sleep(models.Model):
	QUALITY_CHOICES = (('POOR', 'Poor'), ('GOOD', 'Good'), ('EXCELLENT', 'Excellent'))

	bedtime = models.DateTimeField()
	wakeup_time = models.DateTimeField()
	quality = models.CharField(max_length= 15, choices = QUALITY_CHOICES, default = 'GOOD')
	description = models.TextField()
	
	def __str__(self):
		hours = self.sleep_duration.seconds // 3600
		mins = (self.sleep_duration.seconds - (hours * 3600)) // 60
		return str(hours) + " hours " + str(mins) + " mins"
	
	@property # returns it in hours
	def sleep_duration(self):
		return (self.wakeup_time - self.bedtime)/3600

class Discipline(models.Model):
	DISCIPLINE_CHOICES = (('YES', 'Yes'), ('NO', 'No'))

	date = models.DateField(default = datetime.today)
	discipline = models.CharField(max_length  = 3, choices = DISCIPLINE_CHOICES, default = 'YES')