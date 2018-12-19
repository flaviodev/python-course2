from mongoengine import *

class Profile(Document):
    meta = {'allow_inheritance': True}
    __name = StringField(name='name', required=True, max_length=200)
    __likes = LongField(name='likes', default=0)

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_likes(self):
        return self.__likes

    def set_likes(self, likes):
        self.__likes = likes

    def like(self):
        self.__likes += 1
        self.save()

    def to_string(self):
        return '{} ({} likes)'.format(self.__name,self.__likes)
