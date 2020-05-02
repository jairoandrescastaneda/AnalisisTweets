from tweepy.auth import OAuthHandler
import tweepy
from config.config import Config

class AuthTweet:
    #es una variable de clase que no debe llamarse desde afuera
    _api = None

    @classmethod
    def get_api_tweet(cls):
        if cls._api == None:
            api_tweet = cls.connect_api()
            cls._api = api_tweet
        

        return cls._api

    @staticmethod    
    def connect_api():
        config = Config()
        credentials = config.get_twittercredentials()
        auth_twiiter = tweepy.OAuthHandler(
            credentials['consumer_key'],
            credentials['consumer_secret']
            )
        auth_twiiter.set_access_token(
            credentials['access_token'],
            credentials['access_token_secret']
            )
        
        api_auth = tweepy.API(auth_twiiter)
        return api_auth
        
        
