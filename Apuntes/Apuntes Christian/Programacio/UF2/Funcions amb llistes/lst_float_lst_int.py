# FUNCIONS
import sys

def es_float(cad):
	'''
    FUnción que determina si es un float o no.
	input: str no vacia
	output: boolean
	'''	
	# sacar el signo, si esta
	if cad[0] in '+-':
		cad = cad[1:]
	
	# separar por el .
	camps = cad.split('.')

	# len 3 o mas
	if len(camps) >= 3:
		return False
	
	# si len és 1
	if len(camps) == 1:
		return camps[0].isdigit()
	
	# si len és 2
	# si és 3.3
	if camps[0].isdigit() and camps[1].isdigit():
		return True
	elif cad == '.':
		return False
	# caso: .3 y 3.
	elif (camps[0] == '' and camps[1].isdigit()) or (camps[0].isdigit() and
		camps[1] == ''):
			return True
	return False

def lst_str_a_lst_int(lst_str):
    '''
    Función que transforma una lista de str a uns
    lista de ints.
    in: lst (de cadenas)
    out: lst (de nums)
    '''
    # crear una lista para los nums
    lst_int = []

    # bucle: pasar a int, cada elemento de la lista
    for elem in lst_str:
        lst_int.append(int(elem)) # pasar a int
    
    # devolver la lista de ints
    return lst_int

def maximo(llista):
    '''
    Función que muestra el maximo de una lista
    in: lst (lista de caracters/digitos)
    out: int/str (caracter/digito mas grande)
    '''
    # agarrar maximo por defecto
    maxi = llista[0]

    # bucle: buscar el maximo
    for elem in llista:
        # si es mas grande que el maximo
        if elem > maxi:
            maxi = elem # se convierte en el maximo
    
    # devuelve el maximo
    return maxi

# PROGRAMA PRINCIPAL
# leer los argumentos
caracteres = sys.argv[1:]

lst_str = []
lst_float = []
# bucle: crear una lista de float i una de strs
for elem in caracteres:
    if not elem.isdigit():
        lst_str.append(elem)
    if es_float(elem):
        lst_float.append(elem)
lst_float = lst_str_a_lst_int(lst_float)

max_float = 0
max_str = ''
# buscar el maximo de los floats
max_float = maximo(lst_float)
# buscar el maximo de los strs
max_str = maximo(lst_str)

# mostrar los resultados
print(max_float)
print(max_str)

# TEST DRIVER
if __name__=='__main__':
    if False:
        print(lst_str_a_lst_int(['1','2','3']))