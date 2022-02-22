#!/usr/bin/python3

# PART TEORICA
# Ex1
"""
0 llista = [9,7,2,8,1]
1
2 for i in range(1,len(llista)):
3     final = len(llista) - i
 
4     for j in range(0,final):
5         if (llista[j] > llista[j + 1]):
6             # comenta que es fa en les ordres de sota
7             t = llista[j]
8             llista[j] = llista[j + 1]
9             llista[j + 1] = t
10 
11 print('llista final', llista)
"""
"""
linia | range[] | i | final | j | llista[j] | llista[j + 1] | llista

"""

# Ex2
# Juego de pruebas
# Entrada                                       | Salida
#08/07/2012  08/04/2012  28/05/2012  08/11/2012 | 250  212   160  300
#08/07/2012  08/04/2012  28/05/2012  28/05/2012 | 250  212   160  160

# Control de errores
# Entrada                                       | Salida
#08/07/2012  08/04/2012  28/05/2012  08/11/2012 |          T
#08/07/2012  78/04/2012  28/05/2012  28/05/2012 |          F
#08-07-2012  78/04/2012  28/05/2012  28/05/2012 |          F
#                                               |          F

# Programa
# FUNCIONES
import modul_calendari
import modul_llista
import sys

# CONTROL DE ERRORES
MENSAJE = f'Error: prog.py fecha_valida(../2012)[1..4]'

# comprobar el num de arguments
if len(sys.argv[1:]) <= 0:
    print(MENSAJE)
    exit(0)

# bucle: comprobar si son fechas validas
for elem in sys.argv[1:]:
    if not modul_calendari.es_data_valida(elem):
        print(MENSAJE)
        exit(0)

# bucle: comprobar que fechas del 2012
for elem in sys.argv[1:]:
    año = modul_calendari.get_data(elem)[2]
    if año != 2012:
        print(MENSAJE)
        exit(0)

# PROGRAMA PRINCIPAL
# leer fechas por argumento
fechas_nacimiento = sys.argv[1:]

lista_dias =  []
# bucle: pasar las fechas a su dia del año
for fecha in fechas_nacimiento:
    dia_año = modul_calendari.dia_any(fecha)
    lista_dias.append(dia_año)

# ordernar lista de fechas
lista_ordenada = modul_llista.ordena_bombolla(lista_dias)

# mostra la lista de fechas ordenadas
print(lista_ordenada)

# TEST DRIVER de Juego de pruebas
if __name__ == '__main__':
    if True:
        print('08/07/2012, 08/04/2012, 28/05/2012, 08/11/2012',)
