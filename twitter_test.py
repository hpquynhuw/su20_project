import twitter
import os
import sys

api = twitter.Api(consumer_key='NHBqJjf8SWmZkG5clkLAqQRDF',
                  consumer_secret='hTJki4wA2JvijE5Yo07hjN3ssRSdyiDbzv4VhxIp2JS3i0deUp',
                  access_token_key='1271149860759232517-YKjVVWzJWOuOI2xEnrRa6jj9DsEkqh',
                  access_token_secret='2jEEFlyVIaO4QOXTA5bvPSy0anlE0MIDQYxjcycxXPiuO')

trend = twitter.models.Trend()


try:
  trends = api.GetTrendsCurrent()
  for trend in trends:
    print(trend.param_defaults)
except UnicodeDecodeError:
  print("failed")