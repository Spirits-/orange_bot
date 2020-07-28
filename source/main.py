from bot import IRC
import os
import random
import time

## IRC Config
server = "10.0.0.2" # Provide a valid server IP/Hostname
port = 6667
channel = "#talk"
irc = IRC("ORANGE_BOT")
irc.connect(server, port)
irc.joinChannel("#talk")
i = 0
while True:
    time.sleep(0.5)
    irc.joinChannel("#talk")
    #irc.get_response()
    irc.sendMessage("#talk", "Hello World!")
    i += 1
    print(i)