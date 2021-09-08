#Realizar un programa que permita
monto = int(input("Ingrese el monto a abonar: "))
formadepago = int(input("FORMA DE PAGO \n 1- Para pagar en efectivo (-10% si > 1000) \n 2- Para pagar con tarjeta (-5%) \n 3- Fiado (+50%) \n"))
totalfinal = 0
if formadepago == 1:
    if monto > 1000:
        desc = monto * 0.1
        totalfinal = monto - desc
    else:
        totalfinal = monto
elif formadepago == 2:
    desc = monto * 0.05
    totalfinal = monto - desc
elif formadepago == 3: #Nueva funcion! Fiado aumentara 50% mas el monto
    desc = monto * 0.5
    totalfinal = monto + desc
else:
    print('Opcion incorrecta')

if formadepago == 1 or formadepago == 2 or formadepago == 3: #Ahora no mostrara 0 si se ingresa una opcion incorrecta
    print('El total final es: ', totalfinal)