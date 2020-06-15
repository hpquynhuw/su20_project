import twitter
import json

CONSUMER_KEY='NHBqJjf8SWmZkG5clkLAqQRDF'
CONSUMER_SECRET='hTJki4wA2JvijE5Yo07hjN3ssRSdyiDbzv4VhxIp2JS3i0deUp'
ACCESS_TOKEN_KEY='1271149860759232517-YKjVVWzJWOuOI2xEnrRa6jj9DsEkqh'
ACCESS_TOKEN_SECRET='2jEEFlyVIaO4QOXTA5bvPSy0anlE0MIDQYxjcycxXPiuO'

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN_KEY,
                  access_token_secret=ACCESS_TOKEN_SECRET)

trends = api.GetTrendsCurrent()
# print(trends[0].__dict__)

search_results = api.GetSearch(raw_query='q=%23COVID&result_type=popular&count=10',geocode='43.653225,-79.383186,10km')

sample = search_results[0].AsDict()
# print(sample)
print(sample.keys())

# with open('search_results.json','w') as json_file:
#   json.dump(search_results[0].AsJsonString(),json_file)