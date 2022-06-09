# /usr/bin/python3
#-*- coding: utf-8-*-
#
# exemple-echoClient.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys,socket
HOST = ''
PORT = 50001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn, addr = s.accept()
print("Connected by", addr)
while True:
  data = conn.recv(1024)
  if not data: break
  conn.send(data)
conn.close()
sys.exit(0)


