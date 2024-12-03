
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

#1. Convertir a mayúsculas

texto = "hola mundo"
mayusculas = texto.upper()
print(mayusculas)

#2. Convertir a minúsculas

texto = "Hola Mundo"
minusculas = texto.lower()
print(minusculas)

#3. Primera letra en mayúscula (Capitalizar)

texto = "hola mundo"
capitalizando = texto.capitalize()
print(capitalizando)

#4. Cada palabra con mayúscula inicial (Título)

texto = "hola mundo"
titulo = texto.title()
print(titulo)

#5. Invertir mayúsculas y minúsculas

texto = "Hola Mundo"
invertido = texto.swapcase()
print(invertido)

#6. Convertir cadenas según mayúsculas y minúsculas (Comprobar)
#Verificar si una cadena está en mayúsculas

texto = "HOLA"
print(texto.isupper())

#Verificar si una cadena está en minúsculas:

texto = "hola"
print(texto.islower())

#Identificar caracteres

#1. Comprobar si un carácter está en una cadena

texto = "Hola Mundo"
print('a' in texto)  # Resultado: True
print('z' in texto)  # Resultado: False

#2. Encontrar la posición de un carácter

texto = "Hola Mundo"
posicion = texto.find('M')
print(posicion)  # Resultado: 5

#Método index(): Similar a find(), pero genera un error si el carácter no está presente.

texto = "Hola Mundo"
posicion = texto.index('M')
print(posicion)  # Resultado: 5

#3. Contar la frecuencia de un carácter

texto = "Hola Mundo"
conteo = texto.count('o')
print(conteo)  # Resultado: 2

#4. Identificar el tipo de carácter

#Comprobar si es una letra:

caracter = 'H'
print(caracter.isalpha())  # Resultado: True

#Comprobar si es un dígito:

caracter = '5'
print(caracter.isdigit())  # Resultado: True

#Comprobar si es un espacio en blanco:

caracter = ' '
print(caracter.isspace())  # Resultado: True















