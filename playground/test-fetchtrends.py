import json
import requests
from secrets import twitter_token
from secrets import base_url
from datetime import date

class Test_FetchTrends:
    def __init__(self):
        trend_url=base_url+"trends/place.json?id="
        headers={"Authorization": "Bearer {}".format(twitter_token)}
        params = {
            'id': ['2490383','4118', '1105779', '44418'],
            'names': ['seattle','toronto', 'sydney','london']
            }
        today = date.today()
        for i, j in zip(params['id'],params['names']):
            url=trend_url+i
            res=requests.get(url, headers=headers)
            tweet_data=res.json()

            out_file = open(f"{j}_{today}.json", "w")
            json.dump(tweet_data, out_file, indent=6)
            out_file.close()

if __name__ == '__main__':
    cp=Test_FetchTrends()
