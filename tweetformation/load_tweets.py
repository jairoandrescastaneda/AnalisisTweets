import tweepy
#from tweetpy import TweepError, RateLimitError
from auth.auth import AuthTweet
from config.config import Config

class LoadTweet:

    def __init__(self):
        config = Config()
        self.twitter_credentials = config.get_twittercredentials()
        self.api_tweet = AuthTweet.get_api_tweet()


    def tweets_hometimeline(self, user_id, lastweet_id=None):
        parameters = None
        if lastweet_id is not None:
            parameters = {

                "since_id":lastweet_id,
                "tweet_mode":"extended"
            }
        else:
            parameters = {
                "id":user_id,
                "tweet_mode":"extended"
            }
        #** convierte los valores de un diccionario a los parametros de un metodo
        home_timeline = tweepy.Cursor(
            self.api_tweet.user_timeline,
            **parameters
            ).items()
        return home_timeline

    def tweets_search(self, query_search, lastweet_id=None):
        parameters = None
        
        if lastweet_id is not None:
            parameters = {
            "q":query_search,
            "since_id":lastweet_id,
            "lang":"es",
            "result_type":"mixed",
            "tweet_mode":"extended"
            }
        else:
            
            parameters = {
            "q":query_search,
            "lang":"es",
            "result_type":"mixed",
            "tweet_mode":"extended"
            }

        
        result_search = tweepy.Cursor(
            self.api_tweet.search,
            **parameters
            ).items()

        
        return result_search
    


    

