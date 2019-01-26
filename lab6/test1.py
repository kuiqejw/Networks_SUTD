#!/usr/bin/env python
# 50.012 Lab 9
import paho.mqtt.client as mqtt

import cmd
import sys
import time
import select

username = "laura_ong"
broker = "test.mosquitto.org"
port = 1883
dchannels = ['user/'+username, 'hello/sutd', 'hey/there']

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    if rc==mqtt.MQTT_ERR_SUCCESS:
        print("Connected successfully to %s"%broker)
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    for dc in dchannels:
        print("Subscribing to channel %s"%dc)
        client.subscribe(dc,qos=1)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Message received on topic: %s, using QoS %s\nMessage: %s"%(msg.topic,str(msg.qos),str(msg.payload)))

class cli(cmd.Cmd):
    """Simple MQTT chat client."""

    client = None
    looping = True
    def do_subscribe(self, topic):
        print("Subscribing to channel %s"%topic)
        client.subscribe(topic,qos=1)

    def do_unsubscribe(self, topic):
        print("Unsubscribing from channel %s"%topic)
        client.unsubscribe(topic)

    def do_msg(self, channel):
        if not channel:
            print("Please enter a channel to send to.")
            return
        message = raw_input("Enter your message: ")
        print("Sending %s to %s"%(message,channel))
        client.publish(channel, payload=message, qos=1)

    def do_quit(self, line):
        print("Goodbye!")
        exit(0)

if __name__ == '__main__':

    client = mqtt.Client(client_id=username, clean_session=False)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker, port, 60)
    time.sleep(1)

    cli.client=client

    print("Welcome to the MQTT client CLI. Type 'help' or 'msg <channel>'")
    # If there's input ready, do something, else do something
    # else. Note timeout is zero so select won't block at all.
    while True:
            while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                    line = sys.stdin.readline()
                    if line:
                            cli().onecmd(line)
                    else: # an empty line means stdin has been closed
                            print('eof')
                            exit(0)
            else:
                    client.loop(1)
