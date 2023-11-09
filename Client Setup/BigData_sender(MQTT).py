import paho.mqtt.client as mqtt
import serial
import time


# Define your MQTT broker address and port
broker_address = "172.21.5.138"
broker_port = 1883

# Define the topic to which you want to publish
topic = "Pi MQTT server"

# Callback function when a message is published
def on_publish(client, userdata, mid):
    print(f"Message published with message ID: {mid}")

# Create an MQTT client
client = mqtt.Client("MyClient")

# Set the callback function for when the client connects
client.on_publish = on_publish

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Start the MQTT client loop to handle communication
client.loop_start()


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
                
                message = "Temperature: " + str(temperature_celsius)
                qos = 1
                client.publish(topic, message, qos)
                
                print(f"Published: {message} to topic {topic}")
                
        time.sleep(2)
        
        
except KeyboardInterrupt:
    arduino.close()
    
# Disconnect from the MQTT broker
client.disconnect()



