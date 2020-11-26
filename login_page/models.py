from django.db import models

# Create your models here.
class login_model(models.Model):
	username = models.TextField(default='n/a')
	password = models.TextField(default='n/a')
	mobile_no = models.DecimalField(decimal_places=0,max_digits=10,default=0000000000)
	auth = models.TextField(default='n/a')
	session_key = models.TextField(default='n/a')
	