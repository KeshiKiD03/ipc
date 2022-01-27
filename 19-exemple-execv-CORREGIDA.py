# /usr/bin/python
#-*- coding: utf-8-*-
#
# exemple-execv.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,os
# ------------------------------------------------
print("Hola, començament del programa principal")
print("PID pare: ", os.getpid())

pid=os.fork()
if pid !=0:
  print("Programa Pare", os.getpid(), pid)
  sys.exit(0)

#-------------------------------------------------
print("Programa fill", os.getpid(), pid)
#os.execv("/usr/bin/ls",["/usr/bin/ls","-ls","/"])  # 'v' ACCEPTA llistes i tuples
#os.execl("/usr/bin/ls","/usr/bin/ls","-ls","/") # 'l' NO ACCEPTA llistes i tuples, només li podem passar paràmetres fixes.
#os.execlp("ls","ls","-ls","/") # 'l' hem de passar-li els arguments literals, 'p' buscarà ell el PATH fins l'executable (no ens cal posar-li la ruta absoluta (/usr/bin/ls))
#os.execvp("uname",["uname", "-a"])  # Amb 'p' buscarà l'executable 'uname' i executarà l'ordre '-a'
#os.execv("/bin/bash",["/bin/bash", "show.sh"]) # executem el programa 'show.sh'
#os.execle("/bin/bash", "/bin/bash", "show.sh", {"nom":"joan", "edat":"25"})   # 'e' li passem variables d'entorn (com a diccionari)
#-------------------------------------------------
print("Hasta lugo lucas!")   # Mai és veurà!!!!!
sys.exit(0)


"""

## NOMBRE DEL PROGRAMA + SINTAXIS

**19-exemple-execv.py**

  Ídem anterior però ara el programa fill execula un “ls -la /”. Executa un nou 
  procés carregat amb execv. Aprofitar per veure les diferents variants de *exec*.
  Provar cada un dels casos.

# ----------------------------------------------

## Explicación

**19-exemple-execv.py**

  Ídem anterior però ara el programa fill execula un “ls -la /”. Executa un nou 
  procés carregat amb execv. Aprofitar per veure les diferents variants de *exec*.
  Provar cada un dels casos.


# ----------------------------------------------

## Metodología

1. execv --> v es la versió.

2. El propio código que se está ejecutando, pasa a convertirse al programa que se le ha pedido.

3. El propio proceso se convierte en un nuevo programa.

4. execv ejecuta el proceso. Y nunca ejecuta el último. Se autosustituye.

5. Lanza un subproceso con un programa que nosotros queramos.

6. Execv --> El programa que le queremos pasar en formato STRING y una LISTA y un elemento [0] --> Nombre del programa

7. El execv es inmediato. Asegurarse de tener grabado. 

8. execl --> 

9. execv --> Es inmediato, substituye el propio codigo.

10. execp --> No hace especificar la ruta absoluta, y la l es hardcode.

11. Las listas son dinámicas. 

P o E --> Rutas absolutas o simplemente con el nombre. No utiliza el path, usa una ruta relativa.

12. Mappiing = Diccionario.

13. La E usa Diccionarios. Hereda las variables.


#os.execle("/bin/bash", "/bin/bash", "show.sh", {"nom":"joan", "edat":"25"})   # 'e' li passem variables d'entorn (com a diccionari)

1. El primer argumento es /bin/bash.

2. El segundo argumento es /bin/bash

3. El programa a ejecutar es show.sh

4. Pasar la estructura de datos que es un diccionario. Pasarle un diccionario, Por variables de entorno en show.sh


#! /bin/bash
# Programa lligat amb el programa 19-exemple-execv.py

echo "nom: $nom"
echo "edat: $edat"



15.

16.

17.

18.

19.

20.







"""

