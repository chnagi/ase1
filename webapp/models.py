from django.db import models

# Create your models here.
class User(models.Model):
	auto_increment_id = models.AutoField(primary_key=True)
	Name=models.CharField(max_length=200)
	email=models.CharField(max_length=500)
	Roll_no=models.CharField(max_length=150)
	Distnace=models.FloatField(default=0)
	Velocity=models.FloatField(default=0)
	add_date = models.DateTimeField(auto_now_add=True)

