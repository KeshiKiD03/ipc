# /usr/bin/python3
#-*- coding: utf-8-*-
#
# 25-ps-server-one2one.py [-p port]
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
# 26-telnet-client.py -p port -s server
# 26-telnetServer.py [-p port] [-d debug]
# Implementar un servidor i un client telnet. Client i server fan un diàleg.
# Cal un senyal de “yatà” Usem chr(4).
# Si s’indica debug el server genera per stdout la traça de cada connexió.

import sys,socket, os
from subprocess import Popen, PIPE
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", type=int, dest="port", metavar="port",
                     help="numero depuerto en el que escucha el server",
                     default=50001)
parser.add_argument("-d", "--debug", action="store_true",
                     help="generar traza de conexion")
args=parser.parse_args()
HOST = ''
PORT = args.port
MYEOF = bytes(chr(4), 'utf-8')
DEBUG = args.debug
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(1)
while True:
    conn, addr = s.accept()
    print("Connected by", addr)
    while True:
        data = conn.recv(1024)
        print('Recive', repr(data))
        if not data: break                
        pipeData = Popen(data, stdout=PIPE, stderr=PIPE, shell=True)
        for line in pipeData.stdout:
            conn.sendall(line)
            if DEBUG: sys.stderr.write(str(line,'utf-8'))
        for line in pipeData.stderr:
            conn.sendall(line)
            if DEBUG: sys.stderr.write(str(line,'utf-8'))        
        conn.sendall(MYEOF)
        
    conn.close()
s.close()
sys.exit(0)

