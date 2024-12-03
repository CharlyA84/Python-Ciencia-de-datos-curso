
#Busquedas 
#Comprobar si una cadena de texto empieza o termina por algun subcadena


from pickletools import string1


Texto = "Bienvenido al curso de Python"
print(Texto.startswith(("b")))

Palabra = "hola, como estas?"
if Palabra.startswith("hola"):
    print("La cadena comienza 'hola'")

ozuna = "Buenvenidos al curso de Python"
print(ozuna.endswith(("n")))

#Encontrar la primera ocurrencia de alguna subcadena


beto = "Bienvenido al curso de Python"
print(beto.find(("b"))) 


print(beto.count('i'))


#Remplazar elementos 
#podemos usar la funcion replace() indicando la subcadena a reemplazar ,la subcadena de reemplazo y cuantas intancias se deben reemplazar, si no se especifica este ultimo argumento
#, la sustitucion se hara en todas las intancias encontradas
proverb = 'Quien mal anda mal acaba'
print(proverb.replace('mal' , 'bien'))

print(proverb.replace('mal' , 'bien' , 1))

#Mayusculas y minusculas 
#Python nos permite realiza variaciones en los caracteres de una cadena de texto para pasarlos a mayusculas 
#y/o minusculas.Veamos las distintas opciones disponibles

#1. Convertir a may�sculas

texto = "hola mundo"
mayusculas = texto.upper()
print(mayusculas)

#2. Convertir a min�sculas

texto = "Hola Mundo"
minusculas = texto.lower()
print(minusculas)

#3. Primera letra en may�scula (Capitalizar)

texto = "hola mundo"
capitalizando = texto.capitalize()
print(capitalizando)

#4. Cada palabra con may�scula inicial (T�tulo)

texto = "hola mundo"
titulo = texto.title()
print(titulo)

#5. Invertir may�sculas y min�sculas

texto = "Hola Mundo"
invertido = texto.swapcase()
print(invertido)

#6. Convertir cadenas seg�n may�sculas y min�sculas (Comprobar)
#Verificar si una cadena est� en may�sculas

texto = "HOLA"
print(texto.isupper())

#Verificar si una cadena est� en min�sculas:

texto = "hola"
print(texto.islower())

#Identificar caracteres

#1. Comprobar si un car�cter est� en una cadena

texto = "Hola Mundo"
print('a' in texto)  # Resultado: True
print('z' in texto)  # Resultado: False

#2. Encontrar la posici�n de un car�cter

texto = "Hola Mundo"
posicion = texto.find('M')
print(posicion)  # Resultado: 5

#M�todo index(): Similar a find(), pero genera un error si el car�cter no est� presente.

texto = "Hola Mundo"
posicion = texto.index('M')
print(posicion)  # Resultado: 5

#3. Contar la frecuencia de un car�cter

texto = "Hola Mundo"
conteo = texto.count('o')
print(conteo)  # Resultado: 2

#4. Identificar el tipo de car�cter

#Comprobar si es una letra:

caracter = 'H'
print(caracter.isalpha())  # Resultado: True

#Comprobar si es un d�gito:

caracter = '5'
print(caracter.isdigit())  # Resultado: True

#Comprobar si es un espacio en blanco:

caracter = ' '
print(caracter.isspace())  # Resultado: True















