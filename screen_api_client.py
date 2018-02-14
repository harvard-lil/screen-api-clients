import requests


def go(url, room, headers, p, breaks=True):
    payload = { "message": p, "room_name": room }
    if breaks:
        r = requests.post(url, headers=headers, json={ "message": "\n\n", "room_name": room })
    r = requests.post(url, headers=headers, json=payload)
