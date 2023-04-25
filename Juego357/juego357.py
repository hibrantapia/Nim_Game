# juego 3 5 7
# v2
# TODO: 
# 

import random as r
col1 = 3
col2 = 5
col3 = 7


def printBoard():
    # imprimir el tablero
    print("1: " + " * "*col1)
    print("2: " + " * "*col2)
    print("3: " + " * "*col3)

def modifyBoard(col, num):
    # modificar el tablero
    global col1
    global col2
    global col3
    if (col == 1):
        col1 -= num
    elif (col == 2):
        col2 -= num
    elif (col == 3):
        col3 -= num


def nimSum():
    global col1
    global col2
    global col3
    # calcula la suma de nim de las columnas
    # la suma de nim es la suma en múltiplos de 4 2 y 1, se busca que los múltiplos tengan pareja para que la suma sea 0
    # esto se puede conseguir con un XOR ya que es una operación en binario que nos permitirá saber si hay parejas sin tener que hacer la suma
    # Si el XOR regresa 0, entonces no hay parejas y el agente estará en una posición virtualmente perdedora.
    # Si el XOR regresa un número distinto de 0, entonces el agente estará en una posición virtualmente ganadora y puede forzar la victoria desde ahí
    return col1 ^ col2 ^ col3  # XOR "^"


def agente(col1, col2, col3):
    print("El nim es  " + str(nimSum()))
    print("Es el turno del agente")
    # las combinaciones ganadoras son 2 2 0, 3 3 0, 4 4 0, 5 5 0, 1 1 1, 1 2 3, 1 4 5, 2 2 4, 2 4 6, 2 5 7, 3 4 7, 3 5 6
    # ya que su nimSum es distinto de 0 y se puede forzar la victoria
    col, num = 0, 0
    col1h = col1
    col2h = col2
    col3h = col3
    if (nimSum() == 0):
        print("Bot: Estás en una buena posición, veré qué puedo hacer")
        # el agente está en una posición perdedora y no importa el número de fichas que retire, virtualmente perderá
        # entonces escogemos aleatorio
        if (col1 != 0):
            col = 1
            num = r.randint(1, col1)
            return col, num
        elif (col2 != 0):
            col = 2
            num = r.randint(1, col2)
            return col, num
        elif (col3 != 0):
            col = 3
            num = r.randint(1, col3)
        else:
            print(
                "Se jodió la condición en jugadas aleatorias, en teoría no debería aparecer este mensaje")
    else:
        # el agente está en una posición ganadora y puede forzar la victoria
        # el agente tiene que hacer una jugada tal que el nimSum sea 0
        # para esto, el agente tiene que retirar el número de fichas que haga que el nimSum sea 0 de una columna no vacía
        # tiene que retirar mínimo 1 ficha

        sum=nimSum()
        if (col1!=0 and (col1^sum)<col1 and col==0 and num==0):
            col=1
            num=col1-col1^sum
            print(str(col1^sum) + " " + str(sum))
            col1h=col1h-num
        elif (col2!=0 and (col2^sum<col2) and col==0 and num==0):
            col=2
            num=col2-col2^sum
            print(str(col2^sum)+ " " + str(sum))
            col2h=col2h-num
        elif (col3!=0 and (col3^sum<col3) and col==0 and num==0):
            col=3
            num=col3-col3^sum
            print(str(col3^sum)+ " " + str(sum))
            col3h=col3h-num

        # if (col1 != 0 and ((col1 ^ nimSum()) < col1)):
        #     col = 1
        #     num = col1-(col1 ^ nimSum())
        #     col1h = col1h-num
        #     print(f"Here 1 num: {num}, col1h: {col1h}, nimSum: {nimSum()}, XOR: {col1 ^ nimSum()}")
        # elif (col2 != 0 and ((col2 ^ nimSum()) < col2)):
        #     col = 2
        #     num = col2-(col2 ^ nimSum())
        #     col2h = col2h-num
        #     print(f"Here 2 num: {num}, col2h: {col2h}, nimSum: {nimSum()}, XOR: {col2 ^ nimSum()}")
        # elif (col3 != 0 and ((col3 ^ nimSum()) < col3)):
        #     col = 3
        #     num = col3-(col3 ^ nimSum())
        #     col3h = col3h-num
        #     print(f"Here 3 \n num: {num}, col3h: {col3h}, nimSum: {nimSum()}, XOR: {col3 ^ nimSum()}")
                
        if (col1h == 0 and col2h == 0 and col3h == 0):
            print("Bot: Final del juego, bien jugado :)")
            num-=1
            return col, num
        
        # if (col1h+col2h+col3h == 2):
        #     print("Entered test")
        #     if(col==1 and num>=col1):
        #         num=col1-1
        #     elif(col==2 and num>=col2):
        #         num=col2-1
        #     elif(col==3 and num>=col3):
        #         num=col3-1
             
    return col, num

def endgame(turn):
    if (turn):
        print("Ganó el jugador")
    else:
        print("Ganó el agente")

def validateCols():
    global col1
    global col2
    global col3
    if(col1<0):
        col1=0
    if(col2<0):
        col2=0
    if(col3<0):
        col3=0

def control():
    global col1
    global col2
    global col3
    done = False
    print("En este juego se deben retirar cualquier cantidad de fichas de una columna, pero solo una columna por turno. El jugador que retira la última ficha pierde.")
    # turn= r.randint(0,1) #1 es agente, 0 es jugador
    turn = 1  # , para debugging donde el jugador empieza
    while (not done):
        validateCols()
        printBoard()
        if (bool(turn)):
            if ((col1 == 0 and col2 == 0 and col3 == 1)):
                col, num = 3, 1
                done = True
                print("Bot: Retiro " + str(num) +
                      " fichas de la columna " + str(col))
                print("Bot: Bien jugado! :)")
                modifyBoard(col, num)
                endgame(1)
                break
            elif ((col1 == 0 and col2 == 1 and col3 == 0)):
                col, num = 2, 1
                done = True
                print("Bot: Retiro " + str(num) +
                      " fichas de la columna " + str(col))
                print("Bot: Bien jugado! :)")
                modifyBoard(col, num)
                endgame(1)
                break
            elif ((col1 == 1 and col2 == 0 and col3 == 0)):
                col, num = 1, 1
                done = True
                print("Bot: Retiro " + str(num) +
                      " fichas de la columna " + str(col))
                print("Bot: Bien jugado! :)")
                modifyBoard(col, num)
                endgame(1)              
                break
            else:
                col, num = agente(col1, col2, col3)
                print("Bot: Retiro " + str(num) +
                      " fichas de la columna " + str(col))
                modifyBoard(col, num)
                turn = not turn
                
        else:
            print("Es tu turno")
            print(f"El nimsum es {nimSum()}")
            print("Ingresa la columna")
            col = int(input())
            print("Ingresa la cantidad de fichas a retirar")
            num = int(input())
            modifyBoard(col, num)
            turn = not turn
        if (col1 == 0 and col2 == 0 and col3 == 0):
            done = True
            endgame(not turn)

    print("¿rejugar? (s/n)")
    if (input() == "s"):
        col1 = 3
        col2 = 5
        col3 = 7
        control()
        
if __name__ == '__main__':
    control()