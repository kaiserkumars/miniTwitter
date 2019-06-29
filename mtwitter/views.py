from django.shortcuts import render
import twitter
from . import gettweets
from .models import TwitterData
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
# from .forms import TwitterDataForm


# def get_tweets():
#   """
#   returns twitter feed with settings as described below, contains all related twitter settings
#   """

#   user =''
#   api = twitter.Api(consumer_key='',
#                     consumer_secret='',
#                     access_token_key='',
#                     access_token_secret='')

#   statuses = api.GetUserTimeline(user_id=0,count=8)
#   print(statuses)
#   # return api.GetUserTimeline(screen_name=user, exclude_replies=True,count=20, include_rts=False)  
#   return statuses



@login_required
def home(request):
	context={}
	# print(get_tweets())

	context['tweets'] = gettweets.get_tweets()
	return render(request,'mtwitter/home.html',context)

@login_required
def search(request):
	query_string = ''
	found_entries = None
	if ('q' in request.GET) and request.GET['q'].strip():
		query_string = request.GET['q']
		lookups= Q(tweet__icontains=query_string)
		# print(lookups)
		tweets = TwitterData.objects.filter(Q(tweet__icontains=query_string)|Q(screen_name__icontains=query_string)).order_by('date')
		# print(str(tweets))
		context = { 'query_string': query_string, 'tweets': tweets }
		return render(request, 'mtwitter/search_results.html', context)
	else:
		return render(request, 'mtwitter/search_results.html', { 'query_string': 'Null', 'found_entries': 'Enter a search term' })

def logout(request):
	logout(request)
	return render(request,'mtwitter/logged_out.html')
# class TwitterDataCreateView(CreateView):
#     model = TwitterData
#     form_class = TwitterDataForm