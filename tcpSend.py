import socket
import keyboard

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.205", 8888))

keyboard.on_press(lambda e: s.send(str(e).encode('utf-8')), suppress=True)

keyboard.wait('ctrl+c')

# while True:
# 	s.send((input("Send> ")+"\n").encode('utf-8'))