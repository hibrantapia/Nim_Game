import random as r
import tkinter as tk

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
    # print("El nim es  " + str(nimSum()))
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
        if (col1 != 0 and ((col1 ^ nimSum()) < col1)):
            col = 1
            num = col1-(col1 ^ nimSum())
            col1h = col1h-num
        elif (col2 != 0 and ((col2 ^ nimSum()) < col2)):
            col = 2
            num = col2-(col2 ^ nimSum())
            col2h = col2h-num
        elif (col3 != 0 and ((col3 ^ nimSum()) < col3)):
            col = 3
            num = col3-(col3 ^ nimSum())
            col3h = col3h-num

        if (col1h == 0 and col2h == 0 and col3h == 0):
            print("Bot: Final del juego, bien jugado :)")
            num = num-1

        # estoy bastante seguro que hay una mejor forma de hacer esto
        # el chiste es que no se ponga en una situación comprometedora tratando de terminar en una configuración 1 1 0
        if ((col1h == 1 and col2h == 1) or (col1h == 1 and col3h == 1) or (col2h == 1 and col3h == 1)):
            if (col1 > 1):
                num = col1-1
                col = 1
            elif (col2 > 1):
                num = col2-1
                col = 2
            elif (col3 > 1):
                num = col3-1
                col = 3
        if (col1 == 0 or col2 == 0 or col3 == 0):
            if (col1 == 1 or col2 == 1 or col3 == 1):
                # este caso cubre el caso n, 1, 0
                # el agente debe comer la fila n completa para forzar la victoria
                if (col1 > 1):
                    col = 1
                    num = col1
                elif (col2 > 1):
                    col = 2
                    num = col2
                elif (col3 > 1):
                    col = 3
                    num = col3
        # if (col1h+col2h+col3h == 2):
         #   num += 1
    return col, num


def start():
    print("En este juego se deben retirar cualquier cantidad de fichas de una columna, pero solo una columna por turno. El jugador que retira la última ficha pierde.")
    printBoard()

def turnoJugador():
    col_limits = {1: col1, 2: col2, 3: col3}
    col, num = 0, 0
    print("Es tu turno")
    #verify col and num are integers, col is between 1 and 3, num is between 1 and col{1,2,3}
    col,num= verify(col,num)

    return col, num

def verify(col, num):
    col_limits = {1: col1, 2: col2, 3: col3}
    while True:
        try:
            col = int(input("Ingresa una columna no vacía (1-3): "))
            try:
                num = int(input(f"Ingresa una cantidad de fichas válida (1-{col_limits[col]}): "))
            except KeyError:
                print("Por favor ingresa una columna válida.")
                continue
        except ValueError:
            print("Por favor ingresa un número entero de una columna no vacía.")
            continue
        else:
            if col < 1 or col > 3 or num < 1 or num > col_limits[col]:
                print("Por favor ingresa valores válidos.")
            else:
                return int(col), int(num)



def endgame(turn):
    if (turn):
        print("Ganó el jugador")
    else:
        print("Ganó el agente")


def control():
    global col1
    global col2
    global col3
    done = False
    start()
    turn = r.randint(0, 1)  # 1 es agente, 0 es jugador
    # turn = 0  # , para debugging donde el jugador empieza
    while (not done):
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
            col,num= turnoJugador()
            #print(f"col: {col}, num: {num}")
            modifyBoard(int(col),int(num))
            turn=not turn
        printBoard()
        if (col1 == 0 and col2 == 0 and col3 == 0):
            done = True
            endgame(not turn)

    print("¿rejugar? (s/n)")
    if (input() == "s"):
        col1 = 3
        col2 = 5
        col3 = 7
        control()


class NimGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Juego de Nim")
        self.geometry("400x470")

        self.label = tk.Label(self, text="Juego de Nim", font=("Arial", 16))
        self.label.pack(pady=10)
        
        self.description_label = tk.Label(self, wraplength=350, text="En este juego se deben retirar cualquier cantidad de asteriscos de una fila, pero solo una fila por turno. El jugador que retira el último asterisco pierde. \n Jugarás contra un agente inteligente.", font=("Arial", 12))
        self.description_label.pack(pady=10)
        

        self.board_label = tk.Label(self, font=("Arial", 12))
        self.board_label.pack(pady=5)
        self.update_board_label()
        
        self.status_label = tk.Label(self, font=("Arial", 12))
        self.status_label.pack(pady=5)
        
        self.column_label = tk.Label(self, text="Fila:", font=("Arial", 12))
        self.column_label.pack(pady=5)

        self.column_entry = tk.Entry(self)
        self.column_entry.pack(pady=5)
        
        self.tokens_label = tk.Label(self, text="Número de Asteriscos:", font=("Arial", 12))
        self.tokens_label.pack(pady=5)

        self.tokens_entry = tk.Entry(self)
        self.tokens_entry.pack(pady=5)

        self.submit_button = tk.Button(self, text="Enviar Movimiento", command=self.submit_move)
        self.submit_button.pack(pady=5)
        
        self.reset_button = tk.Button(self, text="Reiniciar Juego", command=self.reset_game)
        self.reset_button.pack(pady=5)

    def update_board_label(self):
        board_text = f"1. {' * ' * col1}\n2. {' * ' * col2}\n3. {' * ' * col3}"
        self.board_label.config(text=board_text, font=("Arial", 12))
        
    def reset_game(self):
        global col1, col2, col3
        col1 = 3
        col2 = 5
        col3 = 7
        self.update_board_label()
        self.status_label.config(text="El juego se ha reiniciado.")

    def submit_move(self):
        col = int(self.column_entry.get())
        num = int(self.tokens_entry.get())

        if col not in {1, 2, 3} or num < 1 or num > {1: col1, 2: col2, 3: col3}[col]:
            self.status_label.config(text="Movimiento inválido. Por favor intentalo de nuevo.")
            return

        modifyBoard(col, num)
        self.update_board_label()
        self.status_label.config(text="Your move was submitted.")

        if col1 == 0 and col2 == 0 and col3 == 0:
            self.status_label.config(text="¡Perdiste! Todos los asteriscos fueron tomados.")
            return

        col, num = agente(col1, col2, col3)
        modifyBoard(col, num)
        self.update_board_label()
        self.status_label.config(text=f"El agente tomó {num} asterisco(s) de la fila {col}.")

        if col1 == 0 and col2 == 0 and col3 == 0:
            self.status_label.config(text="¡Ganaste! El agente tomó el último asterisco.")

if __name__ == "__main__":
    app = NimGUI()
    app.mainloop()