import json
import requests
from secrets import twitter_token
from secrets import base_url
from datetime import date

# This can transverse through the json-trends file and fetch related popular tweets.
# Idea: Since some searches can come back null, eliminate those before saving the json files
class Test_Json:
    def __init__(self):
        self.key_info = ["created_at", "id", "text", "entities", "user", "in_reply_to_status_id", 
                         "in_reply_to_screen_name", "geo", "coordinates", "place", "is_quote_status", "retweet_count", 
                         "favorite_count", "lang" ]

        self.search_url=base_url+"search/tweets.json?"
        self.headers={"Authorization": "Bearer {}".format(twitter_token)}
        today = date.today()

        with open('toronto_2020-06-19.json') as json_file:
            data = json.load(json_file)
            for p in data[0]['trends']:
                name = p['name']
                query = p['query']
                url=self.search_url+"q="+query+"&result_type=popular&count=10"

                res=requests.get(url, headers=self.headers)
                tweet_data=res.json()

                with open(f"playground/trends/trend-{name}_{today}.json", "w") as out_file:
                    key_data = self.extract_key_info(tweet_data["statuses"])
                    json.dump(key_data,out_file,indent=4)
                # out_file = open(f"trend-{name}_{today}.json", "w")
                # json.dump(tweet_data, out_file, indent=6)
                # out_file.close()

        # Examples of query set-ups:
        #   https://api.twitter.com/1.1/search/tweets.json?q=twitterdev%20new%20premium
        #   https://api.twitter.com/1.1/search/tweets.json?q=%23superbowl&result_type=recent
    # def extract_key_info(self, statuses):
    #     output_dict = {"statuses" : []}
        
    #     for status in statuses:
    #         temp_dict = {}
    #         for key in status.keys():
    #             if key in self.key_info:
    #                 if key == "entities":
    #                     entities_dict = 
    #                 temp_dict.update({key : status[key]})
    #         output_dict["statuses"].append(temp_dict)
    #     return output_dict

    def extract_key_info(self, statuses):
        output_dict = {"statuses" : []}
        for status in statuses:
            tweet = {}
            for key in self.key_info:
                if key == "entities":
                    tweet[key] = self.extract_entities(status["entities"])
                elif key == "user":
                    tweet[key] = {"screen_name" : status["user"]["screen_name"], "id" : status["user"]["id"]}
                else:
                    tweet[key] = status[key]
            output_dict["statuses"].append(tweet)
        return output_dict

    def extract_entities(self, entities):
        hashtags = [i["text"] for i in entities["hashtags"]]
        mentions = [{"screen_name" : i["screen_name"], "id" : i["id"]} for i in entities["user_mentions"]]
        urls = [i["url"] for i in entities["urls"]]

        return {"hashtags" : hashtags,
                "user_mentions" : mentions,
                "urls" : urls}

if __name__ == '__main__':
    cp=Test_Json()
