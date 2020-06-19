import json
from secrets import twitter_token
from secrets import base_url
from datetime import date
from searchtweets import gen_rule_payload, ResultStream

# This can be used to search up related tweets of trending topics, not
# necessarily popular tweets, but tweets in general within last 30 days

class Test_Search30:
    def __init__(self):
        search_args={
            'bearer_token': twitter_token,
            'endpoint': base_url+"tweets/search/30day/Test.json",
            'extra_headers_dict': None
        }

        today = date.today()
        #query = "q=" + self.buildQuery(params)
        FILE_NAME=input("Insert trend file name: ")
        MAX_CALL=20

        with open(FILE_NAME) as json_file:
            data = json.load(json_file)
            for p in data[0]['trends']:
                name = p['name']
                QUERY=name

                rule = gen_rule_payload(QUERY, results_per_call=MAX_CALL)

                rs = ResultStream(rule_payload=rule,
                          max_results=MAX_CALL,
                          max_pages=1,
                          **search_args)

                # TOTALLY FORGOT ABOUT REQUESTS RATE
                # CAN'T DO THIS FOR A TREND FILE SINCE THERE ARE OVER 20 TRENDS

                with open(f"trend30-{name}-{today}.json", 'w', encoding='utf-8') as f:
                    for tweet in rs.stream():
                        json.dump(tweet, f, indent=6)
                        f.write('\n')
                print('done')

        # Examples of query set-ups:
        #   https://api.twitter.com/1.1/search/tweets.json?q=twitterdev%20new%20premium
        #   https://api.twitter.com/1.1/search/tweets.json?q=%23superbowl&result_type=recent

if __name__ == '__main__':
    cp=Test_Search30()
