#Hola.
#En esta ocasion vamos a continuar con el codigo de nuestra red social,
#al cual le habi­amos agregado un mensaje.
#El programa de la semana anterior permitia:
#1. Obtener datos del usuario
#2. Consultar y mostrar varios mensajes de estado del usuario
#3. Escoger entre distintas acciones que el usuario puede realizar

#Si lograste agregar una opcion nueva al sistema, por ejemplo, para escribir los datos
#del perfil del usuario, habras notado que tienes que escribir de nuevo el codigo necesario
#con un print por cada dato. El codigo se ver­a como esta mas abajo.
from datetime import datetime

def year():
    now = datetime.now()
    year = now.year
    return year

def name():
    nombre = input("Para empezar, dime como te llamas. ")
    print()
    print("Hola ", nombre, ", bienvenido a Mi Red")
    print()
    return nombre


def age():
    agno = int(input("Para preparar tu perfil, dime en que año naciste. "))
    dato1 = year()
    edadFinal = dato1 - agno
    return edadFinal


def height():
    print("Cuentame mas de ti, para agregarlo a tu perfil.")
    estatura = float(input("¿Cuanto mides? Dimelo en metros. "))
    estatura_m = int(estatura)
    estatura_cm = int( (estatura - estatura_m)*100 )
    return estatura_m, estatura_cm


def amigos():
    num_amigos = int(input("Muy bien. Finalmente, cuentame cuantos amigos tienes. "))
    return num_amigos


def datos(dato1, dato2, dato3, dato4, dato5):
    print("Nombre:  ", dato1)
    print("Edad:    ", dato2, "años")
    print("Estatura:", dato3, "metros y", dato4, "centi­metros")
    print("Amigos:  ", dato5)


#-----------------****************---------------
print("Bienvenido a ... ")
print("""
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/

""")

# Solicitud de nombre
nombre1 = name()

# CÃ¡lculo de edad
edad1 = age()

# CÃ¡lculo de estatura
altura1 = height()

# Cantidad de amigos
num_amigos = amigos()

#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre1, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
datos(nombre1, edad1, altura1[0], altura1[1], num_amigos)
print("--------------------------------------------------")
print("Gracias por la informacion. Esperamos que disfrutes con Mi Red")
print()

#Esta opcion permite entrar al ciclo. Solo interesa que no sea 0.
opcion = 1
while opcion != 0:
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje publico")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opcion: "))

    #Codigo para la opcion 1. Publicar un mensaje.
    if opcion == 1:
        mensaje = input("Ahora vamos a publicar un mensaje. ¿Que piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre1, "dice:", mensaje)
        print("--------------------------------------------------")

    #Codigo para la opcion 2. Publicar un mensajes a un grupo de personas.
    elif opcion == 2:
        mensaje = input("Ahora vamos a publicar un mensaje a un grupo de amigos. ¿Que quieres decirles? ")
        print()
        cuales = int(input("Cuantos amigs quieres que vean esto?"))
        for i in range(cuales):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            print("--------------------------------------------------")
            print(nombre1, "dice:", "@"+nombre_amigo, mensaje)
            print("--------------------------------------------------")

    #Codigo para la opcion 3. Publicar los datos del perfil del usuario.
    elif opcion == 3:
        print("--------------------------------------------------")
        datos(nombre1, edad1, altura1[0], altura1[1], num_amigos)
        print("--------------------------------------------------")

    #Codigo para la opcion 4. Actualizar los datos del perfil del usuario.
    elif opcion == 4:
        #Repetimos el codigo para solicitar datos
        # Solicitud de nombre
        nombre = name()

        # Calculo de edad
        edad = age()

        # Calculo de estatura
        altura = height()

        # Cantidad de amigos
        num_amigos = amigos()

        print()
        print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
        # Repetimos el codigo para mostrar los datos del usuario.
        print("--------------------------------------------------")
        datos(nombre, edad, altura[0], altura[1], num_amigos)
        print("--------------------------------------------------")
        print()

    #Codigo para la opcion 0. Salir.
    elif opcion == 0:
        print("Has decidido salir.")

    #Codigo para la opcion que no coincida con ninguna anterior.
    else:
        print("No conozco la opcion que has ingresado. Intentalo otra vez.")

print()
print("Gracias por usar Mi Red. ¡Hasta pronto!")
print()

#Si pruebas este cÃ³digo, verÃ¡s que funciona correctamente, pero nuestro programa ahora es bastante largo.
#Casi 140 lÃ­neas.
#Esto en sÃ­ no es malo. Sin embargo, si le pones atenciÃ³n, verÃ¡s que hay cÃ³digo que hemos tenido
#que repetir completamente. Por ejemplo, el cÃ³digo para mostrar el perfil de un usuario estÃ¡ escrito tres veces.
#Si ahora queremos agregar un nuevo dato del usuario, por ejemplo, el paÃ­s en que vive, debemos modificar
#al menos tres partes distintas del programa.
#Esto lo podemos hacer, talvez sin cometer errores, en un programa pequeÃ±o como Ã©ste.
#Pero en programas mÃ¡s grandes, es muy fÃ¡cil que nos olvidemos de actualizar una parte del cÃ³digo,
#o que no recordemos todas las partes que hay que modificar.

#Cuando tenemos instrucciones que se repiten tantas veces en distintas partes del programa,
# es una indicaciÃ³n de que talvez necesitamos agregar funciones.

#Te invitamos a pensar en al menos 3 alternativas o funcionalidades de este cÃ³digo
#que podrÃ­an convertirse en una funciÃ³n.