# /usr/bin/python
#-*- coding: utf-8-*-
#
# popen-sql.py
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys, argparse
from subprocess import Popen, PIPE
# -------------------------------------------------------
command = " psql -qtA -F',' -h 172.17.0.2 -U edtasixm06 training -c \"select * from clientes; \""
pipeData = Popen(command,shell=True,stdout=PIPE)
# stdout = PIPE --> Si el argumento no es PIPE, no hace nada. Si el argumento es PIPE, será un objeto legible.
# Será un flujo donde se puede leer. Estamos leyendo la salida de la orden CLIENTE.
# Si decimos pipeData.stdout --> Es un bufer donde leerá cosas, es un flujo.
for line in pipeData.stdout:
  print(line.decode("utf-8"), end="")
exit(0)


"""

## NOMBRE DEL PROGRAMA + SINTAXIS

**12-popen-sql.py** 

  Es pot fer una primera versió tot hardcoded sense diàleg amb: 
  psql -qtA -F';' training  -c “select * from oficinas;”.
  Executa la consulta “select * from oficinas;” usant psq.  
  Atenció: posar al popen shell=True.
  Podem usar un container Docker amb la bd training de postgres
  fent:

```
Hi ha un docker a dockerhub:
$ docker run --rm --name psql -h psql -it edtasixm06/postgres /bin/bash

A la adreça de github [asixm06-docker](https://github.com/edtasixm06/asixm06-docker/tree/master/postgres:base) hi la les ordres per engegar el postgres.

Cal fer-les per posar en marxa el servei i inicialitzar la base de dades.
$ su -l postgres
$ /usr/bin/pg_ctl -D /var/lib/pgsql/data -l logfile start

Verificar el funcionament des de dins del container:
$ psql -qtA -F',' training -c "select * from clientes;"


Des del host executar consultes, cal indicar la adreça ip del container al que connectem, i l’usuari (role) que és edtasixm06:
$  psql -qtA -F',' -h 172.17.0.2 -U edtasixm06 training -c "select * from clientes;"

Si volem que el container faci map a un dels ports del host:
$ docker run --rm --name psql -h psql -p 5432:5432  -it edtasixm06/postgres /bin/bash
$inicialitzar des de dins del docker
$ psql -qtA -F','  -h d02  -U edtasixm06 training -c "select * from oficinas;"
```

# ----------------------------------------------

# Resumen 

1. 


## Explicación

**12-popen-sql.py** 

  Es pot fer una primera versió tot hardcoded sense diàleg amb: 
  psql -qtA -F';' training  -c “select * from oficinas;”.
  Executa la consulta “select * from oficinas;” usant psq.  
  Atenció: posar al popen shell=True.
  Podem usar un container Docker amb la bd training de postgres
  fent:

```
Hi ha un docker a dockerhub:
$ docker run --rm --name psql -h psql -it edtasixm06/postgres /bin/bash

A la adreça de github [asixm06-docker](https://github.com/edtasixm06/asixm06-docker/tree/master/postgres:base) hi la les ordres per engegar el postgres.

Cal fer-les per posar en marxa el servei i inicialitzar la base de dades.
$ su -l postgres
$ /usr/bin/pg_ctl -D /var/lib/pgsql/data -l logfile start

Verificar el funcionament des de dins del container:
$ psql -qtA -F',' training -c "select * from clientes;"


Des del host executar consultes, cal indicar la adreça ip del container al que connectem, i l’usuari (role) que és edtasixm06:
$  psql -qtA -F',' -h 172.17.0.2 -U edtasixm06 training -c "select * from clientes;"

Si volem que el container faci map a un dels ports del host:
$ docker run --rm --name psql -h psql -p 5432:5432  -it edtasixm06/postgres /bin/bash
$inicialitzar des de dins del docker
$ psql -qtA -F','  -h d02  -U edtasixm06 training -c "select * from oficinas;"
```


# ----------------------------------------------

## Metodología Y APUNTES


##################### POPEN ########################

## POPEN CONSTRUCTOR

* La clase es subproces.Popen()

* Si hacemos from subprocess import Popen, PIPE

  * Sólamente importaremos
  
* Al popen le pasamos el "programa ejecutable", se le pasa como argumento el stdout=PIPE.


--------------------------------------------------------------------------------

[Hacer una container con PSQL con DETACH con la base de datos TRAINING]

1. Encender un container de PostgreSQL.

2. Su -l postgres

3. /usr/bin/pg_ctl -D /var/lib/pgsql/data -l logfile start

4. $ psql -qtA -F',' -h [host] -U [postgres] training -c "select * from clientes;

5. Base de datos POSTGRES.

**12-popen-sql.py** 

  Es pot fer una primera versió tot hardcoded sense diàleg amb: 
  psql -qtA -F';' training  -c “select * from oficinas;”.
  Executa la consulta “select * from oficinas;” usant psq.  
  Atenció: posar al popen shell=True.
  Podem usar un container Docker amb la bd training de postgres
  fent:

```
Hi ha un docker a dockerhub:
$ docker run --rm --name psql -h psql -it edtasixm06/postgres /bin/bash

A la adreça de github [asixm06-docker](https://github.com/edtasixm06/asixm06-docker/tree/master/postgres:base) hi la les ordres per engegar el postgres.

Cal fer-les per posar en marxa el servei i inicialitzar la base de dades.
$ su -l postgres
$ /usr/bin/pg_ctl -D /var/lib/pgsql/data -l logfile start

Verificar el funcionament des de dins del container:
$ psql -qtA -F',' training -c "select * from clientes;"


Des del host executar consultes, cal indicar la adreça ip del container al que connectem, i l’usuari (role) que és edtasixm06:
$  psql -qtA -F',' -h 172.17.0.2 -U edtasixm06 training -c "select * from clientes;"

Si volem que el container faci map a un dels ports del host:
$ docker run --rm --name psql -h psql -p 5432:5432  -it edtasixm06/postgres /bin/bash
$inicialitzar des de dins del docker
$ psql -qtA -F','  -h d02  -U edtasixm06 training -c "select * from oficinas;"
```



####################################################################################



############## 12.POPEN-SQL.PY #################


# /usr/bin/python
#-*- coding: utf-8-*-
#
# popen-sql.py
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys, argparse
from subprocess import Popen, PIPE
# -------------------------------------------------------
command = " psql -qtA -F',' -h 172.17.0.2 -U edtasixm06 training -c \"select * from clientes; \""
pipeData = Popen(command,shell=True,stdout=PIPE)
for line in pipeData.stdout:
  print(line.decode("utf-8"), end="")
exit(0)



* DOCKER

	* docker run --rm --name psql -h psql -it edtasixm06/postgres /bin/bash
	
	* su -l postgres
	
	* /usr/bin/pg_ctl -D /var/lib/pgsql/data -l logfile start
	
	* psql -qtA -F',' training -c "select * from clientes;"
	
	----
	
* HOST

	* Instalar POSTGRESQL
	
	* Probar consulta: "psql -qtA -F',' -h 172.17.0.2 -U edtasixm06 training -c "select * from clientes;""
	
	* Si queremos que el container haga map a uno de los puertos = $ docker run --rm --name psql -h psql -p 5432:5432  -it edtasixm06/postgres /bin/bash






https://gitlab.com/isx-m02-m10-bd/uf2-sql-ddl-i-dml-public/-/raw/main/introduccio/0_install_config_postgreSQL.md


isx36579183@i11:~/Documents/ipc$ python3 12-popen-sql.py 
2111,JCP Inc.,103,50000.00
2102,First Corp.,101,65000.00
2103,Acme Mfg.,105,50000.00
2123,Carter & Sons,102,40000.00
2107,Ace International,110,35000.00
2115,Smithson Corp.,101,20000.00
2101,Jones Mfg.,106,65000.00
2112,Zetacorp,108,50000.00
2121,QMA Assoc.,103,45000.00
2114,Orion Corp,102,20000.00
2124,Peter Brothers,107,40000.00
2108,Holm & Landis,109,55000.00
2117,J.P. Sinclair,106,35000.00
2122,Three-Way Lines,105,30000.00
2120,Rico Enterprises,102,50000.00
2106,Fred Lewis Corp.,102,65000.00
2119,Solomon Inc.,109,25000.00
2118,Midwest Systems,108,60000.00
2113,Ian & Schmidt,104,20000.00
2109,Chen Associates,103,25000.00
2105,AAA Investments,101,45000.00
isx36579183@i11:~/Documents/ipc$ 



---------------------

13. 13-popen-sql-injectat.py  consulta 


* Pasarle un STRING. // ARGUMENT

* 13-popen-sql-injectat.py  consulta

Fer que la sentència sql a fer sigui un argument tot entre cometes que es passa com a argument. sql injectat: perills d’injectar codi d’usuari en els programes.









####################################################################################



############### SOLUCIÓN #################




# SOLUCIÓN

# /usr/bin/python
#-*- coding: utf-8-*-
#
# popen-sql.py
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
# Utilitza el docker edtasixm06/postgres
# -----------------------------------------
#commandLocal = "psql -qtA -F ';' lab_clinic -c 'select * from pacients;'"
#commandRemote = "psql -qtA -h i11 -U postgres -F ';' lab_clinic -c 'select * from pacients;'"
# -------------------------------------------
import sys
from subprocess import Popen, PIPE
import argparse
parser = argparse.ArgumentParser(description='Consulta SQL interactiva')
parser.add_argument('sqlStatment', help='Sentència SQL a executar',metavar='sentènciaSQL')
args = parser.parse_args()

cmd = "psql -qtA -F',' -h 172.17.0.2 -U postgres  training"
#py2# pipeData = Popen(cmd, shell = True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
pipeData = Popen(cmd, shell = True, bufsize=0, universal_newlines=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
pipeData.stdin.write("select * from oficinas;\n\q\n")

for line in pipeData.stdout:
  print(line, end="")
sys.exit(0)






####################################################################################




### SOLUCIÓN

cmd = "psql -qtA -F',' -h 172.17.0.2 -U postgres  training"

* Nos conecta en una máquina PostgreSQL

psql -qtA -F',' -h 172.17.0.2 -U postgres training 

* Enciende una sesión de diálogo con TRAINING.













####################################################################################



####### COMPROBACIONES ##############



isx36579183@i11:~/Documents/ipc$ python3 13-popen-sql-injectat.py "select * from clientes;"
22,Denver,Oeste,108,300000.00,186042.00
11,New York,Este,106,575000.00,692637.00
12,Chicago,Este,104,800000.00,735042.00
13,Atlanta,Este,105,350000.00,367911.00
21,Los Angeles,Oeste,108,725000.00,835915.00
isx36579183@i11:~/Documents/ipc$ 





---------------------------------



https://docs.python.org/3/library/subprocess.html





>>> pipeData.stdin.write("select * from oficinas;\n")
24
>>> 


-----


>>> pipeData.stdout.readline()
'22,Denver,Oeste,108,300000.00,186042.00\n'
>>> 


-----


>>> pipeData.stdout.readline()
'22,Denver,Oeste,108,300000.00,186042.00\n'
>>> 


-----

>>> pipeData.stdout.readline()
'12,Chicago,Este,104,800000.00,735042.00\n'
>>> 


-----


>>> pipeData.stdout.readline()
'12,Chicago,Este,104,800000.00,735042.00\n'
>>> pipeData.stdout.readline()
'13,Atlanta,Este,105,350000.00,367911.00\n'
>>> pipeData.stdout.readline()
'21,Los Angeles,Oeste,108,725000.00,835915.00\n'
>>> pipeData.stdout.readline()


* Aún está leyendo.

* Se está recuperando. 

* Hay un problema --> Cuando leemos un fichero, cuando llegamos al final de la línea.

* El readline() --> Dice que ya está.

* El problema que hay es que si hacemos un SELECT y cuando lee linea a linea.

	* El for read nunca terminará, porque no hay un fin de fichero.
	
	* El procedimiento es leer linea a linea.
	













####################################################################################





* Ejecuta información, termina y muere.

* Mostrar mensaje de que ya ha terminado.






SHELL = TRUE --> Es como si estamos haciendo una sesión de SHELL

Bufsize = 

	0 --> Sin buffer

Comunicaciones con Buffer o sin Buffer.

	* Te bajas un documento. El marcador dice que ya se ha bajado, pero no lo puedes desmontar aún.
	
	* Cuando ya es seguro desmontar.
	
		* El sistema operativo dice que ya ha terminado.
		
			* Por debajo hay un buffer.
			
				* Se guarda en una memoria rapida llamada Buffer.


----------------------

* Nos devuelve texto.


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

