'''
    Raspberry Pi end of Smart System
'''
import serial
ser = serial.Serial('dev/ttyAMA0',9600,timeout=1)
ser.open()

while true:
    message = ser.readline()
    print message
    except KeyboardInterrupt:
        ser.close()
