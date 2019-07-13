The above circuit is using hardware SPI to wire the MCP3008. I found some of these chips don’t support hardware SPI but can still use the software SPI protocol.

Here’s how to wire the chip:

Lower row:
CH0: Data from sensor

Upper row (left to right, left is the “notch” position):
VDD -> 3.3V
VREF -> 3.3V
AGND -> GND
CLK -> GPIO 18
DOUT -> GPIO 23
DIN -> GPIO 24
CS/SHDN -> GPIO 25
DGND -> GND

Afterwards do NOT install the py-spidev package but instead get the following packages using PIP:

Adafruit_GPIO
Adafruit_MCP3008

Finally use the following modified python3 code:

import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

CLK = 18
MISO = 23
MOSI = 24
CS = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

while True:

v = (mcp.read_adc(0) / 1023.0) * 3.3
dist = 16.2537 * v**4 – 129.893 * v**3 + 382.268 * v**2 – 512.611 * v + 301.439
print(“Distance {:.2f}”.format(dist))
time.sleep(0.5)