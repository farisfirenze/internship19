import Adafruit_DHT as dht
import paho.mqtt.client as mqtt

broker_address = "192.168.43.195"
client = mqtt.Client("P1")
client.connect(broker_address)
i=0
topic = input("Enter the topic : ")

while True:
        temp, humidity = dht.read_retry(dht.DHT22, 4)
        #print ("Temperature : %0.2f*C Humidity : %0.2f" %(temp, humidity))
        st_temp = str(temp)
        st_stemp = st_temp[0:5]+"*C"
        st_hum = str(humidity)
        st_shum = st_hum[0:5]+"%"
        i = i + 1
        print(str(i)+" : Temperature = "+st_stemp+" Humidity = "+st_shum)
        data = str(i)+' : Temperature = '+st_stemp+' Humidity = '+st_shum+''
        client.publish(topic,data)