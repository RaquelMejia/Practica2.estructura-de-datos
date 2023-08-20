#Crear una lista con la siguiente serie de numeros 
numeros =  [1, 4, 6, 7, 8, 10, 13, 2, 9, 28, 9, 10, 7, 3, 8] 
pares = [] 
impares = [] 

for numero in numeros:

 if numero%2 == 0:
     pares.append(numero)
 else:
     impares.append(numero)
     
print("serie:",numeros)    
print("pares:",pares)
print("impares:",impares)
 
    
