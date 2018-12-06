import routes.main_route
from mongoengine import *

connect('mongoengine_test', host='db', port=27017)

routes.main_route.run()
