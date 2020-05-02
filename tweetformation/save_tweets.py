from models.account_twitter import AccountTwitter
from models.information_tweet import TweetInformation
from .load_tweets import LoadTweet

class SaveTweet:

    def __init__(self):
        pass

    def validate_tweet_id(self,id_tweet):
        return TweetInformation.objects(tweet_id=id_tweet).first()

    def is_retweet(self,tweet):
        return hasattr(tweet,'retweeted_status')

    def is_quoted_retweet(self,tweet):
        return hasattr(tweet,'quoted_status')

    def save_tweet(self, tweet, store):
        user = tweet.user
        
        tweet_information = TweetInformation(
                    tweet_id=tweet.id_str,
                    text_full=tweet.full_text,
                    coordinates=tweet.coordinates,
                    created_at=tweet.created_at,
                    stores = [store],
                    screen_name = user.screen_name
                )
        tweet_object = self.validate_tweet_id(id_tweet=tweet.id_str)
        if tweet_object is None:
            tweet_information.save()
        else:
            tweet_object.stores.append(store)
            tweet_object.save()


    def build_query_twitter(self,twitter_account):
        twitter_account = twitter_account[1:len(twitter_account)]
        query = "%40"+twitter_account
        return query


    def main(self):
        load_tweet = LoadTweet()
        accounts_twitter = AccountTwitter.objects
        #Tweets Search
        for account_twitter in accounts_twitter:
            query_search = self.build_query_twitter(account_twitter.account)
            list_tweets = load_tweet.tweets_search(query_search=query_search)
            
            for tweet in list_tweets:
                
                if self.is_retweet(tweet):
                    tweet = tweet.retweeted_status
                elif self.is_quoted_retweet(tweet):
                    self.save_tweet(tweet.quoted_status,account_twitter.account)

                self.save_tweet(tweet,account_twitter.account)
        



