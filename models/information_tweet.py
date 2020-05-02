from mongoengine import (Document,  StringField, PointField, 
                            DateTimeField, ListField)

class TweetInformation(Document):
    tweet_id = StringField(required=True)
    text_full = StringField(required=True)
    coordinates = PointField(default=None, null=True)
    created_at = DateTimeField(required=True)
    screen_name = StringField(required=True)
    stores = ListField(StringField())
