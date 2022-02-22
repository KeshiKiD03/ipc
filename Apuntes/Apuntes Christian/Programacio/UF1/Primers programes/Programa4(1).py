# Programa que agarra segundos y los normaliza con el formato mm:ss
seg = int(input('Segundos: '))

horas = seg // 3600
seg = seg % 3600
minutos = seg // 60
segundos = seg % 60

print(horas, ":", minutos, ":", segundos)
