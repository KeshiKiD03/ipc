# /usr/bin/python
#-*- coding: utf-8-*-
#
# daytime-server.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys,socket
from subprocess import Popen, PIPE
HOST = ''
PORT = 50001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(1)
conn, addr = s.accept()
print("Connected by", addr)
command = ["date"]
pipeData = Popen(command,stdout=PIPE)
for line in pipeData.stdout:
  conn.send(line)
conn.close()
sys.exit(0)


