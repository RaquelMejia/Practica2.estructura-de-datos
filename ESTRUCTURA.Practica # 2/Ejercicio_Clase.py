#Declarar Variable

continuar = True
total_Venta = 0
cantidad_Venta = 0

def inputNumber(mensaje, isFloat = False):
    while  True:
        try:
            if isFloat:
                return float(input(mensaje))
            return int (input(mensaje))
        except ValueError:
            print("Opps no es una entrada valida intenta de nuevo")

while continuar == True:
    cantidad = inputNumber("Ingresa la cantidad de producto: ")
    precio = inputNumber("Ingresa el precio del producto: ")

    total_Sin_Descuento= cantidad*precio

    if cantidad >= 5 and cantidad <= 10:
        total_Venta += total_Sin_Descuento - (total_Sin_Descuento* 0.05)
    elif cantidad >= 11 and cantidad <= 20:
        total_Venta += total_Sin_Descuento - (total_Sin_Descuento* 0.10)
    elif cantidad > 20:
        total_Venta +=total_Sin_Descuento - (total_Sin_Descuento* 0.15)
    else:
        total_Venta += (total_Sin_Descuento)
    
    cantidad_Venta += cantidad 

    opción = input("¿Desea Continuar? S/N")

    if opción.upper() == 'N':
        continuar = False
        print("Gracias por comprar :)")

    print("Total de la venta ${0}". format(total_Venta))
    print("Unidades Totales {0}". format(cantidad))



