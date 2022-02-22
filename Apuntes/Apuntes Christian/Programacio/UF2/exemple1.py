#!/usr/bin/python3
# 07/25/2021
# Cristian Condolo
# M05 Programacio- UF2 
# Descripcion:
# Hacer funciones que multiplica dos int's.
# ========================================================
# Programa
# FUNCIONES
def multiplicar(n1,n2,res):
    '''
    Funcion que multiplica dos numeros
    in: 2 int (nums), lst(resultados)
    out: int (resultado)
    '''
    num1 = n1
    num2 = n2
    res = num1 * num2

def multiplicar1(n1,n2,res):
    '''
    Funcion que multiplica dos numeros
    in: 2 int (nums), lst(resultados)
    out: int (resultado)
    '''
    num1 = n1
    num2 = n2
    res.append(num1 * num2)

# PROGRAMA PRINCIPAL
resultado = []
res = 0
num1 = 5
num2 = 10
multiplicar(num1,num2,res)
print(res)
multiplicar1(num1,num2,resultado)
print(resultado)