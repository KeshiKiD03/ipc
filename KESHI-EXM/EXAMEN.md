# EXAMEN

# EXAMEN 02: 

## Processos: 

* Volem fer un **SERVIDOR** que **REBI FITXERS** **ENVIATS** des d'un **PROGRAMA CLIENT** i els **GUARDI** en el **DISC**. 

* El **servidor acceptarà** la **connexió** d'un **sol client al mateix temps**, després d'atendre'l acceptarà la **connexió** d'un **altre** i així succesivament fins que rebi un **senyal** per a **finalitzar**.

* Per simplificar només es transmetran **fitxers de text**. 

* Servidor: **prog_servidor Client**: prog_cliente -H adreça_servidor -p port_servidor -f fitxer1 -f fitxer2 ...



### Servidor FTP

* File Transfer Protocol

* Envío y obtención de ARCHIVOS entre 2 EQUIPOS REMOTOS.

* Usan el puerto 20 o 21

## VENTAJAS

    Realiza una conexión rápida con el servidor.
    Es ideal para subir muchos archivos o pocos, según se necesite.
    Es multiplataforma, funciona en cualquier sistema operativo.
    Permite subir y bajar archivos bi-direccionalmente.
    Soporta conexiones encriptadas con certificados SSL
    No necesitas saber comandos ni usar la terminal, tiene clientes gráficos.
    No se requiere de conocimientos técnicos para usarlo.


## DESVENTAJAS

Si no hay SSL de por medio, los datos de usuario y contraseña, la información que sube o baja se envía sin encriptación..

No permite la automatización de diferentes procesos como lo permiten otros protocolos más modernos, como por ejemplo conectar a través de un servidor SSH.

Es un protocolo viejo, que si bien ha recibido actualizaciones, no se ha adaptado al desarrollo web moderno.

No permite paralelizar las descargas o subidas de archivos, estos deben hacerse uno a uno.

No permite resumir las descargas o subida de archivos, pueden quedar corruptos los archivos si hay errores en la red.





## CLIENTE

1. Cliente se quiere conectar al SERVIDOR.

s.connect((HOST,PORT))


## SERVIDOR

1. El Servidor está escuchando conexiones 1 a 1 (One By One). El Servidor acepta la conexión del Cliente.

conn, addr = s.accept()
