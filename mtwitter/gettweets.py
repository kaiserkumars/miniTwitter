from mtwitter.models import TwitterData
import twitter
from dateutil.parser import parse
from mtwitter.settings import get_secret

def get_tweets():
	"""
	returns twitter feed with settings as described below, contains all related twitter settings
	"""

	user ='kaiserkumars'
	# api = twitter.Api(consumer_key='iJoZZuV7etVrJfE4K9ir8sIqa',
	#                   consumer_secret='uyJyWoP05z2MUKnggW7vHnIG2sckmM1aHRMgGveZLyrz8401Xs',
	#                   access_token_key='622588040-TYDgG1UlGUvA1hW8PA7mOG5CiMw0WiuPZlkoP8cc',
	#                   access_token_secret='laAmFjeLhWzOK7Y524VevdMdeLeNpnmCUmjee1AQU7osj')
	api = twitter.Api(consumer_key=get_secret('consumer_key'),
	                  consumer_secret=get_secret('consumer_secret'),
	                  access_token_key=get_secret('access_token_key'),
	                  access_token_secret=get_secret('access_token_secret'))

	statuses = api.GetUserTimeline(user_id=622588040,count=0)
	# print(statuses)
	# duplicate='UNIQUE constraint failed: mtwitter_weatherdata.location, core_weatherdata.metric, core_weatherdata.date'
	bulk_insert=[]
	# print(dir(TwitterData))
	for s in statuses:
		# print(s)
		dt = parse(s.created_at)
		# print(dt)
		data  = TwitterData(org_name=s.user.name,profile_url=s.user.profile_image_url,tweet_id =s.id,screen_name=s.user.screen_name, tweet = s.text, date= dt, favCount =0)
		bulk_insert.append(data)
	try:
		TwitterData.objects.bulk_create(bulk_insert)
		print("Success.")
	except Exception as e:
		# if(str(e)==duplicate):
		# 	print('Duplicate Data')
		# else:
		print(str(e))

	return statuses
