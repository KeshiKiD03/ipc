#!/bin/bash
# --------------------------------------
import sys,socket,os,signal,argparse, time
from subprocess import Popen, PIPE
# --------------------------------------
parser = argparse.ArgumentParser(description="""Get Server""")

parser.add_argument("port", type=int)

args=parser.parse_args()
# --------------------------------------
HOST = ''
PORT = args.port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(1)
# -------------------------------------    
while True:
    conn, addr = s.accept()
    print("Connected by", addr)
    data = conn.recv(1024)
    pipeData = Popen(data,shell=True,stdout=PIPE)
    if not data:      
        break
    for line in pipeData.stdout:
        conn.send(line)
    conn.send(b'\x04')

sys.exit(0) 
