import socket
import sys
import time
import re

class IRC:
 
    irc = socket.socket()
  
    def __init__(self, username):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        IRC.username = username
        IRC.currentChannel = None
 
    def sendMessage(self, channel, msg):
        message = "PRIVMSG " + channel + " " + msg + "\n"
        print("SEND >>" + message)
        self.irc.send(bytes(message, "UTF-8"))

    def connect(self, server, port, password = ""):
        print("Connecting to: " + server)
        self.irc.connect((server, port))
        time.sleep(3)
        # Authentication
        if password != "":
            self.irc.send(bytes("PASS " + password, "UTF-8"))

        self.irc.send(bytes("NICK " + self.username + "\n", "UTF-8"))
        self.irc.send(bytes("USER " + self.username + " OrangeHostname" + " 10.0.0.2" + " :MIGHTY ORANGE", "UTF-8"))
        time.sleep(5)

    def joinChannel(self, channel):
        self.irc.send(bytes("JOIN " + channel + "\n", "UTF-8"))
        self.currentChannel = channel

    def get_response(self):
        time.sleep(1)
        pingRegex = re.compile(r"^PING :(.*)", re.M)
        resp = self.irc.recv(2040).decode("UTF-8")
        print("RCV >>" + resp)
        if pingRegex.search(resp):
            mo = pingRegex.search(resp)
            print("Responding to PING")
            self.irc.send(bytes("PONG " + mo.group(1) + '\r\n', "UTF-8")) 
        return resp