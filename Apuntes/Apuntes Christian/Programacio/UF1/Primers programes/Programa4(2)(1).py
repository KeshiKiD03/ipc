# Programa que normalice los segundos
segundos = int(input())

minutos = segundos // 60
segundos_f = segundos % 60
horas_f = minutos // 60
minutos_f = minutos % 60

print(f'{horas_f}:{minutos_f}:{segundos_f}')
