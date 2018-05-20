import serial
import wave, struct, math
ser = serial.Serial('/dev/ttyUSB0',9600,timeout=1)
ser.isOpen()

sampleRate = 38461.0 # hertz
duration = 1.0       # seconds
frequency = 440.0    # hertz

i = 0

while i < 1000:
    ser.write('Ready')
    wavef = wave.open('sound'+str(i)+'.wav','w')
    wavef.setnchannels(1)
    wavef.setsampwidth(2)
    wavef.setframerate(sampleRate)
    for i in range(int(duration * sampleRate)):
        value = ser.readLine.decode('utf-8')
        data = struct.pack('<h',value)
        wavef.writeframesraw(data)
    wavef.writeframes('')
    wavef.close()
    i++
