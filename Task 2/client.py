import paho.mqtt.client as mqtt #import the client1
import time
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
	
broker_address = "192.168.43.195"
#broker_address="iot.eclipse.org"
print("Creating new instance")
client = mqtt.Client("P1") #create new instance
print("New client instance created ...")
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
#print("Subscribing to topic","mytopic")
#client.subscribe("house/bulbs/bulb1")
topic = input("Enter a topic to publish : ")
print("Publishing message to topic : ",topic)
client.publish(topic,"SAMPLE MESSAGE, message received from : Laptop")
time.sleep(4) # wait
client.loop_stop() #stop the loop
#def on_publish(client,userdata,result):             #create function for callback
#    print("data published \n")
#    pass
#client1= paho.Client("control1")                           #create client object
#client1.on_publish = on_publish                          #assign function to callback
#client1.connect(broker,port)                                 #establish connection
#ret= client1.publish("house/bulb1","on")

#def on_disconnect(client, userdata, rc):
#   print("client disconnected ok")
#client1.on_disconnect = on_disconnect
#client1.disconnect()