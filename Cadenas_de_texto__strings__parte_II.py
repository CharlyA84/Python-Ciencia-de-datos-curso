
#Combinar dos strings
#podemos combinar dos o mas cadenas de texto usando el operador +:
proverb1 = 'Cuando el rio suena'
proverb2 = 'agua lleva'
Resultado= proverb1+','+proverb2 #Incluimos una coma
print(Resultado)

#Repetir cadenas
#podemos repetir dos o mas cadenas de texto utilizando operador *:
reaccion= 'Wow'
repetidor=reaccion*4
print(repetidor)

#Indexacion en los strings
#los strings estan inexados y cada caracter su propia posicion
#Para obtener un unico caracter de un string hay que especificar un
# indice dentro de corchetes [...].


sentence = 'hola, Mundo'
print(sentence[0])
print(sentence[-1])
print(sentence[4])
print(sentence[5])
#el indexado de una cadena de texto siempre empieza en 0 y termina
#en una unidad menos de la longitud de la cadena.

#trucar una cadena 
#es posible extraer "trozos" de una cadena de texto:
#[:] Extrae la secuencia enteras desde el comienzo hasta el final. como 
#hacer una copia de todo el string
#[start:] Extraer desde start hasta el final de la cadena 
#[:end] Extare desde el principio el comienzo de la cadena hasta end -1
#[start:end] Extare desde estar hasta end -1
#[start:end:step] Extrae desde start hasta end -1 haciendo saltos de tamaño step

proverb = 'Agua pasada no mueve molino'
print(proverb[:])
print(proverb[12:])
print(proverb[:11])
print(proverb[5:11])
print(proverb[5:11:2])





