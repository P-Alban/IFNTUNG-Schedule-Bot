import os

import pytz
import redis
from mixpanel import Mixpanel

TIMEOUT = 10000
CACHE_TIME = 3600 * 10  # 10 hours
TIME_ZONE = pytz.timezone('Europe/Kiev')
default_encoding = 'windows-1251'
url = 'http://194.44.112.6/cgi-bin/timetable.cgi?n=700'
timestamp_length = 12
days = {'Сьогодні': 0, 'Завтра': 1}
requests_limit_per_day = 25
throttle_time = 2
mp = Mixpanel(os.environ.get('MIX_TOKEN'))
r = redis.from_url(os.environ.get('REDIS_URL'))
flag_message = 'Військова підготовка'
default_time_set = ['6:00', '6:15', '6:30', '6:45', '7:00', '7:15', '7:30', '7:45', '8:00']
