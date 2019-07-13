import paho.mqtt.subscribe as mqtt
import paho.mqtt.client as mqttc
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))

msg = mqtt.simple("datas")
client = mqttc.Client("P5")
client.connect("192.168.43.196")

while True:
	client.on_message=on_message
	if(client.on_message):
		print(msg.payload.decode("utf-8"))