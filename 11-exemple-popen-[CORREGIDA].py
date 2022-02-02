# /usr/bin/python3
#-*- coding: utf-8-*-
#
# exemple-popen.py ruta
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys, argparse # Importa librerías
from subprocess import Popen, PIPE # Filtra que de la librería de "subprocess", me importa el Popen y el PIPE

parser = argparse.ArgumentParser(description=\
        """Exemple popen""")

parser.add_argument("ruta",type=str,\
        help="directori a llistar")

args=parser.parse_args()
# -------------------------------------------------------
command = ["ls", args.ruta]     # El primer argument serà 'ls', el segon, la ruta
#command = ["who"]
pipeData = Popen(command, stdout=PIPE)      # Crea un tub (popen --> permet construir pipes (constructor)), a l'altre extrem, executa 'ls' de l'argument que li hem passat, 'stdout=PIPE' vol dir que 'stdout' del command, ha d'enviar-ho al tub (pipe)

for line in pipeData.stdout:    # Llegeix cada línea dins del stdout del 'pipe' i la printa
    print(line.decode("utf-8"), end="")

exit(0)


"""

## NOMBRE DEL PROGRAMA + SINTAXIS

#### IPC: Pipes / Subprocess / Popen

**11-exemple-popen.py dir**

  Crear un programa que executa un ls de un argument rebut i 
  mostra per stdout el que rep del popen. Utilitza subprocess.Popen.

# ----------------------------------------------

## Explicación

#### IPC: Pipes / Subprocess / Popen

**11-exemple-popen.py dir**

  Crear un programa que executa un ls de un argument rebut i 
  mostra per stdout el que rep del popen. Utilitza subprocess.Popen.
  
  
############## TEORIA POPEN CONSTRUCTOR #############################

* Abre una "tubería" o "pipe" del comando "cmd".

* Retorna un valor que es un "open file object" conectado al tubo. 

	* Puede ser en modo
	
		* Read 'r'
		
		* Write 'w'

* El "buffering" argument tiene la misma explicación quue la función "open()".

	* Retorna "file object" --> Modo write o read STRINGS QUE BYTES.
	
* El método "close()" retorna None, si el subproceso sale "success".

# ----------------------------------------------

## Metodología y apuntes


########################## IPC ##########################

18.01.22 - IPC 1a Clase

IPC - Inter Process Communication

* Los procesos se pueden compartir en "Shared Memory".

* Pipes

	* Un proceso ejecuta otro proceso y se comunican entre ellos.
	
* Signals

	* Sigterm // Sigkill // Sighub (Reload) // Sigstop (Ctrl + Z)
	
* Sockets

	* Se comuniquen entre ellos.


################################################################


################ PROCESOS ######################################


ps --> ps

pstree --> Arbol de procesos

sudo systemctl start httpd

sleep 999999 &

pgrep sleep --> Dice todos los sleeps

jobs --> Todos los trabajos en segundo plano

fg %1 --> Pasa un proceso en primer plano

CTRL + Z --> Ha aturado el proceso, está en segundo plano pero aturado.

bg %1 --> Se ejecuta en segundo plano. En un estado de aturado.

killall sleep --> Mata todos los procesos sleep.

lsof --> Lsopenfils, dice todos los ficheros que están abiertos en el Sistema de Ficheros.

lsof | wc -l

lsof -i




################## PIPES #######################################


| 🔥PIPES❗🔥 | = TUBOS

* # ordre | ordre2

Contenido de la primera pasa a la 2da


isx36579183@i11:/tmp/m01$ grep "10" /etc/passwd | wc -l
15
isx36579183@i11:/tmp/m01$ 


##################################################################









##################################################################

ls /proc --> Representació virtual de los procesos

df -h

mount | grep /proc

isx36579183@i11:/tmp/m01$ mount | grep /proc
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
systemd-1 on /proc/sys/fs/binfmt_misc type autofs (rw,relatime,fd=29,pgrp=1,timeout=0,minproto=5,maxproto=5,direct,pipe_ino=11633)
nfsd on /proc/fs/nfsd type nfsd (rw,relatime)
isx36579183@i11:/tmp/m01$ 





  10113 pts/1    S+     0:00 cat


 
 
 isx36579183@i11:/tmp/m01$ ls /proc/10113/
arch_status  coredump_filter     gid_map    mounts         pagemap      setgroups     task
attr         cpu_resctrl_groups  io         mountstats     patch_state  smaps         timens_offsets
autogroup    cpuset              limits     net            personality  smaps_rollup  timers
auxv         cwd                 loginuid   ns             projid_map   stack         timerslack_ns
cgroup       environ             map_files  numa_maps      root         stat          uid_map
clear_refs   exe                 maps       oom_adj        sched        statm         wchan
cmdline      fd                  mem        oom_score      schedstat    status
comm         fdinfo              mountinfo  oom_score_adj  sessionid    syscall
isx36579183@i11:/tmp/m01$ 


 
 
 
 ##################################################################
 
 
 
 
 
 
 ##################################################################

# cmdline --> Contiene la línea de ordenes.

# environ --> Hereda las variables de entorno. Todo lo que se hace un EXPORT. Si fuesemos a parar a un subshell.

# stat

isx36579183@i11:/tmp/m01$ cat /proc/10113/stat
10113 (cat) S 9379 10113 9379 34817 10113 4194304 119 0 0 0 0 0 0 0 20 0 1 0 287494 5570560 141 18446744073709551615 94296076836864 94296076854953 140732828800944 0 0 0 0 0 0 0 0 0 17 6 0 0 0 0 0 94296076872784 94296076874368 94296110166016 140732828804307 140732828804311 140732828804311 140732828807147 0
isx36579183@i11:/tmp/m01$ 

# net --> Toda la información relacionada con Redes

isx36579183@i11:/tmp/m01$ ls /proc/10113/net
anycast6      if_inet6            ip_mr_vif          nf_conntrack         rpc           tcp
arp           igmp                ip_tables_matches  nf_conntrack_expect  rt6_stats     tcp6
connector     igmp6               ip_tables_names    nfsfs                rt_acct       udp
dev           ip6_flowlabel       ip_tables_targets  packet               rt_cache      udp6
dev_mcast     ip6_mr_cache        ipv6_route         protocols            snmp          udplite
dev_snmp6     ip6_mr_vif          mcfilter           psched               snmp6         udplite6
fib_trie      ip6_tables_matches  mcfilter6          ptype                sockstat      unix
fib_triestat  ip6_tables_names    netfilter          raw                  sockstat6     wireless
icmp          ip6_tables_targets  netlink            raw6                 softnet_stat  xfrm_stat
icmp6         ip_mr_cache         netstat            route                stat


# fd --> File descriptor --> Todo fichero que se abre tiene un número que le identifica

isx36579183@i11:/tmp/m01$ ls -l /proc/10113/fd
total 0
lrwx------ 1 isx36579183 hisx2 64 Jan 18 10:42 0 -> /dev/pts/1
l-wx------ 1 isx36579183 hisx2 64 Jan 18 10:42 1 -> /tmp/m01/nom.txt
lrwx------ 1 isx36579183 hisx2 64 Jan 18 10:42 2 -> /dev/pts/1
isx36579183@i11:/tmp/m01$ 

* Es un description que para a un fichero.

0 --> Entrada estandar

1 --> Salida estandar.

2 --> Salida de error.

* La salida estandar, no está en la terminal --> /dev/pst/1

* La orden CAT redirige /tmp/m01/nom.txt

/dev/pts/1 --> Es la consola
 
 
 ##################################################################
 
 
 
 ##################################################################
 
 
 
 
 
isx36579183@i11:/tmp/m01$ cd /proc/10692/
isx36579183@i11:/proc/10692$ ls -l fd
total 0
lrwx------ 1 isx36579183 hisx2 64 Jan 18 11:24 0 -> /dev/pts/0
l-wx------ 1 isx36579183 hisx2 64 Jan 18 11:24 1 -> 'pipe:[173627]'
lrwx------ 1 isx36579183 hisx2 64 Jan 18 11:24 2 -> /dev/pts/0
isx36579183@i11:/proc/10692$ 


ls - l /proc/

# El sort viene de un cat --> Pipe

# Modifica y muestra.

```
isx36579183@i11:/proc/10692$ ls -l fd
total 0
lrwx------ 1 isx36579183 hisx2 64 Jan 18 11:24 0 -> /dev/pts/0
l-wx------ 1 isx36579183 hisx2 64 Jan 18 11:24 1 -> 'pipe:[173627]'
lrwx------ 1 isx36579183 hisx2 64 Jan 18 11:24 2 -> /dev/pts/0
isx36579183@i11:/proc/10692$ cd /proc/10693/
isx36579183@i11:/proc/10693$ ls -l fd
total 0
lr-x------ 1 isx36579183 hisx2 64 Jan 18 11:25 0 -> 'pipe:[173627]'
l-wx------ 1 isx36579183 hisx2 64 Jan 18 11:25 1 -> 'pipe:[173629]'
lrwx------ 1 isx36579183 hisx2 64 Jan 18 11:25 2 -> /dev/pts/0
isx36579183@i11:/proc/10693$ cd /proc/10694/
isx36579183@i11:/proc/10694$ ls -l fd
total 0
lr-x------ 1 isx36579183 hisx2 64 Jan 18 11:25 0 -> 'pipe:[173629]'
l-wx------ 1 isx36579183 hisx2 64 Jan 18 11:25 1 -> /tmp/m01/carta.txt
lrwx------ 1 isx36579183 hisx2 64 Jan 18 11:25 2 -> /dev/pts/0
isx36579183@i11:/proc/10694$ 


```









##################################################################
 
 
mkfifo /tmp/dades

ls -l /tmp/dades

tail -f /tmp/dades

# Fabrica un tubo

date > /tmp/dades

 





```
isx36579183@i11:/tmp$ tail -f /tmp/dades
Tue 18 Jan 2022 11:28:04 AM CET



```

# Named Pipe

# named pipe

# mkfifo nom

# Tenemos 2 tubos donde uno escribe y el otro lee

--------------------------------------------------------------------------------

# FD --> File Descriptor

# Hereda la entrada estándar y la salida de ERROR.

sx36579183@i11:/tmp$ ls -l /proc/10875/fd
total 0
lrwx------ 1 isx36579183 hisx2 64 Jan 18 11:31 0 -> /dev/pts/5
lrwx------ 1 isx36579183 hisx2 64 Jan 18 11:31 1 -> /dev/pts/5
lrwx------ 1 isx36579183 hisx2 64 Jan 18 11:31 2 -> /dev/pts/5
l-wx------ 1 isx36579183 hisx2 64 Jan 18 11:31 3 -> /tmp/carta.txt
isx36579183@i11:/tmp$ 

El 3 apunta a tmp.carta

# 


##################################################################




| 🔥11-EXEMPLE-POPEN.PY❗🔥 | 



# /usr/bin/python3
#-*- coding: utf-8-*-
#
# exemple-popen.py
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys, argparse
from subprocess import Popen, PIPE
parser = argparse.ArgumentParser(description=\
        """Exemple popen""")
parser.add_argument("ruta",type=str,\
        help="directori a llistar")
args=parser.parse_args()
# -------------------------------------------------------
command = ["ls", args.ruta]
pipeData = Popen(command, stdout=PIPE)
for line in pipeData.stdout:
    print(line.decode("utf-8"), end=" ")
exit(0)


# POPEN

* Exemple de comunicació entre procesos --> Popen

1. ls, ruta --> Crea un tubo (Popen) = Pipe | En el otro extremo del tubo, ejecuta un $ ls arg

2. El command, genera una salida. [LISTA]

3. ls / | python

4. Genera una serie de información y sale para el programa de Python.

5. Popen = Constructor de una clase (Permite construir PIPES) = TUBOS.

6. Popen(command, stdout=PIPE) --> El command --> Su stdout sale en su PIPE.

---

1. Su orden lo envia al TUBO --> Luego le envía al programa de Python.

El progrmaa de Python tiene un tubo, tiene que leer el tubo.

2. Para cada línea printa la linea. 

3. Es un bucle que lee el tubo.

for line in pipeData.stdout:

# Tiene que hacer un read del stdout.

# Tener un mecanismo por el cual, ejecuta una orden, cualquier orden, se ejecuta y el resultado de la orden, retorna en el programa de Python, lo lee como si fuera de un fichero.


----

# Verificación



```
isx36579183@i11:~/Documents/ipc$ python3 11-exemple-popen.py /
bin
 boot
 dev
 etc
 home
 home_local
 initrd.img
 initrd.img.old
 lib
 lib32
 lib64
 libx32
 lost+found
 media
 mnt
 opt
 proc
 root
 run
 sbin
 snap
 srv
 sys
 tmp
 usr
 var
 vmlinuz
 vmlinuz.old
 isx36579183@i11:~/Documents/ipc$ 

```

```
isx36579183@i11:~/Documents/ipc$ python3 11-exemple-popen.py /tmp
carta.txt
 krb5cc_103033_b3HU3L
 krb5ccmachine_INFORMATICA.ESCOLADELTREBALL.ORG
 m01
 mozilla_isx365791830
 ssh-vGnv2BWnEVlA
 systemd-private-01361c64f73c4e9598cbda7726630138-colord.service-E4RS5g
 systemd-private-01361c64f73c4e9598cbda7726630138-fwupd.service-fc57Ph
 systemd-private-01361c64f73c4e9598cbda7726630138-ModemManager.service-3VnXfj
 systemd-private-01361c64f73c4e9598cbda7726630138-switcheroo-control.service-ET1ttj
 systemd-private-01361c64f73c4e9598cbda7726630138-systemd-logind.service-Q1Rwjh
 systemd-private-01361c64f73c4e9598cbda7726630138-systemd-timesyncd.service-vNctxf
 systemd-private-01361c64f73c4e9598cbda7726630138-upower.service-wEFV3h
 Temp-1d299991-89aa-40e2-a636-d0d69dd981aa
 Temp-7d70c627-8cfb-4f26-8c83-4b3d416d3bac
 tracker-extract-files.103033
 tracker-extract-files.115
 vboxdrv-Module.symvers
 isx36579183@i11:~/Documents/ipc$ 

```


# UNIDIRECCIONAL

command = ["who"]


isx36579183@i11:~/Documents/ipc$ python3 11-exemple-popen.py /tmp
isx36579183 :1           2022-01-18 09:51 (:1)


--------------------------------------------------------------------------------


| 🔥DOCUMENTACIÓN POPEN❗🔥 | 

https://docs.python.org/3/library/subprocess.html?highlight=subprocess%20popen#subprocess.Popen

https://docs.python.org/3/library/

# Libreria SYS




##################################################################




import sys

FROM subprocess import Popen, PIPE

# --> Especifica.

Sino

# import subprocess.Popen, subprocess.PIPE

----




Popen(["/usr/bin/git", "commit", "-m", "Fixes a bug."])

```
>>> import shlex, subprocess
>>> command_line = input()
/bin/vikings -input eggs.txt -output "spam spam.txt" -cmd "echo '$MONEY'"
>>> args = shlex.split(command_line)
>>> print(args)
['/bin/vikings', '-input', 'eggs.txt', '-output', 'spam spam.txt', '-cmd', "echo '$MONEY'"]
>>> p = subprocess.Popen(args) # Success!
```

- Hay que hacer un SPLIT.










##################################################################





# - Popen.stdout -->  El atributo es "readable stream object" - devuelto por open(). Lee el output por el proceso hijo.

# si el argumento no es PIPe no hace nada.

# Será un flujo igual que OPEN(), podremos leer del flujo. Podemos leer el flujo de la orden CLIENTE.

```
If the stdout argument was PIPE, this attribute is a readable stream object as returned by open(). Reading from the stream provides output from the child process. If the encoding or errors arguments were specified or the universal_newlines argument was True, the stream is a text stream, otherwise it is a byte stream. If the stdout argument was not PIPE, this attribute is None.
```









##################################################################


########### EJEMPLOS DE POPEN #########################3




>>> pipeData.stdout
<_io.BufferedReader name=3>
>>> 

----

# Es un flujo donde leerá los datos.

-----

>>> pipeData.stdout.readline()
b'isx36579183 :1           2022-01-18 09:51 (:1)\n'
>>> 


-----

Devuelve b pero no hay nada


##################################################################






11-exemple-popen.py dir

Crear un programa que executa un ls de un argument rebut i mostra per stdout el que rep del popen. 

Utilitza subprocess.Popen.


1. 

2.

3.

4.

5.

6.

7.

8.

9.

10.

11.

12.

13.

14.

15.

16.

17.

18.

19.

20.







"""

