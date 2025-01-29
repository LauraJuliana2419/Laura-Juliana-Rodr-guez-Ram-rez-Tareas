##Programación de computadores
##Autora Laura Juliana Rodríguez Ramírez 
##--------------------------------------------------------------------------
##1.Programa que determine si en una lista no existen elementos repetidos
print("--------------------------------------------------------")
print("Programa para determinar si exiten elementos repetidos en una lista\n")
Lista = []
for i in range(1,5):
 Nombres = (input("Por favor ingrese un nombre para la lista de datos:\n"))
##Uso de metodo .append(para agregar un nuevo elemento a la lista) 
##Y el metodo .lower(para que todos los nombres esten en minusculas)
 Lista.append(Nombres.lower())
def determinar_repetidos(lista):
##Uso del metodo set(para guardar valores no repetidos)
    elementos = set()
##Lista para guardar los elementos repetidos
    repetidos = []
    for rep in lista:
        if rep in elementos:
            repetidos.append(rep)
        else:
##Uso del metodo add(para añadir un nuevo dato,que no este)
            elementos.add(rep)
##Uso del metodo len(devuelve la longitud de los elementos repetidos)
##si es mayor a 0 hay repetidos 
    if len(repetidos)>0:
       return "Existen elementos repetidos en la lista y son: ",repetidos
    else:
        return "No existen elementos repetidos en la lista: ",lista
print(determinar_repetidos(Lista))
print("--------------------------------------------------------")
##2.Programa que determine si un elemento es palindrome 
print("Programa para determinar si un elemento de la lista es palíndrome\n")
Lista_1 = []
for i in range(1,5):
 Nombres_1 = (input("Por favor ingrese un nombre para la lista de datos:\n"))
 Lista_1.append(Nombres_1.lower())
def determinar_palíndromes(lista_1):
    palindromes = []
    for dato in lista_1:
##Se compara el nombre del dato original con
##el dato en orden inverso para saber si es 
##palindrome
        if dato == dato[::-1]:
##Si es palindrome se agrega a esa lista
            palindromes.append(dato)
##Si la longitud(la cantidad de palindromes)
##es mayor a 0 hay palindromes
    if len(palindromes)>0:
       return "Existen elementos palíndromes en la lista y estos son: ",palindromes
    else:
        return "No existen elementos palíndromes en la lista: \n ",Lista_1
print(determinar_palíndromes(Lista_1))
##3.Programa para determinar si en una lista se encuentra una cadena 
##de caracteres con dos o mas vocales
print("--------------------------------------------------------")
print("Programa para determinar si en una lista se encuentra una cadena de caracteres con dos o mas vocales\n")
cadena_caracteres=input("Por favor diga que mensaje de texto desea enviar:\n")
def vocales (cadena):
    vocales= "aeiou"
    contar_vocales= 0
    for caracteres in cadena.lower():
##Se comprueba si el utlimo caracter iterado contiene 
##una de las vocales
        if caracteres in vocales:
##Si es una vocal se incrementa en 1 
            contar_vocales += 1 
##Se comprueba que hayan 2 o mas vocales
    if contar_vocales>= 2:
        return "En la cadena",cadena, "existen",contar_vocales,"vocales"
    else:
        return ("En la cadena",cadena, "no existen 2 o mas vocales")
print(vocales(cadena_caracteres))
##4.Programa que determina si una lista es palíndrome
##(Es palíndrome si el elemento en la posición i 
##es el mismo en la posicion n-1-i con n la longitud de la lista)
print("--------------------------------------------------------")
print("Programa para determinar si una lista es palíndrome\n")
Lista_2 = []
for i in range(1,7):
 Acciones = (input("Por favor ingrese una acción para la lista de datos:\n"))
 Lista_2.append(Acciones.lower())
def determinar_listas_palíndromes(lista_2):
##Obtenemos la longitud de la lista para determinar la
##posicion simetrica
    n = len(lista_2)
##Usamos el rango n//2(recorre la mitad) para que solo se puedan
##comparar los elementos de ambas mitades(primero y ultimo)
##(segundo y penultimo)(los de la mitad juntos)
    for i in range(n//2):
##Si los elementos no coinciden en las posiciones simetricas
##que se plantean en el if no es palindrome
        if lista_2[i] != lista_2[n-1-i]:
            return "La lista no es palíndrome",lista_2
    return "La lista es palíndrome",lista_2

print(determinar_listas_palíndromes(Lista_2))
##Problemas planteados por Blackbox Ai 
##5.)Ejercicio 1 : Verificar si una lista es simétrica
##Descripción: Desarrollar un programa que determine si una lista es simétrica.
##Una lista es simétrica si los elementos en la posición i son iguales a 
##los elementos en la posición n-1-i, pero en lugar de solo verificar, 
##el programa debe devolver una lista de los elementos que son simétricos.
##Variación: Además de verificar la simetría, el programa debe contar cuántos 
##pares de elementos simétricos hay en la lista y devolver ese conteo.
print("--------------------------------------------------------")
print("Programa que determina si una lista es simetrica\n")
Lista_3 = []
for i in range(1,11):
 Colores = (input("Por favor ingrese un color para la lista de datos:\n"))
 Lista_3.append(Colores.lower())
def lista_simetrica(lista_3):
    s = len(lista_3)
##Se crea una variable que guarde los datos simetricos
    datos_simetricos=[]
##Se crea un contador para que los cuente desde 0
    contar_simetricos=0
    for i in range(s//2):
        if lista_3[i] == lista_3[s-1-i]:
##Si cumple la condicion se agrega a la lista
            datos_simetricos.append(lista_3[i])
##Se incrementa el contador para llevar la cuenta de los simetricos
            contar_simetricos += 1
    if contar_simetricos>0:
            return "La lista es simetrica y hay",contar_simetricos,"datos pares simetricos"
    return "La lista no es simétrica"

print(lista_simetrica(Lista_3))
##6.)Ejercicio 2: Desarrollar un programa que determine si una cadena de caracteres 
##en una lista es un anagrama de otra cadena. Si existe un par de anagramas,
##debe imprimir ambas cadenas; si no existe, debe imprimir "No hay anagramas".
print("--------------------------------------------------------")
print("Programa para determinar si una cadena es un anagrama de otra\n")
Lista_4 = []
for i in range(1,5):
 Palabras = (input("Por favor ingrese una palabra para la lista de datos:\n"))
 Lista_4.append(Palabras.lower())
def determinar_anagramas(lista_4):
    anagramas = []
    for i in range(len(lista_4)):
##Se crea un bucle anidado que recorra los datos,a partir el actual
##sin incluirlo,comparando i con todas las j 
        for j in range(i+1,len(lista_4)):
##Se hace uso del metodo sorted(que devuelve los datos ordenados)
##no modifica la original sino que hace una copia ordenada
            if sorted(lista_4[i]) == sorted(lista_4[j]):
##Si al ser orgranizados son iguales se agregaran a la lista
##de anagramas en forma de tupla para que no sean modificados
##y se muestre el anagrama de i y de j
                anagramas.append((lista_4[i],lista_4[j]))
    if anagramas:
        return "Existen anagramas en la lista y estos son: ",anagramas
    else:
        return "No existen anagramas en la lista:",lista_4
print(determinar_anagramas(Lista_4))
##7.)Ejercicio 3: Desarrollar un programa que determine si en una lista se encuentra
## una cadena de caracteres que contenga al menos tres consonantes. Si la cadena existe
##debe imprimirla; si no existe, debe imprimir "No existe"
print("--------------------------------------------------------")
print("Programa para determinar si en una lista se encuentra una cadena de caracteres con al menos 3 consonantes\n")
cadena_caracteres_1=input("Por favor diga que mensaje de texto desea enviar:\n")
def consonantes (cadena_1):
    consonantes= "bcdfghjklmnñpqrstvwxyz"
    contar_consonantes= 0
##Se inicia un for que recorra cada caracter en minuscula 
    for caracteres_1 in cadena_1.lower():
##Se verifica si el caracter actual esta en las consonates y
##si esta se guarda en el contador
        if caracteres_1 in consonantes:
            contar_consonantes += 1 
    if contar_consonantes>= 3:
        return "En la cadena",cadena_1, "existen",contar_consonantes,"consonantes"
    else:
        return ("En la cadena",cadena_1, "no existen 3 o mas consonantes")
print(consonantes(cadena_caracteres_1))
##8.)Ejercicio 4: Buscar cadenas con al menos una cifra
##Descripción: Desarrollar un programa que determine si hay cadenas 
##en una lista que contengan al menos una cifra. Si existen, debe 
##imprimir todas las cadenas que cumplen con esta condición; si no,
## debe imprimir "No existen cadenas con cifras".
##Variación:El programa debe devolver una lista de 
##las cadenas que contienen al menos una cifra y también contar cuántas 
##cadenas cumplen con esta condición.
print("--------------------------------------------------------")
print("Programa para determinar si en una lista se encuentra una cadena de caracteres con al menos 1 cifra\n")
Lista_5 = []
for i in range(1,5):
 Cifras = input("Por favor ingrese su nombre de usuario:\n")
 Lista_5.append(Cifras.lower())
def cifras (lista_5):
    cifras= []
##Se crea un for que itera sobre cada dato en la lista y a cada dato 
##lo asigna a cadena_2
    for cadena_2 in lista_5:
##Se inicializa la variable con False
        tiene_cifras=False
        for caracter in cadena_2:
##Se utiliza un for que recorre cada caracter del
##dato actual
            if caracter.isdigit():
##Se utiliza el metodo isdigit(Para revisar si el caracter
##actual es un numeros,si es asi devuelve True
                tiene_cifras=True
##Si es asi lo va a agregar a la lista cifras  
                break
##Se rompe recien encuentre el primer numero para
##no revisar mas pues ya se sabe que hay una cifra
        if tiene_cifras:
            cifras.append(cadena_2)
    if cifras:
##El len devuelve la cantidad de cadenas con cifras encontradas
        return "En la cadena",cifras, "existen",len(cifras),"cifras"
    else:
        return ("No existen cadenas que contengan cifras")
print(cifras(Lista_5))