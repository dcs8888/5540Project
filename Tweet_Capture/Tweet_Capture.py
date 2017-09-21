from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys
import time

access_token = "908502750618619904-2nW38xadA7RD7jrtk3CrlDQXX8IoTHs"
access_token_secret = "czJk0wv9airHE0LMUjoGKxi2gUb38vQQFswQ99UuxYhOA"
consumer_key = "2ez9lVBRsTBYKhM5KAyBmTDJE"
consumer_secret = "aLD9lD9vX38pULHjp5By4k6dppZERzlnUdzgpGd9VnZpO3VmDd"

class Listener(StreamListener):

    def __init__(self, max=10):
        print(max)
        self.count = 0
        self.max = max
        self.file = open("tweet.json", "w")

    def on_data(self, data):
        self.file.write(data)
        self.count += 1
        if self.count >= self.max:
            sys.exit(0)

    def limit_handled(self, cursor):
        while True:
            try:
                cursor.next()
            except:
                time.sleep(15*60) # 15 minutes

    def on_error(self, status):
        if status_code == 420:
            return False
        print(status)

def main():

    listener = Listener(100000)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)

    #stream.filter(locations=[-125,25,-65,48], async=True)
    stream.sample()
    
if __name__ == '__main__':
    main()