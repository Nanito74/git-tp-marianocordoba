#Realizar un programa que permita
monto = int(input("Ingrese el monto a abonar: "))
formadepago = int(input("FORMA DE PAGO \n 1- Para pagar en efectivo \n 2- Para pagar con tarjeta \n"))
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
else:
    print('Tecla incorrecta')

print('El total final es: ', totalfinal)