from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "908502750618619904-2nW38xadA7RD7jrtk3CrlDQXX8IoTHs"
access_token_secret = "czJk0wv9airHE0LMUjoGKxi2gUb38vQQFswQ99UuxYhOA"
consumer_key = "2ez9lVBRsTBYKhM5KAyBmTDJE"
consumer_secret = "aLD9lD9vX38pULHjp5By4k6dppZERzlnUdzgpGd9VnZpO3VmDd"


#This is a basic listener that just prints received tweets to stdout.
class Listener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)



def main():
    #This handles Twitter authenification and the connection to Twitter Streaming API
    listener = Listener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
	
	
if __name__ == '__main__':
	main()