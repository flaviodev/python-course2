FROM python

RUN python -m pip install pymongo

RUN python -m pip install mongoengine

WORKDIR /usr/src

CMD ["bash"]