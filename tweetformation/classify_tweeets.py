from models.tweet_clean import TweetClean
from services.ibm_service import IbmService

class ClassifyTweet:

    def __init__(self):
        self.ibm_service = IbmService()

    def _load_tweets(self):
        return TweetClean.objects

    def main(self):
        tweets_clean = self._load_tweets()

        for tweet_clean in tweets_clean:
            intent = self.ibm_service.get_intent(tweet_clean.text_clean)
            if intent:
                confidence = float(intent.get("confidence"))
                if confidence >= 0.92:
                    tweet_clean.complaint = True
                    tweet_clean.save()
