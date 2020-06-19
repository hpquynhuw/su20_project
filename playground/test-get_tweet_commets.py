import json
import requests
import twitter
# from secrets import twitter_token
# from secrets import base_url
from datetime import date

base_url = "https://api.twitter.com/1.1/search/tweets.json?"
twitter_token = "AAAAAAAAAAAAAAAAAAAAAO5PFAEAAAAAnoUc%2Fd2Il%2BZ6KQc7HShNsy7rxLU%3D60JcWQIOtliYFabGPYfS6yWJsgSd7tjyDBQEgheQO1hkVccTjh"
headers={"Authorization": "Bearer {}".format(twitter_token)}

tweet_id = "1272833566171230208"
tweet_username = "LAL2020_Champs"

url = base_url + "q=to:{}&sinceId={}&result_type=recent".format(tweet_username,tweet_id)

res = requests.get(url,headers=headers)
tweet_data = res.json()
# print(tweet_data)

tweet_replies = []
for tweet in tweet_data["statuses"]:
  print(tweet["in_reply_to_status_id_str"])
  # if tweet["in_reply_to_status_id_str"] == tweet_id:
  tweet_replies.append(tweet)

# print(tweet_replies)
  

# with open("./tweet_replies_recent.json",'w') as json_file:
#   json.dump(tweet_replies,json_file,indent=2)

# print(tweet_data)