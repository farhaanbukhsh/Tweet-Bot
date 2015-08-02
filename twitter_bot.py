import twitter
api = twitter.Api(consumer_key='bfSyTpNnSCza7I3kJcSuSju0H',consumer_secret='XDTKR5vTDBigySUm9UYl7S6dmZHrsTdsvoJ5uckAay5qPht8gp', access_token_key='59036562-3VMqfQv8T9jS2v2gBEhCJCCs9bYWYyYMoTKhjvWhA', access_token_secret='x1ANzuuRB7ikgqNXe1Rr4ihn0hkyTagrhWVl4AmZtxPPC')
favorite_hashtags = ['#mozilla','#mozlove','#python','#jnaapti','#msaan']
def follow_user_hashtags_fav(status_object):
  user_dict = dict()
  user_dict = status_object.AsDict()
  user_name = user_dict['user']['name']
  user_id = user_dict['user']['id']
  api.CreateFavorite(status_object)
  print 'You favorited this tweet : \n',status_object.text
  api.CreateFriendship(user_id)
  print 'You are following : \n',user_name
for hashtag in favorite_hashtags:
  print 'For hashtag : \t', hashtag
  list_statuses = api.GetSearch(hashtag)
  for status in list_statuses:
    try:
      follow_user_hashtags_fav(status)
    except twitter.error.TwitterError:
      print "Some Error may be you favorited it twice or you are following yourself"
