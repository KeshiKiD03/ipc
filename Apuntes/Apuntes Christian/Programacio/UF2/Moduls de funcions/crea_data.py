def crea_data(d, m, a):
	'''
	Función que crea una fecha en formato vàlido
	input: 3 int
	output: str (fecha en formato correcto)
	'''
	return f'{d:02}/{m:02}/{a:04}'

# TEST DRIVER de crea_data:
if __name__=='__main__':
    if True:
        print(crea_data(3, 5, 2000))
        print(crea_data(33, 5, 2000))