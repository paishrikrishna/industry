from django.db import models

# Create your models here.
class messages_model(models.Model):
	sender = models.TextField(default='n/a')
	rx = models.TextField(default='n/a')
	message = models.TextField(default='n/a')
	date = models.TextField(default='n/a')
	time = models.TextField(default='n/a')
	