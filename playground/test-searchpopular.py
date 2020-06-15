import json
import requests
from secrets import twitter_token
from secrets import base_url
from datetime import date


# This can be used to search up particular tweets that contain query indicated by user.

class Test_Searchpopular:
    def __init__(self):
        search_url=base_url+"search/tweets.json?"
        headers={"Authorization": "Bearer {}".format(twitter_token)}

        # params = {
        #    'must': [],
        #    'phrases': ['lebron', 'bailing'],
        #    'tags': ['blm', 'usa']
        #    }
        today = date.today()
        #query = "q=" + self.buildQuery(params)

        # Examples of query set-ups:
        #   https://api.twitter.com/1.1/search/tweets.json?q=twitterdev%20new%20premium
        #   https://api.twitter.com/1.1/search/tweets.json?q=%23superbowl&result_type=recent
        url=search_url+"q=%23CapitolHillAutonomousZone&result_type=popular&count=10"


        res=requests.get(url, headers=headers)
        tweet_data=res.json()

        out_file = open(f"sample_{today}.json", "w")
        json.dump(tweet_data, out_file, indent=6)
        out_file.close()

    # From user's input, we can build the query search for search
    # Not all query builder operators are included below
    def buildQuery(self, params):
        space="%20"
        exact="%22"
        htag="%23"

        query = ""
        for i in params['must']:
            query=query+exact+i+exact+space
        for i in params['phrases']:
            query=query+i+space
        for i in params['tags']:
            query=query+htag+i+space

        return query[:-3]

if __name__ == '__main__':
    cp=Test_Searchpopular()
