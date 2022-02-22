#menores buscar los numeros primos menores que n
import math
import sys

def es_primer(n):
    '''
    Input: int
    Output: boolean
    '''

    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# leemos el maximo
maxim = int(sys.argv[1])
# por cada numero de 2 a n:
for i in range(0, maxim):
    # si es primo
    if es_primer(i):
        # lo mostramos
        print(i)