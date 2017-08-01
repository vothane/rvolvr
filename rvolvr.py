from twython import Twython
from apscheduler.schedulers.blocking import BlockingScheduler
import api_keys

sched = BlockingScheduler()

APP_KEY = api_keys.APP_KEY
APP_SECRET = api_keys.APP_SECRET

twitter = Twython(APP_KEY, APP_SECRET)

@sched.scheduled_job('interval', minutes=11)
def revolve_avatar():
    avatar = open('myImage.png', 'rb')
    twitter.update_profile_image(image=avatar)

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=5)
def evolve_banner():
    twitter.update_profile_banner_image(banner=image)

sched.start()
