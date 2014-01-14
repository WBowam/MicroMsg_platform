from django.db import models

# Create your models here.
class Yijian(models.Model):
	brief=models.CharField(max_length=50)
	content=models.TextField()