import serial
import time
import smbus
import sys
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect('tcp://172.21.5.138:5555')

print('Established serial connection to Arduino')

print('Program started')
arduino = serial.Serial('/dev/ttyACM0', 9600)

try:
    while True:

        arduino_data = arduino.readline()

        decoded_values = arduino_data.decode().strip()

        if "Temperature:" in decoded_values:
            parts = decoded_values.split(" ")
            if len(parts) >= 2:
                
                temperature_celsius = float(parts[1])

                print(f"Temperature: {temperature_celsius}\u00B0C")
                
                # Send a message to the server
                message = "Temperature: {"+str(temperature_celsius)+"}"
                bm = message.encode("utf-8")
                socket.send(bm)

        
        time.sleep(2)
        
        
except KeyboardInterrupt:
    arduino.close()

# Close the socket and the ZeroMQ context
socket.close()
context.term()
