# Hace una funcion que traduzca un mensaje hexadecimal a un mensaje.
# E.E. str (mensaje codificado en hexadecimal)

# FUNCIONES
def baseb_to_decimal(numb,b):
    '''
    Funcion que transforma cadenas de 2 digitos de b16 a decimal (por comenzar)
    input: cadena de 2 digits b16
    output: int
    '''
    numb = numb.upper()
    total = 0
    exponent = len(numb) - 1
    # bucle: transforma hexa a decimal
    for cad in numb:
        if cad >= '0' and cad <= '9':
            total = total + int(cad) * b ** exponent
        else:
            total = total + (ord(cad) - ord('A') + 10) * b ** exponent
        exponent = exponent - 1
    
    # devuelva el decimal
    return total

def traductor_hexa(cifrado):
    '''
    in: str (cadena haxadecimal correcto (i cada dos son un caracter))
    out: str (text)
    '''
    # para pasar a hexadecimal
    mensaje = ''

    # bucle: cortar de 2 en 2
    for i in range(0,len(cifrado),2):
        byte = cifrado[i:i + 2]
        # pasar a decimal
        num = baseb_to_decimal(byte,16)
        # buscar el caracter
        c = chr(num)
        # añadir a la frase
        mensaje = mensaje + c
    
    # devolver mensaje
    return mensaje

# PROGRAMA PRINCIPAL
# leer hexadecimal
cadena = input()
print(traductor_hexa(cadena))