from mongoengine import Document, StringField

class query_search(Document):
    query = StringField(required=True)
