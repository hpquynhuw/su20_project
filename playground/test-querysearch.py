import json
# import requests
from searchtweets import gen_rule_payload, ResultStream
from secrets import twitter_token
from secrets import base_url
from datetime import date

# This can return data for the specified query and time period.
# We will use the 30-day search period: /search/30day/Test.json
# and the searchtweets package
# Sandbox: 30 REQUESTS PER MINUTE, and 100 TWEETS PER REQUEST, MAX 25K TWEETS MONTHLY

class Test_Searchquery:
    def __init__(self):
        search_args={
            'bearer_token': twitter_token,
            'endpoint': base_url+"tweets/search/30day/Test.json",
            'extra_headers_dict': None
        }

        txt = input("Type query: ")
        QUERY=str(txt)
        MAX_CALL=20

        rule = gen_rule_payload(QUERY, results_per_call=MAX_CALL)

        rs = ResultStream(rule_payload=rule,
                  max_results=MAX_CALL,
                  max_pages=1,
                  **search_args)
        print(rs, end='\n\n')

        # out_file = open(f"sample_{QUERY}.json", "w")
        # json.dump(tweet_data, out_file, indent=6)
        # out_file.close()

        with open("sample-{0}.json".format(txt.replace(':','-')), 'w', encoding='utf-8') as f:
            for tweet in rs.stream():
                json.dump(tweet, f, indent=6)
                f.write('\n')
        print('done')

# TwitterDev%20%5C%22search%20api%5C%22
# sample: POST "https://api.twitter.com/1.1/tweets/search/:product/:label.json" -d
# '{"query":"TwitterDev "search api"",
# "maxResults":"500",
# "fromDate":"<yyyymmddhhmm>",
# "toDate":"<yyyymmddhhmm>"}'
# -H "Authorization: Bearer TOKEN"
        # Examples of query set-ups:
        #   https://api.twitter.com/1.1/search/tweets.json?q=twitterdev%20new%20premium
        #   https://api.twitter.com/1.1/search/tweets.json?q=%23superbowl&result_type=recent

if __name__ == '__main__':
    cp=Test_Searchquery()
