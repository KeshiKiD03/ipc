#!/usr/bin/python
#-*- coding: utf-8-*-

# Autor: Cristian Condolo
# Fecha: curs 2020-21

# Versión con juego de pruebas completo

# Descripción:
'''
Modulo para trabajar con el timestamp.
Un timestamp es una cadena del tipo:
dd/mm/aaaa  HH:MM:SS
Donde dd, mm y aaaa son enteros que corresponen a un dia, mes y año de
una fecha real. Y HH, MM y SS son enteros que corresponen a una hora,
minuto y segundo.
'''
import modul_calendari
import modul_hora_rellotge	
	
def get_data(timest):
	'''
	Función que dada un timestamp correcto extrae la parte corresponiente 
	a la fecha. Sobre esta fecha podremos utilizar get_data etc..
	in: str (timestamp vàlid)
	out: str (fecha vàlida)
	'''
	# devolvemos la parte la fecha del timestamp
	return timest.split()[0]
	
def get_hora(timest):
	'''
	Función que dada un timestamp correcto extrae la parte corresponiente
	a la hora de reloj (hh:mm:ss).
	in: str (timestamp vàlido)
	out: str (hora de reloj vàlida)
	'''
	# devuelve la hora del timestamp
	return timest.split()[1]
	
def crea_timestamp(data, hora):
	'''
	Función que crea un timestamp en formato vàlido
	in: str, str ( data vàlida, hora_rellotge vàlida)
	out: str (data en format correcte)
	'''
	# delvolver la fecha y hora juntas
	return f'{data} {hora}'
	
def normalitza_segons(s):
	'''
	Función que dada una cantidad de segundos la transforma en una hora de reloj.
	Si pasa de las 24 horas, vuelve a empezar
	in: int (segundos, >= 0)
	out: hora de reloj correcta
	'''
	# normalizar la hora
	segundos = s % 60
	m = s // 60
	minutos = m % 60
	horas = (m // 60) % 24
	# devolver la hora
	return modul_hora_rellotge.crea_hora(horas, minutos, segundos)
	
def sumaTimestamp(timest, hora):
	'''
	Función que dada un timestamp le añadimos la hora de reloj
	in: str, str (timestamp, hora de reloj vàlida)
	out: str (timestamp)
	'''
	# separar la fecha y la hora del timestamp
	hora_t = get_hora(timest)
	fecha_t = get_data(timest)
	
	# separamos la hora, minutos y segundos del timestamp y la
	# hora de reloj
	h_t, m_t, s_t = modul_hora_rellotge.get_hora(hora_t)
	h, m, s = modul_hora_rellotge.get_hora(hora)
	
	segs_totals = modul_hora_rellotge.hora_a_segons(h + h_t, m + m_t, s + s_t) #segundos de la hora de reloj
	segs_por_dia = modul_hora_rellotge.hora_a_segons(24, 0, 0) # segundo de un dia
	# si ha pasado un dia, normalizar	
	if segs_totals > segs_por_dia:
		fecha_t = modul_calendari.dia_seguent(fecha_t)
		segs_totals = segs_totals % segs_por_dia
		
	# normalizar los segundos totales
	hora_nueva = normalitza_segons(segs_totals)
	
	# crear el timestamp
	return crea_timestamp(fecha_t, hora_nueva)
	
# TEST DRIVERS
if __name__ == '__main__' :
	# test driver de get_data y get_hora
	if True:
		print(get_data('01/01/2000 20:20:23'))
		print(get_hora('01/01/2000 20:20:23'))
		print()
	# test driver de crea_timestamp	
	if True:
		print(crea_timestamp('01/01/2000', '20:20:23'))
	# test driver de normalitza_segons
	if True:
		print(normalitza_segons(3663))
		print(normalitza_segons(3000000))
		print(normalitza_segons(864061))
		print(normalitza_segons(2 * 864000))
	# test driver de sumaTimestamp
	if True:
		print(sumaTimestamp('01/01/2000 20:20:23', '01:02:03'))
		print(sumaTimestamp('01/01/2000 20:20:23', '05:00:00'))