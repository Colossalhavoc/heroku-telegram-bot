# -*- coding: utf-8 -*-
import redis
import os
import telebot
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['1166420817:AAEJc-vAL6nxvvFj0YNNl62iI5s2xZwBgkI']
#some_api_token = os.environ['SOME_API_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
#r = redis.from_url(os.environ.get("REDIS_URL"))

#       Your bot code below
  bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...
