import math

def es_primer(n):
    '''
    Funcion que dice si n en primo o no
    Input: int
    Output: boolean
    '''
    num = 2
    while (n % num) != 0:
        num += 1
    return n == num

def següent_primer(n):
    '''
    Funcio que devuelve el siguiente numero primo de n
    Input: int > 0
    Outout: int
    '''
    

'''
if __name__ == "__main__":
    if True:
        # Juego de pruebas
        # Entrada   Salida
        # -           False
        # 1           True
        # 0           False
        # abc         False
        # 1.5         False
        # -1          False
        # 5 abc       False
'''