import socket
import time


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('172.21.5.138', 1883)
    server_socket.bind(server_address)
    server_socket.listen(1)
    print("MQTT Server (1883) is listening...")

    while True:
        client_socket, client_address = server_socket.accept()
        now = time.ctime()
        
        print("Connected by:" + str(client_address) + " " + str(now))     
        
        client_socket.close()
 
if __name__ == "__main__":
     start_server()
    
