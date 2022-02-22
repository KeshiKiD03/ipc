#!/usr/bin/python3

# Autor: Cristian Condolo
# Data: curs 2020-21

# Descripción:
'''
Mòdulo para trabajar con horas de reloj.
Una hora de reloj és una cadena del tipo
hh:mm:ss
que se correponde con una hora de reloj real
'''

def es_hora_valida(hora_rellotge):
    '''
    Función que determina si una hora de reloj es valida
    (hh:mm:ss)
    in: str (hora rellotge)
    out: boolean
    '''
    # comprobar si es formato correcto
    if not es_hora_format_correcte(hora_rellotge):
        return False
    
    h,m,s = get_hora(hora_rellotge)
    # comprobar si es una hora real
    return es_hora_real(h,m,s)

def get_hora(hora_valida):
    '''
    Función que dada una hora de reloj de formato
    correcto devuelve la hora, el minuto y el segundo
    in: str (hora valida)
    out: lista de 3 int
    '''
    # recortar la hora
    campos = hora_valida.split(':')

    # devolver hora,minuto,segundo
    return (int(campos[0]),int(campos[1]),int(campos[2]))

def es_hora_format_correcte(cadena):
    '''
    Función que determina si una cadena cualquiera tiene
    formato hh, mm y ss numeros enteros
    in: str (hora rellotge)
    out: boolean
    '''
    # comprobar la longitud de la cadena
    if len(cadena) != 8:
        return False
    
    campos = cadena.split(':')
    # comprobar la longitud de cada campo
    if not (len(campos[0]) == 2 and len(campos[1]) == 2 and len(campos[2]) == 2):
        return False
    
    # y comprobar si todos los campos son digitos
    return campos[0].isdigit() and campos[1].isdigit() and campos[2].isdigit() 

def es_hora_real(h,m,s):
    '''
    Función que determina si 3 enteros corresponde a una hora que 
    exista.
    in: 3 int
    out: boolean
    '''
    # comprobamos que la hora es correcta
    if not (h > -1 and h < 24):
        return False
    # comprobamos que el minuto es correcto
    if not (m > -1 and m < 60):
        return False
    # comprobar que los segundos sean correctos
    return s > -1 and s < 60

def hora_a_segons(h, m, s):
    '''
    in: 3 int(hora,minutos,segundos)
    out: int (segundos)
    '''
    # devolver los segundos
    return h * 3600 + m * 60 + s

def crea_hora(h,m,s):
    '''
    Función que transforma una hora de reloj en
    formato valido
    in: 3 int
    out: str (hora rellotge)
    '''
    # formar hora: hh:mm:ss
    return f'{h:02}:{m:02}:{s:02}'

def seguent_segon(hora_valida):
    '''
    Función que una hora de reloj al siguente
    segundo de la hora.
    in: str (hora valida)
    out: str (hora rellotge)
    '''
    # recortar la hora
    h,m,s = get_hora(hora_valida)

    # sumar 1 segundo
    s += 1
    if s == 60: # si los segundos llega a 60
        s = 0
        m += 1
        if m == 60: # si los minutos llega a 60
            m = 0
            h += 1
            if h == 24: # si la hora llega a 24
                h = 0
    # devuelve la hora(creada de nuevo)
    return crea_hora(h,m,s)

# TEST DRIVER
if __name__ == "__main__":
	# test driver de es_hora_format_correcte
	if True:
		print(es_hora_format_correcte('03:02:00'))
		print()
	# test driver de es_data_valida
	if True:
		# 1. Segun si el formato és correcto
		print(es_hora_valida('03:02:00'))
		print(es_hora_valida('23:02:00'))
		print(es_hora_valida('24:00:00'))
		print(es_hora_valida('03:62:00'))
		print(es_hora_valida('03:02:0'))
		print(es_hora_valida('03 02 00'))
		print(es_hora_valida('03:62:78'))
		print()
	# test driver de get_hora
	if True:
		print(get_hora('03:02:00'))
		print()	
	# test driver de es_hora_real
	if True:
		print(es_hora_real(14, 13, 20))
		print(es_hora_real(14, 0, 2020))
		print()
	# test driver de crea hora
	if True:
		print(crea_hora(3, 5, 20))
		print(crea_hora(23, 5, 20))		
		print(crea_hora(3, 3, 123))  # se puede crear horas con valores incorrectos
		print()