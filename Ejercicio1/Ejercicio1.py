NombreJug1 = input("Escribe el nombre del primer jugador: ")
NombreJug2 = input("Escribe el nombre del segundo jugador: ")
NombreJug3 = input("Escribe el nombre del tercer jugador: ")
NombreJug4 = input("Escribe el nombre del cuarto jugador: ")

dic_contador = [121, 121, 121,121]
i = 1
#1 Jugada

while (i < 4 ) :
    print( "{} Partida".format(i))
    dic_contador[0] -= int(input("Introduce los puntos que ha restado el jugador1:"))
    dic_contador[1] -= int(input("Introduce los puntos que ha restado el jugador2: "))
    dic_contador[2] -= int(input("Introduce los puntos que ha restado el jugador3: "))
    dic_contador[3] -= int(input("Introduce los puntos que ha restado el jugador4: "))


    if (dic_contador[0]) <= 0:
       print("El jugador 1 con nombre {} ha ganado en la ronda {} con {} puntos".format(NombreJug1, i ,dic_contador[0]))
       break  
    else:
       print("A {} le queda {} puntos".format(NombreJug1,dic_contador[0]))

    if (dic_contador[1]) <= 0:
       print("El jugador 2 con nombre {} ha ganado en la ronda {} con {} puntos".format(NombreJug2, i ,dic_contador[1]))
       break
    else:
       print("A {} le queda {} puntos".format(NombreJug2,dic_contador[1]))  
        
    if (dic_contador[2]) <= 0:
       print("El jugador 3 con nombre {} ha ganado en la ronda{} con {} puntos".format(NombreJug3, i ,dic_contador[2]))
       break
    else:
       print("A {} le queda {} puntos".format(NombreJug3,dic_contador[2]))  

    if (dic_contador[3]) <= 0:
       print("El jugador 4 con nombre {} ha ganado en la ronda{} con {} puntos".format(NombreJug4, i ,dic_contador[3]))
       break
    else:
       print("A {} le queda {} puntos".format(NombreJug4,dic_contador[3]))  

    
    i += 1
    