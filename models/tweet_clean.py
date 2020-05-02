from mongoengine import (
                        Document, 
                        StringField, 
                        BooleanField,
                        ListField
                        )

class TweetClean(Document):
    tweet_id = StringField(required=True)
    text_clean = StringField(required=True)
    complaint = BooleanField(default=False)
    url_tweet = StringField(required=True)
    stores = ListField(StringField())