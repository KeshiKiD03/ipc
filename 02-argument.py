#/usr/bin/python3
#
# Python documentation:
# argparse tutorial: 

import argparse # Importamos la librería ARGPARSE
parser=argparse.ArgumentParser(description=\
  "programa exemple de processar arguments",prog="02-arguments.py",epilog="hasta luegu lucas!") # Establecemos en la variable "parser", el módulo argparse y la función/tipo ArgumentParser()
parser.add_argument("-e","--edat", type=int, dest="useredat", help="edat a processar", metavar="edat") # Añadimos método de argumento del tipo opcional
parser.add_argument("-f","--fit", type=str, help="fitxer a processar", dest="fitxer") # Añadimos método de argumento del tipo opcional
parser.add_argument("-n","--nom", type=str, help="nom de usuari") # Añadimos método de argumento del tipo opcional
#parser.add_argument("fit", type=str, help="fitxer") # Añadimos método de argumento del tipo posicional
args=parser.parse_args() # Añadimos método parse_args() --> Pulsa el botón.
#print(parser)
print(args)
print(args.useredat, args.nom)
exit(0)

