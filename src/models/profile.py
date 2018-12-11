from mongoengine import *

class Profile(Document):
    name = StringField(required=True, max_length=200)
    likes = LongField(required=False)

