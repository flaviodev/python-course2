from mongoengine import *

class Profile(Document):
    __name = StringField(name='name', required=True, max_length=200)
    __likes = LongField(name='likes', default=0)
    __vip = BooleanField(name = 'vip', default=False)

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_likes(self):
        return self.__likes

    def is_vip(self):
        return self.__vip

    def set_vip(self, vip):
        self.__vip = vip

    def like(self):
        self.__likes += 1
        self.save()

    def get_credits(self):
        return self.__likes * 10.0 if self.__vip else 0.0