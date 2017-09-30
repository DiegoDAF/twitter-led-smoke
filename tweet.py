import tweepy
import time
import datetime
import RPi.GPIO as GPIO

ACCESS_KEY = 'your-access-key'
ACCESS_SECRET = 'access-secret'
CONSUMER_KEY = 'consumer-key'
CONSUMER_SECRET = 'cosumer-secret'

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.output(25, GPIO.LOW)
old = "a"
search_text = "#ekofigus"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
while True:
  search_result = api.search(search_text, rpp=1, count=1)
  for i in search_result:
        if i.text == old:
            print "repetido"
        else:
            print i.text
            GPIO.output(25, GPIO.HIGH)
            time.sleep(4)
            GPIO.output(25, GPIO.LOW)
            old = i.text
  time.sleep(10)
GPIO.cleanup()
