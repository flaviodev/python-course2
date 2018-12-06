#exec mongod & > /var/lib/mongodb/mongo.log 2>&1
setsid mongod >/dev/null 2>&1 < /dev/null &


python main.py