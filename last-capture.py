# -*- coding: utf-8 -*-

from random import randint, choice
from time import sleep
from datetime import datetime, timedelta
import humanize
from perma_times import get_objects
from screen_api_client import go


url = "https://<your domain>/new_event"
room = "<your room>"
token = "<your token>"

headers = {"Authorization": "Token %s" % token}


while True:
    try:
        objects = get_objects(20,0)
        for object in objects:
            if object[-2] is not None:
                domain = object[0].split("//")[-1].split("/")[0]
                last = object[-2]
                p = u"∞ Last Perma capture, of {1}, was {0}.".format(
                    humanize.naturaltime(datetime.now() - timedelta(seconds=last)), domain)
                go(url, room, headers, p)
                break
    except:
        pass
    sleep(60)
