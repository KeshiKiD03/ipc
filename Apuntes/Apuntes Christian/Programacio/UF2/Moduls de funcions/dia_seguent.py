def es_any_traspas(a):
	'''
	Funció que diu si un any és o no de traspàs
	Input: enter positiu (any)
	output: boolean
	'''
	return (a % 400 == 0) or ( a % 4 == 0 and a % 100 != 0)

def dies_mes(m, a):
	'''
	Funció que ens diu quants dies té un mes
	input: dos enters. m ha de ser entre 1 i 12 (inclosos) i a positiu
	output: enter
	'''
	DIES_MES = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	dies = DIES_MES[m]
    # si es año bisiesto y es febrero, tiene 29 dias
	if m == 2 and es_any_traspas(a):
		dies = 29
	
    # devuelve el ultimo dia del mes
	return dies

def get_data(cadena):
    '''
    in: str (fecha real)
    out: 3 int (dia,mes,año)
    '''
    # recortamos fecha
    campos = cadena.split('/')

    # pasamos de str a int
    dia = int(campos[0])
    mes = int(campos[1])
    año = int(campos[2])

    # devolvemos dia,mes,año
    return (dia,mes,año)

def crea_data(d, m, a):
	'''
	Función que crea una fecha en formato vàlido
	input: 3 int
	output: str (fecha en formato correcto)
	'''
    # escribe la fecha: dd/mm/aaaa
	return f'{d:02}/{m:02}/{a:04}'

def dia_seguent(data):
	'''
	Funció que rep una data i retorna el dia seguent
	Input: str (Data correcta)
	Output: str (data correcta)
	'''
	# recortar la fecha
	d, m, a = get_data(data)
	
    # si el dia es igual al ultimo dia del mes
	if d == dies_mes(m, a):
		d = 1
		m = m + 1
        # si el mes se pasa de 12
		if m == 13:
			m = 1
			a = a + 1
	else: # sino suma un dia
		d = d + 1
	
    # devolvemos la fecha siguiente
	return crea_data(d, m, a)