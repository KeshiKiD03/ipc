# primos menores que n
import math

def es_primer(n):
    '''
    Input: int
    Output: boolean
    '''

    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

#   test driver
print(es_primer(4))
print(es_primer(17))
print(es_primer(101))
print(es_primer(2))