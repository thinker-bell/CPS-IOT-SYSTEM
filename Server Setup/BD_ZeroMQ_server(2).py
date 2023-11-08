import zmq


context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.bind("tcp://172.21.5.138:5555")

socket.setsockopt_string(zmq.SUBSCRIBE, '')

print("ZMQ Socket (5555) is now listening...\n")

while(True):
     message = socket.recv().decode("utf-8")

     if message:
         print(f"Recieved {message}")
     else:
         print("No message recieved")


