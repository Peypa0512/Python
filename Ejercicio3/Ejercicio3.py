personas=[]
musica = []
letra = "TRWAGMYFPDXBNJZSQVHLCKE"

class Amigos():
    "Clase con los datos de amigos, limpieza de datos y lo adjunto a lista personas"

    def __init__(self,nombre, apell,dni,poblacion,pais):


        #cambio caracteristicas de datos y compruebo que se introduce bien el dni

        self.nombre = nombre.title()
        self.apell= apell.title()
        self.poblacion = poblacion.capitalize()
        self.pais = pais.upper()
        self.nif= dni
        x = self.nif

        while True:

            if len(x) == 9 and x.isdigit() == True or x.isalpha() == True:
                print("Debe contener una letra tu DNI")
                x = input("Introduce tu DNI> ")
            elif len(x) < 9 and len(x) > 9:

                    try:
                         if len(x) < 9 and len(x) > 9:
                            print("Si tu DNI contiene \"0\"debes de ponerlos")
                            print(f'Debe contener 8 digitos {nombre}')
                            x = input("Introduce tu DNI: ")

                    except(ValueError):
                        print(f"El dni es erroneo, vuelve a intentarlo {nombre}")
                        x = input("Introduce tu DNI> ")

            else:
                dni = int(x[0:8])
                resid = dni % 23
                z = letra[resid]
                dn = str(dni).zfill(8) + z
                nif = dn
                break
            #cargo datos en lista personas
        print(f"La letra no cuadra con el resto del DNI {nombre}")
        print(f'El DNI correcto es {nif}')
        personas.append([nombre, apell, nif, poblacion, pais])




class Musica():
    #Capturo dato de gustos musicales y cambio caracteristicas para almacenar en lista musica
    def __init__(self,cancion, inter, genero):
        self.cancion= cancion.title()
        self.genero= genero.upper()
        self.inter = inter.title()
        musica.append([self.cancion,self.inter,self.genero])
        print('Datos grabados correctamente')




class Amiguete(Amigos,Musica):
	# con un submenu vamos a hacer varios filtros

    def __init__(self,nombre,apell,dni,poblacion,pais,cancion,inter,genero):
        Amigos.__init__(self,nombre,apell,dni,poblacion,pais)
        Musica.__init__(self,cancion,inter,genero)
        self.cancion = cancion
        self.inter = inter
        self.genero = genero

    def submenu(self):
		#creamos el submenu para poder unir las distintas consultas

        print("Bienvenido a este submenú, vamos a hacer ahora una serie de consultas")
        print("""
            1.- Vamos a conocer algo más a tus amigos
            2.- Veremos que gustos musicales tienen
            3.- Vamos a conocer algo más de tus amigos y sus gustos musicales
            4.- Volver al Menú Principal
            """)
        pregunta = int(input("Necesito que eligas una opción..... "))

        while True:

            if pregunta == "1":
                print(self.datos())
            if pregunta == "2":
                print(self.musica())
            if pregunta == "3":
                print(self.mixto())
            if pregunta == "4":
                return menu2()
            if pregunta != "1" and pregunta != "2" and pregunta != "3":
                print("¡Ups!.... Parece que te has equivocado, vuelve a intentarlo .....")
                pregunta = input("---- ")


    def datos(self):
		# Consultas con los datos recogidos de la clase Amigos
		
        print("Vamos a cotillear un poco en tus amigos, elige la opción que mas desees saber de ellos")
        print("Elige del 1 al 4")

        print("""
                        1.- Quieres saber el DNI y el nombre de tu amigo 
                        2.- Te gustaría ver el nombre de tus amigos como se vería en formato anglosajon?
                        3.- Te puedo mostrar si quieres sus DNI 
                        4.- Salir """)
        pregunta = input("---- ")

        while True:

            if pregunta == "1":
                for x in range(len(personas)):
                    print(f'El nombre de tu amigo es {personas[x][0]} {personas[x][1]} {personas[x][2]}')

            if pregunta == "2":
                for x in range(len(personas)):
                    print(f'El nombre de tu amigo en anglosajon sería {personas[x][1]}, {personas[x][0]}')

            if pregunta == "3":
                for x in range(len(personas)):
                    print(f'Aunque esto no deberia ser posible...... en fin, el DNI de tu amigo es {personas[x][2]}')
            if pregunta == "4":
                print("Volvemos al Menú Inicial")
                print(self.submenu())
        
		# para solo introducir la opcion correcta
            if pregunta != "1" and pregunta != "2" and pregunta != "3":
                print("¡Ups!.... Parece que te has equivocado, vuelve a intentarlo .....")
                pregunta = input("---- ")
            x = input("¿Quieres saber algo más de tus amigos? S/N ")

            if x != "N" and x != "n" and x != "S" and x != "s":
                print("Esta no era la respuesta que esperaba.... vuelva a intentarlo, por favor")
                x = input("¿Quieres saber algo más de tus amigos? S/N ")

            if x.lower() == "s":

                print("Me alegro mucho que hayas elegido esta opción.... continuemos")
                print("Vamos a cotillear un poco en tus amigos, elige la opción que mas desees saber de ellos")
                print("Elige del 1 al 4")

                print("""
                        1.- Quieres saber el DNI y el nombre de tu amigo 
                        2.- Te gustaría ver el nombre de tus amigos como se vería en formato anglosajon?
                        3.- Te puedo mostrar si quieres sus DNI 
                        4.- Volver al menú anterior   """)
                pregunta = input("---- ")


            else:
				#salimos del programa
                print("Es una pena, pero hasta pronto, ¡Nos vemos!")
                exit()

    def musica(self):
			#usamos los registros obtenidos de la case Musica
			
            print("Vamos a saber mas cosas de tus amigos, elige la opción que mas desees saber de ellos")
            print("Elige del 1 al 3  o simplemente N")

            print("""
                           1.- Te puedo ordenar las canciones preferidas de tus amigos 
                           2.- Puedo mostrarte que tipo de genero de música prefieren tus amigos
                           3.- ¿Prefieres saber que grupo músical es el preferido de tus amigos?
                           4.- Volvemos a Menú Principal""")
            pregunta = input("---- ")

            while True:

                if pregunta == "1":

                    for x in range(len(musica)):
                        print(f'La canción preferida de tus amigo es {musica[x][0]}')

                if pregunta == "2":
                    for x in range(len(musica)):
                        print(f'El genero de música que prefiere tu amigo es {musica[x][2]}')

                if pregunta == "3":
                    for x in range(len(musica)):
                        print(f'El grupo músical preferido de tu amigo es  {musica[x][1]}')

                if pregunta == "4":
                    #regresa a Submenu
					
					print('Volvemos al Menú Principal')
                    print(self.submenu())

                if pregunta != "1" and pregunta != "2" and pregunta != "3":
                    print("¡Ups!.... Parece que te has equivocado, vuelve a intentarlo .....")
                    pregunta = input("---- ")

                x = input("¿Quieres saber algo más de tus amigos? S/N ")



                if x != "N" and x != "n" and x != "S" and x != "s":
                    print("Esta no era la respuesta que esperaba.... vuelva a intentarlo, por favor")
                    x = input("¿Quieres saber algo más de tus amigos? S/N ")

                if x.lower() == "s":

                    print("Puedo enseñarte más cosas de los gustos musicales de tus amigos.... ¿Seguimos?")
                    print("Debes elegir del 1 al 3  o simplente N")

                    print("""
                                   1.- Te puedo ordenar las canciones preferidas de tus amigos 
                                   2.- Puedo mostrarte que tipo de genero de música prefieren tus amigos
                                   3.- ¿Prefieres saber que grupo músical es el preferido de tus amigos? 
                                   4.- Volver al menú principal     """)
                    pregunta = input("---- ")

                else:
                    #salimos del programa
					print("Entonces volvamos al menú principal")
                    exit()

    def mixto(self):
		#consultas con datos de ls clases Amigos y Musica
		
        print(
            "¡Hola de nuevo!, voy a intentar darte las información que quieras, para ello necesito que eligas unas opción...")
        print("""
                  1-. Te puedo decir el grupo favorito de cada amigo....
                  2.- Puedo decirte su genero de música preferido
                  3.- ¿Quieres saber su canción favorita?
                  4.- Volver al Menú anterior
                  """)
        pregunta = input("Elige la opción .......")

        while True:

            if pregunta == "1":
                print(len(personas))
                for x in range(len(personas)):
                    print(f'El grupo favorito de tu amigo  {personas[x][0]} {personas[x][1]} es {musica[x][2]}')

            if pregunta == "2":
                for x in range(len(personas)):
                    print(
                        f'El genero de musica que escucha tu amigo en anglosajon sería  {personas[x][1]},{personas[x][0]}'
                        f' es  {musica[x][2]}')

            if pregunta == "3":
                for x in range(len(personas)):
                    print(f'la canción favorita  de tu amigo  {personas[x][0]} {personas[x][1]} es {musica[x][0]}')

            if pregunta == "4":
                print ('Volvemos al Menú Principal')
                print(self.submenu())

            x = input("¿Quieres saber algo más de tus amigos? S/N ")
            if x != "N" and x != "n" and x != "S" and x != "s":
                print("Esta no era la respuesta que esperaba.... vuelva a intentarlo, por favor")
                x = input("¿Volveos a intentarlo? S/N ")

            if x.lower() == "s":

                print("Me alegro mucho que hayas elegido esta opción.... continuemos")
                print("Elige del 1 al 4")

                print(""" 
                          1- Te puedo decir el grupo favorito de cada amigo....
                          2.- Puedo decirte su genero de música preferido
                          3.- ¿Quieres saber su canción favorita?
                          4.- salir del programa
                          """)

                pregunta = input("---- ")

            else:
                print("Es una pena, pero hasta pronto, ¡Nos vemos! ok")
                exit()


            if pregunta != "1" and pregunta != "2" and pregunta != "3" or pregunta != "4":
                print("¡Ups!.... Parece que te has equivocado, vuelve a intentarlo .....")
                pregunta = input("---- ")



def uno():

            # Primera opción de entrada de datos de los Amigos
            nombre = input("Por Favor introduce tu nombre> ")
            apell = input("Introduce tus apellidos> ")
            nif = input("Introduce tu DNI> ")
            poblacion = input("Introduce tu ciudad> ")
            pais = input("Introduce tu pais> ")
            cancion = input("¿Cuál es tu canción favorita? ")
            inter = input("Recuerdame de que grupo es: ")
            genero = input("¿A qué genero pertenece? ")
			
            # creo objeto misAmigos de Amiguete
            misAmigos = Amiguete(nombre, apell, nif, poblacion, pais,cancion, inter, genero)



            while True:

                x = input("¿Deseas añadir más amigos? S/N ")

                if x != "s" and x != "n" and x != "S" and x != "N":
                    print("Tiene que introducir S / N")
                    x = input("¿Deseas añadir más amigos? S/N ")

                elif x != "N" and x != "n":

                    nombre = input("Por Favor introduce tu nombre> ")
                    apell = input("Introduce tus apellidos> ")
                    nif = input("Introduce tu DNI> ")
                    poblacion = input("Introduce tu ciudad> ")
                    pais = input("Introduce tu pais> ")
                    cancion = input("¿Cuál es tu canción favorita? ")
                    inter = input("Recuerdame de que grupo es: ")
                    genero = input("¿A qué genero pertenece? ")
					# creo de nuevo objeto misAmigos de Amiguete
                    misAmigos = Amiguete(nombre,apell,nif,poblacion,pais,cancion, inter, genero)


                else:
                    break

			# entramos en submenu
			
            print(misAmigos.submenu())

def menu2():
	#clase definida para volver al Menú Principal
    return False

def nueve():
  print("Fin de Programa, hasta luego :)")
  return False





def menu(opcion):


    diccionario = {
    1 : "uno()",
    2 : "menu2()",
    3 : "nueve()"

    }
    return eval (diccionario.get(opcion))

while True:

    print("""
        1. Vamos a grabar los datos de tus amigos y a continuación veremos unas cosas interesantes de ellos.
        3. Salir  
        """)
    opcion = int(input('---->'))
    continuar = menu(opcion)
    if (continuar == False):
        print("Hemos finalizado, hasta pronto")
        break


if  __name__ == '__main__':
    menu(opcion) #iniciamos el programa switch
