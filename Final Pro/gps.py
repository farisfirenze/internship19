import serial
import pynmea2
import webbrowser
import os

ser = serial.Serial(port='/dev/ttyS0',baudrate=9600)

while True:
        try:
                #ser = serial.Serial(port='/dev/ttyS0',baudrate=9600)
                #msg0 = ser.readline()
                #if('CPGGA' in msg0):
                #       print(msg0)
                #       #msg = pynmea2.parse(msg0,check=False)
                msg = pynmea2.parse(ser.readline(),check=False)
                #else:
                #       continue
                #print(msg)
                #print("Latitude : "+msg.lat+"\nLongitude : "+msg.lon)
                #s = ['%s: %s' % (msg.fields[i][0], msg.data[i]) for i in range(l$
                print("Latitude : "+str(msg.latitude)+" "+msg.lat_dir)
                print("Longitutde :"+str(msg.longitude)+" "+msg.lon_dir+"\n")
                break
        except IOError and AttributeError:
                #print("Locating...\n")
                continue

#cmd = 'xdg-open \'https://maps.google.com/?='+str(msg.latitude)+','+str(msg.long$
site = "https://maps.google.com/?q="+str(msg.latitude)+","+str(msg.longitude)

webbrowser.open_new(site)
