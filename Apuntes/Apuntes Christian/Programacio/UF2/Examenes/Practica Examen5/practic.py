# 4.1
# n_primers.py
'''
# Programa
import funcions_primers
import sys

# PROGRAMA PRINCIPAL
# llegir el nombre de primers que volem
quant_primers = int(sys.argv[1])
primer = 2	#el primer primer és el dos

# bucle (hem de repetir quant_primers vegades)
for i in range(0, quant_primers):
	#el printem
	print primer
	#busquem el següent primer
	primer = funcions_primers.seguent_primer(primer)
'''

# 4.2
'''
# Programa
import funcions_primers
import sys

# CONTROL DE ERRORES
# si tienes no tienen argumentos
if not (len(sys.argv[1:]) == 1)

# si no es un digito

# si no es mayor de 0

# si es un float y no un enter

# PROGRAMA PRINCIPAL
# llegir el nombre de primers que volem
quant_primers = int()
primer = 2	#el primer primer és el dos

# bucle (hem de repetir quant_primers vegades)
for i in range(0, quant_primers):
	#el printem
	print primer
	#busquem el següent primer
	primer = funcions_primers.seguent_primer(primer)
'''

# 