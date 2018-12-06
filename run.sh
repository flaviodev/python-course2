#!/bin/bash

app_path=`pwd`

docker rm flaviodev-python -f
docker run -it --name flaviodev-python -v $app_path/src:/usr/src:rw -v $app_path/data:/data:rw flaviodev-python sh
