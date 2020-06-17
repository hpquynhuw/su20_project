

import json
import requests
from secrets import twitter_token
from secrets import base_url
from datetime import date

# This can return data for the specified query and time period.
# We will use the 30-day period: /search/30day/:label.json
# The function below is using POST instead of GET
#  'next' token (from result json file) can be used in a subsequent request
#  to retrieve the next portion of the matching Tweets for that query
class Test_Searchdata:
    def __init__(self):
        search_url=base_url+"/search/30day/dev.json"
        headers={"Authorization": "Bearer {}".format(twitter_token)}
        today = date.today()

        request_body = json.dumps({
            "query": "Twitter",
            "maxResults": "100",
            "fromDate": "202006090000"
            # "toDate":
        })
# TwitterDev%20%5C%22search%20api%5C%22
# sample: POST "https://api.twitter.com/1.1/tweets/search/:product/:label.json" -d
# '{"query":"TwitterDev "search api"",
# "maxResults":"500",
# "fromDate":"<yyyymmddhhmm>",
# "toDate":"<yyyymmddhhmm>"}'
# -H "Authorization: Bearer TOKEN"
        #query = "https://api.spotify.com/v1/users/{}/playlists".format(
        #    spotify_user_id)

        response = requests.post(
            search_url,
            data=request_body,
            headers=headers
        )
        res = response.json()

        out_file = open(f"search-sample_{today}.json", "w")
        json.dump(res, out_file, indent=6)
        out_file.close()

        # Examples of query set-ups:
        #   https://api.twitter.com/1.1/search/tweets.json?q=twitterdev%20new%20premium
        #   https://api.twitter.com/1.1/search/tweets.json?q=%23superbowl&result_type=recent

if __name__ == '__main__':
    cp=Test_Searchdata()
