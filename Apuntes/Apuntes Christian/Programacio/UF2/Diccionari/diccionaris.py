# !/usr/bin/python
#  -*- coding:utf-8 -*-
# Autor:

#Descripcio: MODUL DICCIONARIS



def crea_dicc_freq_patro(frase,carac_a_buscar):
	"""Funcio que rep per parametre una seqüència qualsevol(str/list) i una
	 llista de caracters/elements a buscar i et compta les repeticions
	Entrada: Una seqüència qualsevol(string/list) i una altra (string/list)
	amb els caràcters/elements  a buscar 
	Sortida: Les claus amb els seus respectius valorsnumérics
	"""
	# crear un dicionario
	diccionario = {}

	# bucle: pasar por cada caracter
	for car in frase:
		
	
def frequencies(seq):
	"""Funcio que compta la frequencia dels caràcters/elements que passem
	i ens retorna la quantitat de vegades que es repeteix cada paraula o caracter
	Entrada: cadena o llista
	Sortida: claus amb els seus respectius valors numérics
	"""
	

def diccionari_maco(dic):
	""" Funció que ens mostra un diccionari de manera 'maca'. És a dir, a cada 
	línia ens mostra un element (clau, valor) així:
	clau: clau	valor:valor
	Input: diccionari
	Output: res  (la pròpia funció printa)
	"""




	
###################################################################
#TEST DRIVER
if __name__ == "__main__" :		
	if True:
		print crea_dicc_freq_patro(['hola','com','hola','estas','tu','jo','be','i','tu'],['hola','tu','be'])
		print crea_dicc_freq_patro('hola com estas jo be i tu','aeiou') 
		
	if True:
		print frequencies('hola com estas jo be i tu')
		print frequencies(['hola','com','estas','jo','be','i','tu','jo','be','hola'])
	
	
