'''
    Raspberry Pi end of Smart System
'''
import serial
ser = serial.Serial('/dev/ttyAMA0',9600,timeout=1)
ser.isOpen()

while True:
    try:
        message = ser.readline()
        print(message)
    except KeyboardInterrupt:
        ser.close()
