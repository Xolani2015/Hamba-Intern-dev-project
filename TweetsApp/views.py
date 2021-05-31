from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from TweetsApp.models import Tweets
from TweetsApp.serializers import TweetsSerializer


# Create your views here.

@csrf_exempt
def TweetsApi(request, id=0):
    if request.method=='GET':
        tweets = Tweets.objects.all()
        tweets_serializer = TweetsSerializer(tweets, many=True)
        return JsonResponse(tweets_serializer.data, safe=False)

        elif request.method == 'POST':
            tweets_data = JSONParser().parse(request)
            tweets_serializer = TweetsSerializer(data=tweets_data)
            if tweets_serializer.is_valid():
                tweets_serializer.save()
                return JsonResponse("Added Successfully!!", safe=False)
            return JsonResponse("Failed to Add.", safe=False)


        elif request.method=='PUT':
            tweets_data = JSONParser().parse(request)
            tweets= Tweets.objects.get(Tweetid=tweets_data['Tweetsid'])
            tweets_serializer=TweetsSerializer(tweets, data=tweets_data)
            if tweets_serializer.is_valid():
                tweets_serializer.save()
                return JsonResponse("Updated succefully", safe=False)
            return JsonResponse("Failed to Update", safe=False)

        
        elif request.method=='DELETE':
            tweets = Tweets.objects.get(Tweetid=id)
            tweets.delete()
            return JsonResponse("Deleted Succefully," safe=False)