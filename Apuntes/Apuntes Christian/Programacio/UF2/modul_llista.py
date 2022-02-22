#!/usr/bin/python3

# Autor: Cristian Condolo
# Fecha: curs 2020-21

# Versión con juego de pruebas completo

# Descripción:
'''
Modulo para trabajar con listas de frecuencias.
Un lista de frecuencia que indica las veces que
se repiten los caracteres a buscar dentro de la
secuencia de caracteres.
'''

def cerca_sequencial(el, sequencia):
    '''
	Función que busca en que posición se encuentra un elemento
    dentro de una successión
    input: elemento, secuència (ex: caràcter y string)
    output: int (posición, -1 si el elemento no està en la secuencia)
    '''
    # bucle: por cada elemento de la secuencia
    for i in range(0, len(sequencia)):
        # comprobar si és el mismo
        if el == sequencia[i]:
            return i # devolver posición
    
    # si no existe
    return -1

def frequencia_elements(seq,els_a_buscar):
    '''
    Función que calcula la frecuencia de unos elementos.
    in: lst (de cadenas), str (caracteres a buscar)
    out: lst de ints (de frecuencias)
    '''
    # crear lista de frecuencias
    frecuencia = [0] * len(els_a_buscar)

    # bucle: per cada caràcter
    for c in seq:
        # busco en que posición està
        pos = cerca_sequencial(c, els_a_buscar)
        if pos != -1:
            #incrementar la frecuencia de la posición
            frecuencia[pos] += 1
    
    # devolver la lista de frecuencia
    return frecuencia

def ordena_bombolla(llista):
    '''
    Funcion que ordena de lista de cualquier cosa, o tambien
    ordenar una lista de listas.
    in: lista de cualquier cosa
    out: lista ordenada
    '''
    # bucle: recorre toda la lista
    for i in range(1,len(llista)):
        final = len(llista) - i # guardar limite, para que no pete

        # bucle: ordenar los caracteres
        for j in range(0,final):
            # si es mayor
            if (llista[j] > llista[j + 1]):
                # los cambiamos de posicion
                t = llista[j]
                llista[j] = llista[j + 1]
                llista[j + 1] = t
    
    # devolver la lista ordenada
    return llista

def take_first(elem):
    '''
    Key function que ordena segun el primer campo.
    in: elemento a ordernar

    '''
    return elem[0]

def take_second(elem):
    '''
    Key function que ordena segun el segundo campo.
    in: elemento a ordernar
    
    '''
    return elem[1]

def take_third(elem):
    '''
    Key function que ordena segun el tercer campo.
    in: elemento a ordernar
    
    '''
    return elem[2]

# TEST DRIVER de funciones
if __name__ == '__main__':
    # test driver de cerca_sequencial
    if False:
        print(cerca_sequencial('o', 'aeiou'))
        print(cerca_sequencial('p', 'aeiou'))
        print(cerca_sequencial(3, [2, 4, 3,-1]))
        print()
    
    # test driver de frequencia_elements
    if False:
        print(frequencia_elements('bon diaaaaa', 'aeiou'))
        print(frequencia_elements('bon diaaaaa', 'abc'))
        print(frequencia_elements([3, 3, 5, 6, 5, 3, 8], [3, 5, 9]))
    
    # test driver de ordena_bombolla
    if True:
        print('9, 7, 2, 8, 1',ordena_bombolla([9, 7, 2, 8, 1]))