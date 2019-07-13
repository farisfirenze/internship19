import paho.mqtt.subscribe as mqtt #import the client1
#import time
#def on_message(client, userdata, message):
#    print("message received " ,str(message.payload.decode("utf-8")))
#    print("message topic=",message.topic)
#    print("message qos=",message.qos)
#    print("message retain flag=",message.retain)
	
#broker_address = "raspberrypi"
#broker_address="iot.eclipse.org"
#print("Creating new instance")
#client = mqtt.Client("P2") #create new instance
#print("New client instance created ...")
#client.on_message=on_message #attach function to callback
#print("connecting to broker")
#client.connect(broker_address) #connect to broker
#client.loop_start() #start the loop
#topic = input("Enter a topic to subscribe : ")
topic = input("Enter a topic to subscribe : ")
print("Subscribing to topic : ",topic)
print("Subscribed to topic : ",topic)
print("Waiting for message from client ...")
msg = mqtt.simple(topic)
print(msg.payload.decode("utf-8"))
#print("Publishing message to topic","mytopic")
#client.publish("mytopic","OFF")
#client.publish("mytopic","message received from : Windows PC")
#time.sleep(4) # wait
#client.loop_stop() #stop the loop