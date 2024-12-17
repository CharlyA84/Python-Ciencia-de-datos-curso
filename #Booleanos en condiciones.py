#Booleanos en condiciones
# cuando queremos preguntar por la veracidad de una determinada variable <<booleana>> en una condicion, se puede hacer asi
is_cold = True
if is_cold == True:
    print('Coge Chaqueta')
else:
    print('Usa camiseta')

#o asi en forma booleano
if is_cold:
    print('Coge chaqueta')
else:
    print('Usa camiseta')
  

#o en el caso de un valor falso del booleano seria:
is_cold = False
if not is_cold: #Equivalente a if is_cold == False
    print('Usa camiseta')
else:
    print('Coge chaqueta')
    


