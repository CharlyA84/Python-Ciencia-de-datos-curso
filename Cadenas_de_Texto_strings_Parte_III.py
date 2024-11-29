#Longitud de uan cadena
#Para obtener la longitud de una cadena podemos hacer uso de len():

proverb = 'Lo cortes no quita lo valiente'
print(len(proverb))

empty = ''
print(len(empty))

#Pertenecia de un elemento 
#Si queremos comprobar que un determinado subcadena se encuentra
# en una cadena de texto utilizamos el operador para ello. Se trata
#de una espresion que tiene como resultado un valor <<boolenano>>
#verdadero o falso

proverb = 'mas vale malo conocido que bueno por conocer'
print('malo' in proverb)
print('bueno' in proverb)
print('regular' in proverb)


#Pertenecia de un elemento 
#tambien podemos ver si un subcadena no esta en la cadena de texto:
dna_sequence = 'ATGAAATTGAAATGGGA'
print(not('C' in dna_sequence)) #Primera aproximacion
print('C' not in dna_sequence) #Forma pitonica

#Dividir una cadena
#Python nos ofrece la funcion split() para dividir las cadenas de texto
#que debemos usar atenponiendo el <<string>> que debemos dividir

proverb = 'No hay mal que por bien no venga'
print(proverb.split())

tools = 'Martillo,sierra,destornilaldor'
print(tools.split(','))

#Si no especifica un separador, split() usa por defecto cualquier secuencia de espacios en blanco, tabuladores y saltos de linea
 
#Limpiar cadenas
#La funcion strip() se utiliza para eliminar caracteres del principio y del fin de un <<string>>
#istrip() y rstrip() son para hacer  <<limpieza>> por la izquierda (comienzo) y por la derecha (final,respectivamente)

serial_number = '\n\t    \n   483749832274832   \n\n\t    \t   \n'

print(serial_number.strip())

print(serial_number.lstrip())

print(serial_number.rstrip())

#la funcion strip() no modifica la cadena que estamos usando sino que devuelve una nueva cadena de textos con 
#las modificaciones permitentes










