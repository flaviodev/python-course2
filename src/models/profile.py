from mongoengine import *

class Profile(Document):
    name = StringField(required=True, max_length=200)

def __init__ (self, name):
    self.name = name
