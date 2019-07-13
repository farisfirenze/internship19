import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import paho.mqtt.client as mqtt
from scipy.io import wavfile
import pynmea2
import os

#MQTT
client = mqtt.Client("P1")
topic = "/PI/MSG"
addrB = "192.168.1.171"
addrC = ""
addrD = ""
def clientConnect(addr,topicName,msg):
        client.connect(addr)
        client.publish(topicName,msg)
        client.disconnect()

#Socket
servAddress = "192.168.1.171"

print("Streaming live..")
os.system("sudo motion service start")

#GPS
serPort = serial.Serial("/dev/ttyS0", baudrate=9600)

#VoiceAnalysis
bsAmp = 3000 #BaseAmplitude

#Comands
recordCmd = 'arecord -D plughw:2,0 -d 5 --format=S16_LE test.wav'
cameraCmd = "fswebcam image.jpg"

#IRSensor
CLK = 18
MISO = 23
MOSI = 24
CS = 25
dist = 30#cm
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
local = [999]*5
count = 0
flag = False

while True:
        try:
                gpsData = pynmea2.parse(serPort.readline(), check=False)
                print local
                for i in range(0,5):
                        v = (mcp.read_adc(0) / 1023.0) * 3.3
                        d = 16.2537*v**4 - 129.893*v**3 + 382.268*v**2 - 512.611*v + 301.439
                        local[i] = d
						time.sleep(0.4)
                        print local
                        if(local[i] < dist):
                                count = count + 1
                                if(count == 5):
                                        flag = True
                                        local = [999]*5
                                        count = 0
                if(d < dist and flag == True):
                        flag = False
                        print("Object closer for 2 seconds.. Recording...")
                        os.system(recordCmd)
                        print("Audio Recorded.. \nAudio analysis in progress...")
                        samplerate, data = wavfile.read('test.wav')
                        print(max(data))
                        print("Audio analysis successfull..")
                        if(max(data) > bsAmp):
                                clientConnect(addrB,"/PI/Switch","Wait")
                                msgType = "X"
                                os.system("sudo killall motion")
								time.sleep(1)
                                os.system(cameraCmd)
                                print("sending captured image...")
                                os.system("sudo python client.py")
                                print("Image sent..")
                                os.system("sudo motion sevice start")
                        else:
                                clientConnect(addrB,"/PI/Switch","nWait")
                                msgType = "Y"
                        msgLat = str(gpsData.latitude)
						msgLon = str(gpsData.longitude)
                        finalMsg = "[ "+servAddress+", "+"("+msgLat+", "+msgLon+")"+", "+msgType+" ]"
                        clientConnect(addrB,topic,finalMsg)
                        clientConnect(addrC,topic,finalMsg)
                        clientConnect(addrD,topic,finalMsg)
                        time.sleep(1)
                local = [999]*5

        except IOError and AttributeError:
                continue