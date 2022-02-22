import sys
import calendari

def dia_següent(fecha_valida):
    '''
    Funcion que devuelve el siguiente dia de la fecha
    in: 1 str ( fecha(dd/mm/aaaa) )
    out: 1 str ( siguiente dia(dd/mm/aaaa) )
    '''
    d, m, a = calendari.get_data(fecha_valida)
    # sumemos un dia
    if d == calendari.dies_mes(m,a):
        d = 1
        m += 1
        if m == 13:
            m = 1
            a += 1
    else:
        d += 1
    
    # devolvel el dia siguiente
    return calendari.crea_data(d,m,a)

print(dia_següent(sys.argv[1]))