#cadena de texto (strings) ParteI
#Strings=Secuenias de carateres
#Python 3 almacena los aracteres odifiados en el estandar Unicode 
#Permite reperesentar una antidad ingente de simbolos incluyendo los famosos emojis
'Mi primera cadena en Python'
#Se puede inluid comillas dobles dentro de la adena de texto
'Los llamados "strings" son secuenias de carateres'
#crea un string con comillas simples dentro
'los llamdos \'string\'son secuencias de caracter'
#comillas simples dentro de comillas dobles
"los llamdas 'string'son secuenias de caracter" 
#cadena vacia
#La cadena vacia es aquella que no contiene ningun caracter:
" " 
#conversion 
#podemos crear strings convirtiendo otros tipos de variables mediantela funcion str():
numero = 123
decimal = 45.67
texto_numero = str(numero)       # "123"
texto_decimal = str(decimal)     # "45.67"
print(texto_numero)
print(texto_decimal) 
#secuencias de escape
#Python permite escapar el significado de algunos caracteres para conseguir otros resultados
#Si escribimos una barra invertida\ antes del carater en cuestion, le otorgamos un sifnigcado especial
#la secuencia de escape mas conocida es \n que representa un salto de linea 
#salto de linea
msg = 'primera linea\nsegunda linea\ntercera linea'
print(msg)
#tabulador
msg = 'valor =\t40'
print(msg)
#comilla simple
msg = 'necesitamos \'escapar\' la comilla simple'
print(msg)
#barra invertida
msg= 'capitulo \\ seccion \\ encabezado'
print(msg)
 #Uso del Print()
 #dentro de la funcion print() se puede usar otros parametros:
msg1='Sabes por que estoy aca?'
msg2= 'por que me apasiona?'
print(msg1, msg2)
print(msg1, msg2, sep= '|')
print(msg2, end='!!\n')

#interaccion con el usuario con input():
#Solicita la entrada de datos por teclado con la funcion input():

name=input('Introduzca su nombre:\n ')
print("El nombre que ingresaste es:\n", name)
print(type(name))




