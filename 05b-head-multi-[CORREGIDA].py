# /usr/bin/python
#-*- coding: utf-8-*-
#
# head [-n 5|10|15] [-f file]...
#  10 lines, file... 
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2022
# -------------------------------------
import sys, argparse # Importamos los módulos sys y argparse
fileList=[] # Establecemos una LISTA VACÍA, fileList
parser = argparse.ArgumentParser(description=\
        """Mostrar les N primereslínies """,\
        epilog="thats all folks") # Llamamos el ARGUMENT PARSE
parser.add_argument("-n","--nlin",type=int,\
        help="Número de línies 5|10|15, def 10",\
        dest="nlin",\
        metavar="numLines",default=10,\
        choices=[5,10,15]) # Definimos un ARGUMENTO del tipo OPCIONAL. Del tipo Integer. # Usa choices para definir un conunto de valores válidos. Por defecto es 10, pero podemos escoger de 5, 10 o 15
parser.add_argument("-f", "--file",type=str,\
        help="fitxer a processar", metavar="file",\
        dest="fileList", nargs="*") # Definimos un ARGUMENTO del tipo OPCIONAL. Del tipo STRING. 
        # Metavar es el alias. 
        # Dest es el nombre de la VARIABLE. 
        # Action es el comando a realizar, en este caso APPEND. Añade al final.
        # Usa NARGS para rellenar con *
parser.add_argument("-v", "--verbose",action="store_true",default=False)
args=parser.parse_args()
print(args)
# -------------------------------------------------------
MAXLIN=args.nlin # Establecemos una CONSTANTE MAXLIN que analizará el número de líneas.

def headFile(fitxer): # Definimos una FUNCIÓN para acordar NUESTRO CÓDIGO. Dentro de la función le pasamos como PARÁMETRO FITXER.
  fileIn=open(fitxer,"r") # Abrimos el fichero en modo READ.
  counter=0 # Establecemos el contador
  for line in fileIn: # Recorremos fileIn
    counter+=1 # Incrementamos el contador
    print(line, end='') # Para cada línea me printas el valor de linea y un salto de línea
    if counter==MAXLIN: break # Si el contador es igual al número de argumentos haces un BREAK.
  fileIn.close() # Cerramos el fichero.

if args.fileList: # Si la lista fileList
  for fileName in args.fileList: # Para cada fileName en la lista fileList
    if args.verbose: print("\n",fileName, 40*"-") # Si hay -v / Booleano, muestra una cabecera con el nombre del fichero a listas. 
    headFile(fileName) # Llamamos la función headFile y mostramos el fileName.

exit(0)








"""

## NOMBRE DEL PROGRAMA + SINTAXIS

**05b-head-multi.py [-n 5|10|15]   [-f filein]...**

  Mostar les n primeres 5 o 10 o 15 (def 10)  de filein.
  Processa múltiples files indicats per -f file, -f file, etc.
  Ampliació: [-v][--verbose] boleà que si hi és mostra una capçalera 
  de llistat amb el nom del fitxer a llistar.


	USANDO NARGS
	
# ----------------------------------------------

## Explicación

**05b-head-multi.py [-n 5|10|15]   [-f filein]...**

  Mostar les n primeres 5 o 10 o 15 (def 10)  de filein.
  Processa múltiples files indicats per -f file, -f file, etc.
  Ampliació: [-v][--verbose] boleà que si hi és mostra una capçalera 
  de llistat amb el nom del fitxer a llistar.

	USANDO NARGS

# ----------------------------------------------

## Metodología y apuntes


ARGPARSE --> Analiza argumentos

    name or flags - Either a name or a list of option strings, e.g. foo or -f, --foo.

    action - The basic type of action to be taken when this argument is encountered at the command line.

    nargs - The number of command-line arguments that should be consumed.

    const - A constant value required by some action and nargs selections.

    default - The value produced if the argument is absent from the command line and if it is absent from the namespace object.

    type - The type to which the command-line argument should be converted.

    choices - A container of the allowable values for the argument.

    required - Whether or not the command-line option may be omitted (optionals only).

    help - A brief description of what the argument does.

    metavar - A name for the argument in usage messages.

    dest - The name of the attribute to be added to the object returned by parse_args().


>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--verbose', '-v', action='count', default=0)
>>> parser.parse_args(['-vvv'])



pepitu=argparse.ArgumentParser() --> Es una caja, un constructor


>>> pepitu
ArgumentParser(prog='', usage=None, description=None, formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=True)
>>> .



_CountAction(option_strings=['-v', '--verbose'], dest='verbose', nargs=0, const=None, default=0, type=None, choices=None, help=None, metavar=None)
>>> 





Analiza argumentos

>>> pepitu.parse_args(['-vvv'])
Namespace(verbose=3)
>>> 








El arguments se almacenan de forma en lista en varios lenguajes de prog, se convierten en .split()


>>> pepitu.parse_args("-v -vv -v".split())
Namespace(verbose=4)
>>> 









NARGS


-v
 consumeix	0


-n 15

	consumeix 15

-nom pere pou
    ----- ----
     consumeix 2


nargs es el numero d'arguments que ha de consumir, de una opció





isx36579183@i11:~/Documents/ipc$ python3 05b-head-multi.py -v -n 5 -f 01-head.py /etc/passwd


isx36579183@i11:~/Documents/ipc$ python3 05b-head-multi.py -v -n 5 -f 01-head.py /etc/passwd


isx36579183@i11:~/Documents/ipc$ python3 05b-head-multi.py -v -n5 -f 01-head.py /etc/passwd
Namespace(nlin=5, fileList=['01-head.py', '/etc/passwd'], verbose=True)

 01-head.py ----------------------------------------
# /usr/bin/python
#-*- coding: utf-8-*-
#
# head [file]
#  10 lines, file o stdin

 /etc/passwd ----------------------------------------
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync



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

