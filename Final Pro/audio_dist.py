import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import paho.mqtt.client as mqtt
import os

addr = "192.168.43.196"
pas = 'raspberry'
i = 0
client = mqtt.Client("P1")
client.connect(addr)
cmd_rec = 'arecord -D plughw:1,0 -d 5 test.wav'
cmd_send = 'sshpass -p '+pas+' scp test.wav pi@'+addr+':FTP/'

local = []
count = 0

CLK = 18
MISO = 23
MOSI = 24
CS = 25

mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

while True:
        v = (mcp.read_adc(0) / 1023.0) * 3.3
		d = 16.2537*v**4 - 129.893*v**3 + 382.268*v**2 - 512.611*v + 301.439
        print("Distance : {0:0.2f}cm".format(d))
		local[i] = d
		i = i + 1
        for k in range(0,100):
			if(local[k] < 20):
				count = count + 1
				if(count > 50):
					os.system(cmd_rec)
					os.system(cmd_send)
					count = 0
					i = 0
					local = []
			else:
				continue
		#temp_d = str(d)
        #data = temp_d[0:5] + "cm"
        #client.publish("datas",data)
        #time.sleep(0.5)
		

	


	
	