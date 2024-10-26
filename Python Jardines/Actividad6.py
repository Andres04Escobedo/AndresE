
""" 
Nivel básico:
Verificar si un número es positivo, negativo o cero
Descripción: Crea un programa que pida al usuario un número y verifique si es positivo, negativo o cero.
"""

signo_numero = input("Escribe un numero: ")
numero = float(signo_numero)

if numero == 0:
    print ("El numero es cero")
elif numero < 0:
    print ("El numero es negativo")
else:
    print ("El numero es positivo")

"""
Determinar si un estudiante aprobó o no
Descripción: Crea un programa que pida la calificación de un estudiante y determine si ha aprobado (60 o más) o no.
"""

calificacion = int(input("Ingrese la calificación del estudiante: "))

if calificacion >= 60:
    print("El estudiante ha aprobado.")
elif calificacion < 60:
    print("El estudiante no ha aprobado.")