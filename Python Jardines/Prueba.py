signo_numero = input("Escribe un numero: ")
numero = float(signo_numero)

if numero == 0:
    print ("El numero es cero")
elif numero < 0:
    print ("El numero es negativo")
else:
    print ("El numero es positivo")