#Este es un programa para convertir la Fuerza centrífuga relativa a RPM y Viceversa
print("BIENVENIDO AL CONVERSOR DE UNIDADES PARA EL USO DE MAQUINAS CENTRIFUGAS")

import math #cargamos el modulo matematico

#primero definimos las variables del programa

k=1.12e5 #constante
g=918 #cm*s^2


#El programa comienza aqui
while True:
    unidad=input("A que unidades quieres convertir [rpm/FCR]: ").lower() #define en que sentido queremos hacer la conversion
    
    if unidad=="rpm" or unidad=="RPM":
        r=float(input("Cual es el radio de tu máquina (cm): ")) #define el radio del eje de rotación de la centrifuga
        fcr=float(input("Cuantos G quieres convertir a rpm: "))
        rpm=math.sqrt(fcr/(k*r))
        print(fcr,"G son",round(rpm,3),"rpm.")
    elif unidad=="FCR" or unidad=="fcr":
        r=float(input("Cual es el radio de tu máquina (cm): ")) #define el radio del eje de rotación de la centrifuga
        rpm=float(input("Cuantos rpm quieres convertir a G: "))
        fcr=k*r*(rpm**2)
        print(rpm,"rpm son",round(fcr,3),"G.")
    else:
        print("Error 1. Por favor escribe rpm o FCR")
        continue

    #preguntamos si queremos seguir convirtiendo unidades, nega abotamos el programa
    seguir=input("Quieres continuar convirtiendo unidades? [y/n]: ").lower()

    if seguir=="n":
        print("Gracias por usar el conversor. ¡Hasta la próxima!")
        print("Creado por MiguelRBla para el curso FUNDAE Fundamentos de python 1.")
        break

    print("------------------------------------")
