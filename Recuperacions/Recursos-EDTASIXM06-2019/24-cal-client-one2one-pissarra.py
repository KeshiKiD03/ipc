# /usr/bin/python3
#-*- coding: utf-8-*-
# cal-client-one2oned-pissarra.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys,socket,argparse
parser = argparse.ArgumentParser(description="""CAL server""")
parser.add_argument("-s","--server",type=str, default='')
parser.add_argument("-p","--port",type=int, default=50001)
args=parser.parse_args()
HOST = args.server
PORT = args.port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
  data = s.recv(1024)
  if not data: break
  print('Data:', str(data))
s.close()
sys.exit(0)


