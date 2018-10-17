#Sebastan Macias Ibarra - A01376492
#Calcular el cociente, residuo y el mayor de verios numeros con ciclos while


# Función encargada de imprimir el menú y recibir la opción del usuario
def leerOpcionMenu():
    print("Menú principal")
    print("Autor: Sebastian Macias Ibarra")
    print("Matrícula: A01376492")
    print("1. Calcular divisiones")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion = int(input("Teclea tu opción: "))   #El usuario escoge el programa que quiere correr
    return opcion                               #El valor de la elección se regresa a main()


# Función encargada de realizar divisiones con restas e imprime el sobrante
def dividir():
    dividendo = int(input("Escribe el número dividendo : "))  #pregunta por el dividendo
    divisor = int(input("Escribe el número divisor : "))        #pregunta  por el divisor

    if divisor < dividendo:                 #Función para demostrar que el divisor es menor que el dividento y se puede realizar una división
        cociente = 0
        dividendoModif = dividendo
        dividendoModif - divisor

        while dividendoModif > 0:           #Ciclo
            if dividendoModif >= 0:
                dividendoModif = dividendoModif - divisor
                cociente += 1

        # Condición para el valor a regresar
        if dividendoModif == 0:
            return ("%d / %d = %d, sobra %d" % (dividendo, divisor, cociente, dividendoModif))

        elif dividendoModif != 0:
            return ("%d / %d = %d, sobra %d" % (dividendo, divisor, (cociente - 1), (divisor - (dividendoModif * -1))))

    elif dividendo < divisor:
        return ("%d / %d = 0, sobra %d" % (dividendo, divisor, dividendo))


#Función que se encarga de buscar el número mayor
def encontrarMayor():
    mayor = 0           #Almacenamiento, variable con valor 0
    numero = int(input("Teclea un número [-1 para salir]: "))       #Pregunta por el número

    if numero == -1: #Si sale de manera inmediata imprimirá que no hay valorer
        return "No hay valor mayor"

    while numero != -1:     #Ciclo
        if numero > mayor:  #Compara si el numero es mayor que la varible mayor
            mayor = numero  #En dado caso que sea mayor, el valor de la variable mayor se sustituirá por el número insertado, sino continua

        numero = int(input("Teclea un número [-1 para salir]: "))

    return "El mayor es: %d" % mayor  #Regresa el valor mayor


#Función principal
def main():
    opcion = leerOpcionMenu() #Invoca función del menú y regresa
    while opcion != 0:
        if opcion == 1:
            resultadoDivision = dividir()
            print(resultadoDivision)
            print("")

        elif opcion == 2:
            mayor = encontrarMayor()
            print(mayor)
            print("")

        elif opcion == 3:
            break   #Sale del programa

        elif opcion > 3:  #Condición que se encarga de imprimir un mensaje para que elija una opción válida
            print("ERROR, teclea 1, 2 o 3")
            print("")

        opcion = leerOpcionMenu()
    print("")
    print("Gracias Por usar este programa, regresa pronto")


#Invoca función principal
main()