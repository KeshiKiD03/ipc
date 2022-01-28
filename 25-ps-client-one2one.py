# /usr/bin/python3
#-*- coding: utf-8-*-
# cal-client-one2oned-pissarra.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket,argparse
from subprocess import Popen, PIPE

parser = argparse.ArgumentParser(description="""PS Client""")
parser.add_argument("-p","--port",type=int, default=50001)
parser.add_argument("server",type=str) # Se conecta cualquiera
args=parser.parse_args()
HOST = args.server
PORT = args.port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Abre el SOCKET TCP
s.connect((HOST, PORT)) # Se conecta

command = "ps ax" # Le pasamos el comando PS AX
pipeData = Popen(command, shell=True, stdout=PIPE)
for line in pipeData.stdout: # Recorre el tubo
	s.send(line) # Recoge el tubo
	
s.close()
sys.exit(0)

