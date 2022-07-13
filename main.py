import random
from time import sleep
from ga4mp import Ga4mp
import os


MEASUREMENT_ID = os.environ["MEASUREMENT_ID"]
API_SECRET = os.environ["API_SECRET"]

ga = Ga4mp(measurement_id = MEASUREMENT_ID, api_secret = API_SECRET, client_id="test_id")

ratio = 29.5
event_type = 'usd_uah'

for i in range(20):
    event_parameters = {'ratio': f'{ratio:.2f}'}

    event = {'name': event_type, 'params': event_parameters }
    events = [event]
    ga.send(events)

    ratio = ratio + random.random() /10 * random.choice([-1, 1])
    sleep(1)