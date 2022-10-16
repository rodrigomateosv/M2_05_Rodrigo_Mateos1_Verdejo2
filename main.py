
#Ejercicio 4
paises = ["España", "Alemania", "Francia", "Suiza", "Dinamarca"]
print(paises)
#Elementos y longitud de los elementos de la lista
print(paises[0], len(paises[0]))
print(paises[1], len(paises[1]))
print(paises[2], len(paises[2]))
print(paises[3], len(paises[3]))
print(paises[4], len(paises[4]))
#Elemento con mayor numero de caracteres
print(f"El elemento con mas caracteres es: ", paises[4])
#El metodo .sort() ordena las listas alfabeticamente o si son numeros en orden normal(1,2,3...,n). Como queremos ordenar la lista por el numero de caracteres que contiene cada elemento (en este caso el numero de letras de cada palabra) utilizamos .sort(key=len) para ordenar la lista de paises por longitud.
#Palabras ordenadas de menor a mayor longitud
paises.sort(key=len)
print(paises)
#Palabras ordenadas de mayor a menor longitud
paises.sort(key=len, reverse=True)
print(paises)

print("\n")
#Ejercicio 3
#Creamos una variable contador = 0. Despues, dentro de un bucle while escribimos el input para escribir la frase. Dentro del while, creamos un condicional, en el que si en la frase aparece una "a" el contador sumara una "a" mas, y si se pulsa el "." termina el condicional y el while, y se imprime el resultado de la suma de letras "a"
contador = 0
while True:
  frase = input("Introduce tu texto: ")
  if frase == "a":
    contador = contador + 1
  elif frase == ".":
     break
        
printf(f"En el texto aparecen {contador} letras a")

printf("\n")




scanf

#Ejercicio 2
#Creo una lista vacia, en la que voy añadiendo las variables que quiera(en este caso 3). Luego, en un condicional declaro las tres condiciones que me pide el ejercio, pero en este caso utilizando los elementos de una lista.
numeros = list()
A = numeros.append(input("Añade un numero: "))
A = numeros.append(input("Añade un numero: "))
A = numeros.append(input("Añade un numero: "))
if numeros[0] == 0:
    print("Error")
elif numeros[0] < numeros[1] < numeros[2]:
    print("Estan en orden ascendente")
else:
    print("No estan en orden ascendente")

print("\n")

#Ejercicio 1
#Creo tres variables. Luego, dentro de un condicional declaro las tres condiciones que me pide el ejercicio. La primera si el num1 == 0 da error, si estan en orden ascendente (num1<num2<num3) o si no lo estan.
num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce un numero: "))
num3 = int(input("Introduce un numero: "))
do while num1 == 0:
    print("Error")
elif num1 < num2 < num3:
    print("Estan en orden ascendente")
else:
    print("No estan en orden ascendente")