'19/03/2021' "-->" "19, 3, 2021"

def get_data(fecha_valida):
    '''
    Funcion que mediante una fecha valida da el dia siguiente
    Input: str (fecha valida)
    Output: tupla de 3 int [dia,mes,año]
    '''
    # calcular
    campos = fecha_valida.split('/')
    d = int(campos[0])
    m = int(campos[1])
    a = int(campos[2])

    return (d,m,a)

# test drive
data1 = get_data('19/03/2021')

dia = data1[0] 
mes = data1[1]
a = data1[2]
print(dia,mes,a)