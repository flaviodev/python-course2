from mongoengine import *
from models.profile import Profile

class VipProfile(Profile):

    def to_string(self):
        return '{} ({} likes - Credits $ {})'.format(self.get_name(),self.get_likes(), self.get_credits())

    def get_credits(self):
        return self.get_likes() * 10.0