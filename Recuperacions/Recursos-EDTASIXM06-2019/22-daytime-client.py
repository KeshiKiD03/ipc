# /usr/bin/python
#-*- coding: utf-8-*-
#
# daytime-client.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys,socket
HOST = ''
#HOST="35.176.221.122"  # AWS EC2
PORT = 50001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
  data = s.recv(1024)
  if not data: break
  print('Data:', repr(data))
s.close()
sys.exit(0)


