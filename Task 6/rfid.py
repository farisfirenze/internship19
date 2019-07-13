import time
import serial

ser = serial.Serial(port='/dev/ttyS0',baudrate=9600)
y1 = '\x03\x0255000825067E\r\n' #first card
z1 = '\x0255000825067E\r\n'

y2 = '\x03\x02550009DF8506\r\n' #second card
z2 = '\x02550009DF8506\r\n'
while True:
        x=ser.readline()
        data = x.split(' ')
        #print(data)
        #print(type(data))
        #for i in data:
                #print(i)
                #if(str(i) == '55000825067E'):
                        #print("YOOO")
        #if(list(data) in )
        if(x == y1 or x == z1):
                print("You used your first card")
        elif(x == y2 or x == z2):
                print("You used your second card")
        #print(x.decode('UTF-8'))
ser.close()

