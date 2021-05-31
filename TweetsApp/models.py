from django.db import models

# Create your models here.

class Tweets(models.Model):
      TweetId = models.AutoField(primary_key=True)
      TweetUser = models.CharField(max_length=100)
      TweetCreateDate = models.DateField()
      TweetSentiment = models.CharField(max_length=100)

