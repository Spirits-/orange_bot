from bot import IRC
import os
import random
import time

## IRC Config
server = "10.0.0.2"
port = 6667
channel = "#talk"
irc = IRC("ORANGE_BOT")
irc.connect(server, port)
i = 0
while True:
    print(i)
    time.sleep(0.5)
    resp = irc.get_response()
    if resp.find("Hello"):
        irc.sendMessage("#talk", "Hello World!")
    i += 1