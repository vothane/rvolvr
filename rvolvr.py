import os
from twython import Twython
from queuelib import FifoDiskQueue
from apscheduler.schedulers.blocking import BlockingScheduler
import api_keys

sched = BlockingScheduler()

APP_KEY = api_keys.APP_KEY
APP_SECRET = api_keys.APP_SECRET
OAUTH_TOKEN = api_keys.OAUTH_TOKEN
OAUTH_TOKEN_SECRET = api_keys.OAUTH_TOKEN_SECRET

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

selfies = ['1.png', '2.png', '3.png']

q = FifoDiskQueue("queuefile")

if len(q) == 0:
    for selfie in selfies:
        q.push(selfie)

selfie = q.pop()
q.close()

@sched.scheduled_job('interval', minutes=10)
def revolve_avatar():
    avatar = open("selfies/"+selfie, 'rb')
    twitter.update_profile_image(image=avatar)

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=5)
def evolve_banner():
    twitter.update_profile_banner_image(banner=image)

sched.start()
