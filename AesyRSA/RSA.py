#demostración del algoritmo de RSA
#Basado en los siguientes recursos: https://www.askpython.com/python/examples/rsa-algorithm-in-python
#https://www.youtube.com/watch?v=CMe0COxZxb0
#https://en.wikipedia.org/wiki/RSA_(cryptosystem)


#imports
import math

#functions 
def buscaCoprimos(phi):
    global e
    while True:
        if math.gcd(e,phi)==1:
            break
        else:
            e+=1

def encuentraD(e,phi):
    global d
    d=1
    while True:
        if (d*e)%phi==1:
            break
        else:
            d+=1
    return d

def promptMessageProcess():
    print("Escribe el mensaje a encriptar")
    print(f"Las llaves  son (e,n): ({e},{n})")
    msg=input()
    #convierte a ascii
    msg=[ord(c) for c in msg]
    print(f"El mensaje en ascii es {msg}")
    return msg



def ascii_to_string(ascii_list):
    string = "".join([chr(x) for x in ascii_list])
    return string

#escoge dos número primos
p=733
q=863
n=p*q

#calcula la función phi de Euler
phi=(p-1)*(q-1)

#escoge un número e que sea coprimo con phi
e=2 #empezmos en 2 porque 1 no es coprimo con ningún número, inicializamos e
buscaCoprimos(phi)

#calcula d
#d es el inverso multiplicativo de e módulo phi
#es decir, d*e=1 mod phi, con el algoritmo de euclides
d=encuentraD(e,phi)

#ya encontramos la llave pública y privada
#ahora vamos a encriptar un mensaje
msg=promptMessageProcess()

#encripta el mensaje
#C=m^e mod n
c=[(m**e)%n for m in msg]
print(f"El mensaje encriptado es {c}")

#desencripta el mensaje
#m=c^d mod n
m=[(c**d)%n for c in c]

#convierte a ascii
m=ascii_to_string(m)

print(f"El mensaje desencriptado en ascii es {m}")





