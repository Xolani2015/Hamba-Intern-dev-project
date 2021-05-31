from rest_framework import serializers

class TweetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweets
        fields = ('TweetId', 'TweetUser', 
        'TweetCreateDate', 'TweetSentiment')