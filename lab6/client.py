# -*- coding: utf-8 -*-
import json
import random, time, threading, sys
import paho.mqtt.client as mqtt #import the client1

mqttc = mqtt.Client("client1", clean_session=False)
#broker_address="iot.eclipse.org"
mqttc.username_pw_set("jxjanbvd", "uuUlFpgEVUte")
mqttc.connect("m23.cloudmqtt.com", 10035, 60)
def on_message(client, userdata, message):
	print('message received', str(message.payload.decode('utf-8')))
	print('message topic = ', message.topic)
	print('message qos = ', message.qos)
	print('message retain flag =', message.retain)
def pub():
	mqttc.publish('sms/henry', 'tara')
	threading.Timer(1,pub).start()
def sub():
	mqttc.subscribe('sms/tara')
	threading.Timer(1,sub).start()

sub()
on_message