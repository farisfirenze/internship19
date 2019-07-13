import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
pin_to_circuit = 7

#initialising MQTT
client = mqtt.Client("P1")
client.connect("192.168.43.195")


def rc_time (pin_to_circuit):
        count = 0
        #Output on the pin for
        GPIO.setup(pin_to_circuit, GPIO.OUT)
        GPIO.output(pin_to_circuit, GPIO.LOW)
		time.sleep(0.5)

        #Change the pin back to input
        GPIO.setup(pin_to_circuit, GPIO.IN)
        #Count until the pin goes high
        while (GPIO.input(pin_to_circuit) == GPIO.LOW):
                count += 1

        return count

#Catch when script is interupted, cleanup correctly
try:
        # Main loop
        while True:
                print(rc_time(pin_to_circuit))
                client.publish("datas",rc_time(pin_to_circuit))
except KeyboardInterrupt:
        pass
finally:
        GPIO.cleanup()
        client.disconnect()
