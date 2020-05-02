from mongoengine import StringField, Document
#Cuentas de twitter que se usaran
class AccountTwitter(Document):
    account = StringField(required=True)
    name = StringField()