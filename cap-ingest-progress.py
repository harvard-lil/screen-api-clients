# -*- coding: utf-8 -*-

from random import randint, choice
from time import sleep
from datetime import datetime, timedelta
import humanize
import subprocess
from screen_api_client import go


url = "https://<your domain>/new_event"
room = "<your room>"
token = "<your token>"

headers = {"Authorization": "Token %s" % token}

last = None
deltas = []
maxdeltas = 10

while True:
    volumes = len(subprocess.check_output("redis-cli -n 1 keys \*", shell=True).split())
    p = "🎓 %s keys to go in CAP ingest" % humanize.intcomma(volumes)
    if last:
        deltas.append(last - volumes)
        if len(deltas) > maxdeltas:
            deltas = deltas[-maxdeltas:]
        p += "\n(%.1f per minute over the last %s)" % (sum(deltas) / float(len(deltas)), "minute" if len(deltas) == 1 else humanize.naturaldelta(timedelta(seconds=60*len(deltas))))
    last = volumes
    go(url, room, headers, p)
    sleep(60)
