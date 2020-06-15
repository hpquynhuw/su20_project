import json
import requests
from secrets import twitter_token
from secrets import base_url
from datetime import date

# This can transverse through the json-trends file and fetch related popular tweets.
# Idea: Since some searches can come back null, eliminate those before saving the json files
class Test_Json:
    def __init__(self):
        search_url=base_url+"search/tweets.json?"
        headers={"Authorization": "Bearer {}".format(twitter_token)}
        today = date.today()

        with open('seattle_2020-06-13.json') as json_file:
            data = json.load(json_file)
            for p in data[]['trends']:
                name = p['name']
                query = p['query']
                url=search_url+"q="+query+"&result_type=popular&count=10"

                res=requests.get(url, headers=headers)
                tweet_data=res.json()

                out_file = open(f"trend-{name}_{today}.json", "w")
                json.dump(tweet_data, out_file, indent=6)
                out_file.close()

        # Examples of query set-ups:
        #   https://api.twitter.com/1.1/search/tweets.json?q=twitterdev%20new%20premium
        #   https://api.twitter.com/1.1/search/tweets.json?q=%23superbowl&result_type=recent

if __name__ == '__main__':
    cp=Test_Json()
