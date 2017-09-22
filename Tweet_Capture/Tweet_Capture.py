from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys
import time
import json

access_token = "908502750618619904-2nW38xadA7RD7jrtk3CrlDQXX8IoTHs"
access_token_secret = "czJk0wv9airHE0LMUjoGKxi2gUb38vQQFswQ99UuxYhOA"
consumer_key = "2ez9lVBRsTBYKhM5KAyBmTDJE"
consumer_secret = "aLD9lD9vX38pULHjp5By4k6dppZERzlnUdzgpGd9VnZpO3VmDd"

class Listener(StreamListener):

    def __init__(self, max=10):
        self.count = 0
        self.max = max

    def on_data(self, data):
        tweet_ok = CheckDeletedTweet(data)
        if (self.count >= self.max):
            sys.exit(0)
        if tweet_ok:
            self.count += 1
            CheckTweet(data)
        
            
    def limit_handled(self, cursor):
        while True:
            try:
                cursor.next()
            except:
                time.sleep(15*60) # 15 minutes

    def on_error(self, status):
        if status_code == 420:
            return False

def CheckTweet(tweet):
    loaded_tweet = json.loads(tweet)

    for line in loaded_tweet['entities']['urls']:
        if line.get('expanded_url'):
            print(line['expanded_url'].encode('utf-8').strip())

    for line in loaded_tweet['entities']['hashtags']:
        if line.get('text'):
            print(line['text'].encode('utf-8').strip())

def CheckDeletedTweet(tweet):
    if 'delete' in tweet:
        return False
    return True

def main():

    listener = Listener(100000)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)

    stream.sample()
    
if __name__ == '__main__':
    main()