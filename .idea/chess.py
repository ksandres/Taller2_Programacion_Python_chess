

x= int(input("ingrese la fila que esta ubicado el caballo"))
y= int(input("ingrese la columna que esta ubivado el caballo"))

x -= 1
y -= 1
if 0<= x < 8 and 0 <=  y <8:

    movimientosCaballo=[(-2,-1), (-2,1),
                        (-1,-2), (-1,2),
                        (1, -2), (1, 2),
                        (2, -1), (2, 1)]
    movimientosValidos = []
    for mx,my in movimientosCaballo:
        nx = x+mx
        ny = y+my
        if 0 <= nx< 8 and 0<= ny <8:
            movimientosValidos.append((nx+1,ny+1))


    print("El caballo puede moverse a las siguientes casillas:")
    for movimiento in movimientosValidos:
        print(f"Fila: {movimiento[1]}, Columna: {movimiento[0]}")


else:
    print("las coordenandas ingresadas son invalidas")




