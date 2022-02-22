"""
def escriuteText(fitxer,linies):
    '''
    '''
    fitxer = open(fitxer,'w')
    fitxer.writelines(linies)
    return

def afegirText(linies,text):
    '''
    '''
    linies[-1] = linies[-1] + '\n'
    for linia in text:
        linies.append(linia)
    linies = ''.join(linies)
    return

def actualitzarFitxer(fitxer,text):
    '''
    '''
    n_fitxer = open(fitxer,'r')
    linies = n_fitxer.readlines()
    afegirText(linies,text)
    escriuteText(fitxer,linies)

actualitzarFitxer('texto.txt',('hasta\n','luego'))
"""

# MODULO DE CLASIFICACION DE LOS EQUIPOS DE FUTBOL
EQUIPS = 'equips.txt'
RESULTATS = 'resultats.txt'
CLASSIFICACIO = 'classificació.txt'

def dicEquip(fitxer_equips):
    '''
    '''
    dic = {}
    fitxer_equips = open(fitxer_equips,'r')
    for linia in fitxer_equips.readlines():
        linia = linia.strip()
        dic[linia.split()[0]] = linia.split()[1]
    fitxer_equips.close()
    return dic

def mostraClassificacio(fitxer_classificacio):
    '''
    Funcion que muestra la classificacio actual
    con el nombre de los equipos de futbol y su 
    puntuaje.
    in: str (fichero de classificació.txt)
    out: none
    '''
    fitxer_classificacio = open(fitxer_classificacio,'r') #abrir el fichero
    # bucle: mostra equipo y classificacion
    for linea in fitxer_classificacio.readlines():
        linea = linea.strip() #por cada linea
        
        # sacar los nombre y sus puntos
        nombre, puntos = linea.split()[0], linea.split()[1]
        
        fitxer_classificacio.close() #cerrar el fichero
        # mostrar clasificacion
        print(f'{dicEquip(EQUIPS).get(nombre)}: {puntos}')

def dicDatesPartits(fitxer_resultats):
    '''
    '''
    dic = {}
    fitxer_resultats = open(fitxer_resultats,'r')
    for linia in fitxer_resultats.readlines():
        linia = linia.strip()
        dic[linia.split()[0]] = linia.split()[1:]
    fitxer_resultats.close()
    return dic

def mostraPartits(data_partit):
    '''
    '''
    partidos = dicDatesPartits(RESULTATS)
    for fecha,partido in partidos.items():
        if fecha == data_partit:
            partido = ' '.join(partido)
            print(f'{fecha} {partido}')

def ordernaPartits(fitxer_resultats):
    '''
    '''
    dic = {}
    fechas_partidos = dicDatesPartits(fitxer_resultats)
    fechas_ordenadas = sorted(fechas_partidos, reverse=True)
    for fecha in fechas_ordenadas:
        dic[fecha] = fechas_partidos.get(fecha)
    return dic

def actualitzarResultats(fitxer_resultats):
    '''
    '''
    linies = []
    partidos_ordenados = ordernaPartits(fitxer_resultats)

    fitxer_resultats = open(fitxer_resultats,'w')  
    for fecha,partido in partidos_ordenados.items():
        partido = ' '.join(partido)
        linia = f'{fecha} {partido}\n'
        linies.append(linia)
    
    fitxer_resultats.writelines(linies)
    fitxer_resultats.close()

#print(dicEquip(EQUIPS))
#mostraClassificacio(CLASSIFICACIO)
#print(dicDatesPartits(RESULTATS))
#mostraPartits('18/01/2021')
#print(ordernaPartits(RESULTATS))
actualitzarResultats(RESULTATS)
