def es_data_valida(cad):
    '''
    Funcion que determina si una fecha es valida (dd/mm/aaaa)
    Input: cadena cualquiera
    Output: boolean
    '''
    # Comprobar que el formato es correcto
    if not es_data_format_correcte(cad):
        return False

    # calcular dia, mes y año
    (d, m, a) = get_data(cad)

    # Comprobar que los enteros de la fecha son correctos
    return es_data_real(d,m,a)

def es_data_format_correcte(cadena):
    '''
    Funcion que determina si una cadena cualquiera tiene formato dd/mm/aaaa,
    amb dd, mm i aaaa nombres enteros positivos
    Input: cadena
    Outut: boolean
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

def es_data_real(dia,mes,año):
    '''
    Funcion que determina si tres enteros corresponden a un dia que existe.
    Consideramos que los años validos solo son los postivos
    Input: int,int,int
    Output: boolean
    '''
    # comprobar que el año sea correcto
    if año <= 0:
        return False

    # comprobar que el mes sea correcto
    if not (mes >= 1 and mes <= 12):
        return False

    # comprobar que el dia sea correcto
    if not (dia >= 1 and dia <= dies_mes(mes,año)):
        return False
    
    return True

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
        if mes == 2 and es_año_bisiesto(año):
                return dias + 1
        else:
                return dias
        # si otro mes cualquiera
        return dias

def es_año_bisiesto(año):
    '''
    Funcion que devuelve los dias del año
    in: 1 int (año)
    out: 1 int (dias del año)
    '''
    # es año bisiesto o no
    return (año % 400 == 0) or (año % 4 == 0 and año % 100 != 0)

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

# TEST DRIVER -- es_data_valida
if __name__ == "__main__":
    print('test driver es_data_valida:')
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