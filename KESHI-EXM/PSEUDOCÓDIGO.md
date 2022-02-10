### Ejemplos de pseudocódigos

## Debajo de estas líneas encontrarás una serie de ejemplos de algoritmos escritos en pseudocódigo. Esto es con el objetivo de poder comprender mejor su estructura y lo relativamente sencillo que es su implementación.


# Pedir dos números enteros y mostrar 'Verdadero' si el primero es mayor

1. ALGORITMO Decir;

2. VAR

3. ENTERO x, z;

4. INICIO

5. ESCRIBIR("Ingresar dos números");

6. LEER( x, z );

7. SI( x > z )

8. ESCRIBIR("Verdadero");

9. FIN SI

10. FIN



# Leer tres números y deducir si se han introducido en orden creciente

1. ALGORITMO N32;

2. VAR

3. ENTERO a, b, c ;

4. INICIO

5. ESCRIBIR("Ingresar tres números");

6. LEER( a, b, c );

7. SI (a < b) AND (b < c)

8. ESCRIBIR("En orden ascendente");

9. SINO

10. ESCRIBIR("En orden descendente");

11. FIN SI

12. FIN




# Pedir dos valores y en caso de que no sean iguales indicar cuál es el mayor

1. ALGORITMO Leer;

2. VAR

3. ENTERO x, y;

4. INICIO

5. ESCRIBIR("Ingresar dos números");

6. LEER(x, y);

7. SI( x == y )

8. ESCRIBIR("Son iguales");

9. SINO

10. SI( x > y )

11. ESCRIBIR("x es mayor");

12. SINO

13. ESCRIBIR("y es mayor");

14. FIN SI

15. FIN_SI

16. FIN



# Pedir un número y mostrarlo por pantalla

1. ALGORITMO Mostrar;

2. VAR

3. ENTERO entrada;

4. INICIO

5. ESCRIBIR("Ingresar un número");

6. LEER( entrada );

7. ESCRIBIR( entrada );

8. FIN



# Pedir un número al usuario y mostrar el nombre del día al corresponde (1=lunes)

1. Usando CASO:

2. ALGORITMO DIA_CASO;

3. VAR

4. ENTERO d;

5. INICIO

6. ESCRIBIR("Ingresar un número del 1 al 7");

7. LEER( d );

8. SI (d >=1 ) AND (d <= 7)

9. EN_CASO_DE d HACER

10. a: ESCRIBIR("Lunes");

11. b: ESCRIBIR("Martes");

12. c: ESCRIBIR("Miércoles");

13. d: ESCRIBIR("Jueves");

14. e: ESCRIBIR("Viernes");

15. f: ESCRIBIR("Sábado");

16. g: ESCRIBIR("Domingo");

17. FIN CASO

18. SINO

19. ESCRIBIR("El valor ingresado no es válido");

20. FIN SI

21. FIN



# Usando PARA

1. ALGORITMO DIA_PARA;

2. VAR

3. ENTERO contador;

4. INICIO

5. PARA contador DESDE 1 HASTA 7

6. EN_CASO_DE contador HACER

7. a: ESCRIBIR("Lunes");

8. b: ESCRIBIR("Martes");

9. c: ESCRIBIR("Miércoles");

10. d: ESCRIBIR("Jueves");

11. e: ESCRIBIR("Viernes");

12. f: ESCRIBIR("Sábado");

13. g: ESCRIBIR("Domingo");

14. FIN CASO

15. FIN_PARA

16. FIN




# Pedir dos números y mostrar la suma de ambos

1. ALGORITMO Sumar;

2. VAR

3. ENTERO Numero1, Numero2, Resultado;

4. INICIO

5. ESCRIBIR("Ingresar dos números para sumar: ");

6. LEER(Numero1, Numero2);

7. Resultado <- Numero1 + Numero2;

8. ESCRIBIR("La suma es: ", Resultado);

9. FIN






# Algoritmo que muestra por pantalla el triple de un número real

1. ALGORITMO Multiplicar;

2. VAR

3. REAL a, y;

4. INICIO

5. ESCRIBIR("Ingresar un número");

6. LEER( a );

7. a <- a * 3;

8. ESCRIBIR(a);

9. FIN








# Algoritmo que pide un número y escribe su cuadrado

1. ALGORITMO Cuadrados_1;

2. VAR

3. ENTERO nNumero, nCuadrado;

4. INICIO

5. ESCRIBIR("Ingresar un número");

6. LEER( nNumero );

7. nCuadrado <- SQR(nNumero);

8. ESCRIBIR(nCuadrado);

9. FIN

Usando MIENTRAS

    ALGORITMO N53_Mientras;
    VAR
    ENTERO Contador;
    INICIO
    Contador <- 1;
    MIENTRAS( Contador <= 100 ) HACER
    ESCRIBIR( Contador );
    Contador <- Contador + 1;
    FIN MIENTRAS
    FIN

Usando REPETIR

    ALGORITMO N53_Repetir;
    VAR
    ENTERO Contador;
    INICIO
    Contador <- 0;
    REPETIR
    Contador <- Contador + 1;
    ESCRIBIR("Número actual: ", Contador);
    HASTA( Contador == 100 )
    FIN

Usando PARA

    ALGORITMO N53_Para;
    VAR
    ENTERO contador;
    INICIO
    PARA contador DESDE 1 HASTA 100
    ESCRIBIR( contador );
    FIN_PARA
    FIN









# Programa que permite calcular la suma de los 5 primeros números enteros positivos


Usando MIENTRAS

    ALGORITMO N55_Mientras;
    VAR
    ENTERO contador, suma;
    INICIO
    contador <- 1;
    suma <- 0;
    MIENTRAS( contador <= 5 ) HACER
    suma <- suma + contador;
    contador <- contador + 1;
    FIN MIENTRAS
    ESCRIBIR("La suma es: ", suma);
    FIN


Hombre escribiendo Pseudocódigo

Usando REPETIR

    ALGORITMO N55_Repetir;
    VAR
    ENTERO contador, suma;
    INICIO
    contador <- 0;
    suma <- 0;
    REPETIR
    contador <- contador + 1;
    suma <- suma + contador;
    HASTA( contador == 5 )
    ESCRIBIR("Resultado: ", suma);
    FIN

Usando PARA

    ALGORITMO N55_Para;
    VAR
    ENTERO contador;
    ENTERO suma <- 0;
    INICIO
    PARA contador DESDE 1 HASTA 5
    suma <- suma + contador;
    FIN_PARA
    ESCRIBIR("La suma es: ", suma);
    FIN












# Leer desde el teclado una serie de números hasta obtener uno inferior a 100

Usando MIENTRAS

    ALGORITMO N50;
    VAR
    ENTERO Numero;
    INICIO
    ESCRIBIR("Dime un número menor de 100");
    LEER( Numero );
    MIENTRAS( Numero >= 100 ) HACER
    ESCRIBIR("Dime un número menor de 100");
    LEER( Numero );
    FIN MIENTRAS
    ESCRIBIR("Ha introducido un número inferior a 100: ", Numero);
    FIN

Cálculos para pseudocódigo

Usando REPETIR

    ALGORITMO N50_2;
    VAR
    ENTERO Numero;
    INICIO
    ESCRIBIR("Ingresar un número menor de 100");
    LEER( Numero );
    REPETIR
    ESCRIBIR("Ingresar un número menor de 100");
    LEER(Numero);
    HASTA( Numero < 100 )
    ESCRIBIR("Se ingresó un número inferior a 100: ", Numero);
    FIN







# Pedir una contraseña utilizando REPETIR hasta que la clave sea 201, 784 ó 988

    ALGORITMO N64;
    VAR
    ENTERO Clave, Intentos;
    INICIO
    Intentos <- 0;
    REPETIR
    Intentos <- Intentos + 1;
    ESCRIBIR("Ingresar la clave: ");
    LEER(Clave);
    HASTA (Clave == 201) OR (Clave == 784) OR (Clave == 988) OR (Intentos == 3);
    SI (Intentos == 3) AND (Clave <> 201) AND (Clave <> <>) AND (Clave == 988)
    ESCRIBIR("Demasiados intentos");
    SINO
    ESCRIBIR("Clave correcta");
    FIN SI
    FIN





# Pedir 10 números al usuario, y mostrar cuántos de ellos han sido mayores de cero

    ALGORITMO ContarNumeros_Para;
    VAR
    ENTERO contador;
    ENTERO positivos <- 0;
    ENTERO numero;
    INICIO
    PARA contador DESDE 1 HASTA 10
    ESCRIBIR("Ingresar un número: ");
    LEER( numero );
    SI( numero > 0 )
    positivos <- positivos + 1;
    FIN SI
    FIN_PARA
    ESCRIBIR("Se introdujeron", positivos, " números mayores de cero");
    FIN

Hombre escribiendo pseudocódigo












# Mostrar los cinco primeros números pares

1. ALGORITMO Pares;

2. VAR

3. ENTERO contador;

4. INICIO

5. PARA contador DESDE 1 HASTA 10 INCREMENTO 2

6. ESCRIBIR( contador );

7. FIN_PARA

8. FIN
