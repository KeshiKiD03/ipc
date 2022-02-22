# la fecha es valida
def es_data_valida(cadena):
    '''
    Funcion que valida fechas
    in: 1 str ( fecha(dd/mm/aaaa) )
    out: boolean
    '''
    # comprobar formato
    if not es_format_valid:
        return False
    
    # calcular dia, mes y año
    (dia, mes, año) = get_data(cadena)

    # comproba si la fecha es real
    return es_data_real(dia,mes,año)

# es formato valida
def es_format_valid(cadena):
    '''
    Funcion que determina si una fecha tiene el formato dd/mm/aaaa
    in: 1 str
    out: boolean
    '''
    # comprobar la longitud de la fecha
    if len(cadena) != 10:
        return False
    
    campos = cadena.split('/')
    # comprobar que contenga 2 barras como separador
    if len(campos) != 3:
        return False
    
    # que cada campo tenga la longitud que toca
    if not (len(campos[0]) == 2 and len(campos[1]) == 2 and len(campos[2]) == 4):
        return False
    
    # y comprobar que todos los campos sea digitos
    return campos[0].isdigit() and campos[1].isdigit() and campos[2].isdigit()

# la fecha es real
def es_data_real(d,m,a):
    '''
    Funcion que determina si tres enteros corresponden a un dia exitente
    in: 3 int
    out: boolean
    '''
    # comprobar que el año sea correcto
    if a <= 0:
        return False

    # comprobar que el mes sea correcto
    if not (m >= 1 and m <= 12):
        return False

    # comprobar que el dia sea correcto
    if not (d >= 1 and d <= dies_mes(m,a)):
        return False
    
    return True

#es año bisiesto
def es_any_trespas(año):
    '''
    Funcion que devuelve los dias del año
    in: 1 int (año)
    out: boolean
    '''
    # es año bisiesto o no
    return (año % 400 == 0) or (año % 4 == 0 and año % 100 != 0)

# dias del mes del año
def dies_mes(mes,año):
    '''
    Funcion que devuelve los dias del mes
    in: 2 int (mes,año)
    out: 1 int (dias del mes)
    '''
    DIAS_MES = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    dias = 0
    # compobar que sea mes del año
    if mes >= 1 and mes <= 12:
        dias = DIAS_MES[mes]
        # si es Febrero y año bisiesto
        if mes == 2 and es_any_trespas(año):
                return dias + 1
        else:
                return dias
        # si otro mes cualquiera
        return dias

# dia, mes y año
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

# el dia siguiente
def dia_següent(fecha_valida):
    '''
    Funcion que devuelve el siguiente dia de la fecha
    in: 1 str ( fecha(dd/mm/aaaa) )
    out: 1 str ( siguiente dia(dd/mm/aaaa) )
    '''
    d, m, a = get_data(fecha_valida)
    # sumemos un dia
    if d == dies_mes(m,a):
        d = 1
        m += 1
        if m == 13:
            m = 1
            a += 1
    else:
        d += 1
    
    # devolvel el dia siguiente
    return crea_data(d,m,a)

def crea_data(d,m,a):
    '''
    Funcion que crea una fecha en formato valido
    Input: 3 int
    Out: str (dd/mm/aaaa)
    '''
    return f'{d:02}/{m:02}/{a:04}'

# test driver
if __name__ == "__main":
    # test driver de es_data_valida
    if False:
        # Que el formato sea correcto
        print(es_data_valida('14/03/20'))
        print(es_data_valida('14/3/2021'))
        print(es_data_valida('14/03/2021'))
        print(es_data_valida('4/03/2021'))
        print(es_data_valida('14-03-2021'))
        print(es_data_valida('14-03-02021'))
        print(es_data_valida('1.4/03/2021'))
        print(es_data_valida('data valida'))
        print(es_data_valida('ab/12/abcd'))
        print(es_data_valida('12/12/-212'))
        print()

        # Que la fecha sea correcto
        # si el mes es correcto
        print(es_data_valida('14/13/2020'))
        print(es_data_valida('14/00/2020'))
        print(es_data_valida('14/03/-002'))
        print()
        # si el año es correcto
        print(es_data_valida('14/03/0000'))
        print(es_data_valida('14/03/2020'))
        print()
        # si el es año bisiesto
        print(es_data_valida('29/02/2020'))
        print(es_data_valida('29/02/2021'))
        print(es_data_valida('29/02/2000'))
        print(es_data_valida('29/02/2100'))
        print()
        # si el dia es correcto
        print(es_data_valida('31/01/2021'))
        print(es_data_valida('31/04/2021'))
        print(es_data_valida('32/07/2021'))
        print(es_data_valida('31/05/2021'))
        print(es_data_valida('00/03/2021'))
        print(es_data_valida('31/12/2021'))
        print()
    # test driver de get_data
    if False:
        print(get_data('19/03/2021'))
        print()
    # test driver de dia_següent
    if False:
        print(dia_següent('31/12/2020'))
        print(dia_següent('31/03/2020'))
        print(dia_següent('28/02/2020'))
        print()
    # test driver de crea_data
    if True:
        print(crea_data(3,5,2021))
        print(crea_data(33,5,2021))
        print()