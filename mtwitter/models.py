from django.db import models
from datetime import date

class TwitterData(models.Model):
	screen_name = models.CharField(max_length=50)
	org_name = models.CharField(max_length=50,default="")
	tweet = models.TextField()
	tweet_id = models.BigIntegerField(default=0)	
	date = models.DateField()
	profile_url = models.URLField(default="")
	favCount = models.IntegerField()
	class Meta:
		unique_together=(('screen_name','tweet'),) #To prevent duplicate records
	def __str__(self):
		return self.tweet

