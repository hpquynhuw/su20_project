import tweepy
import os
import sys
import json

CONSUMER_KEY='NHBqJjf8SWmZkG5clkLAqQRDF'
CONSUMER_SECRET='hTJki4wA2JvijE5Yo07hjN3ssRSdyiDbzv4VhxIp2JS3i0deUp'
ACCESS_TOKEN_KEY='1271149860759232517-YKjVVWzJWOuOI2xEnrRa6jj9DsEkqh'
ACCESS_TOKEN_SECRET='2jEEFlyVIaO4QOXTA5bvPSy0anlE0MIDQYxjcycxXPiuO'

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY,ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

trends = api.trends_available()
print(type(trends[0]))
# trend = twitter.models.Trend()
with open('trends.json','w') as json_file:
  json.dump(trends[0:10],json_file)

# try:
#   trends = api.GetTrendsCurrent()
#   for trend in trends:
#     print(trend.param_defaults)
# except UnicodeDecodeError:
#   print("failed") 