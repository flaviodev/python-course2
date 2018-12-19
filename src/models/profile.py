from mongoengine import *

class Profile(Document):
    name = StringField(required=True, max_length=200)
    __likes = LongField(default=0)

    def get_likes(self):
        return self.__likes

    def like(self):
        self.__likes += 1
        self.save()

    def get_credits(self):
        return self.__likes * 10.0