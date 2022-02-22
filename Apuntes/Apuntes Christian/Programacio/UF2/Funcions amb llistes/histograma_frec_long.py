# FUNCIONES
import sys

def frequencia_long(lst_cadena):
    '''
    FUnción que devuelve una lista con la frecuencia de
    longitud de todos los caracteres
    in: lst (de caracteres)
    out: lst (frecuencia longitudes)
    '''
    # crear la lista de frequencia
    frecuencia = [0] * (10 + 1)# longitud max: 10 por defecto

    # bucle: contar veces que repiten longitud
    for pos in range(0,len(lst_cadena)):
        if len(lst_cadena[pos]) > len(frecuencia): # si hay una len que sobrepasa el len por defecto
            resta = len(lst_cadena[pos]) - len(frecuencia)
            # bucle: adapta el lista de frecuencia
            for zero in range(-1,resta):
                frecuencia.append(0) # añadir un zero mas
        # incrementar frecuencia de longitud
        frecuencia[len(lst_cadena[pos])] += 1

    # devolver lista de frecuencia
    return frecuencia[1:]

def histograma_long(lst_frequencia,CARACTER):
    '''
    Función que dibuja un histograma que muestra la
    frecuencia de longitudes de una cadena.
    in: lst (de frecuencia), str(caracter que represente la cantidad)
    out: none
    '''
    # bucle: dibujar histograma
    for var in range(0,len(lst_frequencia)):
        print(f'{var+1}\t:{CARACTER * lst_frequencia[var]}')

# PROGRAMA PRINCIPAL
# leer las cadenas por argumento
cadenas = sys.argv[1:]

# crear la lista de frecuencia de longitudes
lst_frecuencia = frequencia_long(cadenas)

# dibujar el histograma
histograma_long(lst_frecuencia,'*')

if __name__=='__main__':
    if False:
        print(frequencia_long(['hola','que','tal']))
        histograma_long(frequencia_long(['hola','que','tal']),'*')
        print(frequencia_long(['hola a tothom']))
        histograma_long(frequencia_long(['hola a tothom']),'*')