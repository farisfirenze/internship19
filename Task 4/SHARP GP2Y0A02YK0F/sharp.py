import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import paho.mqtt.client as mqtt

addr = "192.168.43.196"

client = mqtt.Client("P1")
client.connect(addr)

CLK = 18
MISO = 23
MOSI = 24
CS = 25

mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

while True:
	v = (mcp.read_adc(0) / 1023.0) * 3.3
	d = 16.2537*v**4 - 129.893*v**3 + 382.268*v**2 - 512.611*v + 301.439
	print("Distance : {0:0.2f}cm".format(d))
	temp_d = str(d)
	data = temp_d[0:5] + "cm"
	client.publish("datas",data)
	time.sleep(0.5)