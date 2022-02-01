# /usr/bin/python
#-*- coding: utf-8-*-
#
# exemple-execv.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,os
# ------------------------------------------------
print("Hola, començament del programa principal")
print("PID pare: ", os.getpid())

pid=os.fork()
if pid !=0:
  print("Programa Pare", os.getpid(), pid)
  sys.exit(0)

#-------------------------------------------------
print("Programa fill", os.getpid(), pid)
os.execv("/usr/bin/python3", ["/usr/bin/python3", "16-signal.py", "60"])    # Li passem els següents paràmetres perquè executi el programa 16 amb 60 segons.
#-------------------------------------------------
print("Hasta lugo lucas!")   # Mai és veurà!!!!!
sys.exit(0)


"""

## NOMBRE DEL PROGRAMA + SINTAXIS

**20-execv-signal.py**

  Usant l'exemple execv programar un procés pare que llança un fill i finalitza.
  El procés fill executa amb execv el programa python *16-signal.py* al que li 
  passa un valor hardcoded de segons.

# ----------------------------------------------

## Explicación

  Usant l'exemple execv programar un procés pare que llança un fill i finalitza.
  El procés fill executa amb execv el programa python *16-signal.py* al que li 
  passa un valor hardcoded de segons.


# ----------------------------------------------

## Metodología

1. 10 -

2. 15 -

3. Alarma = 14

4. Crear un daemon y se gestiona por SEÑALES.

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

