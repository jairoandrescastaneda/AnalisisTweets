from util.clean_text import CleanText
from models.information_tweet import TweetInformation
from models.tweet_clean import TweetClean

class CleanTweets:

    def __init__(self):
        self._clean_text_util = CleanText() 

    def _load_tweets(self):
        return TweetInformation.objects
    
    def main(self):
        tweets = self._load_tweets()
        url_base = "https://twitter.com/{{screen_name}}/status/{{tweet_id}}"
        for tweet in tweets:
            url = url_base.replace("{{screen_name}}", tweet.screen_name)
            url = url.replace("{{tweet_id}}", tweet.tweet_id)
            text_clean = self._clean_text_util.get_text_clean(tweet.text_full)
            tweet_clean = TweetClean(
                tweet_id=tweet.tweet_id, 
                text_clean=text_clean,
                url_tweet=url,
                stores=tweet.stores
                )
            tweet_clean.save()

