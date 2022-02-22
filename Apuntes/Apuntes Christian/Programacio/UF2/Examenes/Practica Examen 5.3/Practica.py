# 1
# 1.1
import sys
def convertir_a_segons(hora_valida):
    '''
    in: str(hora valida)
    out: str(segundos)
    '''
    # recortar hora
    h,m,s = get_hora(hora_valida)

    # devolver los segundos
    return h * 3600 + m * 60 + s

def es_format_valid(cadena):
    '''
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

def es_hola_valida(hora_rellotge):
    '''
    in: str (hora rellotge)
    out: boolean
    '''
    # comprobar si es formato correcto
    if not es_format_valid(hora_rellotge):
        return False
    
    h,m,s = get_hora(hora_rellotge)
    # comprobar si es una hora real
    return (h > -1 and h < 24) and (m > -1 and m < 60) and (s > -1 and s < 60)

def seguent_segon(hora_valida):
    '''
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

def crea_hora(h,m,s):
    '''
    in: 3 int
    out: str (hora rellotge)
    '''
    # formar hora: hh:mm:ss
    return f'{h:02}:{m:02}:{s:02}'

def get_hora(hora_valida):
    '''
    in: str (hora valida)
    out: lista de 3 int
    '''
    # recortar la hora
    campos = hora_valida.split(':')

    # pasar de str a int
    h = int(campos[0])
    m = int(campos[1])
    s = int(campos[2])

    # devolver hora,minuto,segundo
    return (h,m,s)

# 1.2
"""
# leer la hora,minuto y segundo por argumento
h = int(sys.argv[1])
m = int(sys.argv[2])
s = int(sys.argv[3])

# pasar la hora,minutos y segundos al formato(hh:mm:ss)
hora = crea_hora(h,m,s)

# si es una hora valida
if es_hola_valida(hora):
    # mostrar los segundos de la hora
    print(convertir_a_segons(hora))
"""

# 1.3
"""
# CONTROL DE ERRORES
MENSAJE = f'{sys.argv[0]} int(hora) int(min) int(sec)'

# comprobar la longitud
if len(sys.argv[1:]) != 3:
    print(MENSAJE)
    exit(1)

h = sys.argv[1]
m = sys.argv[2]
s = sys.argv[3]
# comprobar si los campos son digitos
if not (h.isdigit() and m.isdigit() and s.isdigit()):
    print(MENSAJE)
    exit(1)

h = int(h)
m = int(m)
s = int(s)

# PROGRAMA PRINCIPAL
# pasar la hora,minutos y segundos al formato(hh:mm:ss)
hora = crea_hora(h,m,s)

# si es una hora valida
if es_hola_valida(hora):
    # mostrar los segundos de la hora
    print(convertir_a_segons(hora))
"""