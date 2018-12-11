from mongoengine import *

class Profile(Document):
    name = StringField(required=True, max_length=200)
    __likes = LongField(default=0)

    def get_likes(sefl):
        return sefl.__likes
