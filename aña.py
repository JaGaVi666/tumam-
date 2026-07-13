import random

donas = {
    #Nombre
    "Saturatron" : {"Masa": "chocolate", "Glaseado": "chocolate", "Chispas": "chocolate", "Forma": "sin hueco"},
    "Diabetron" : {"Masa": "Vainilla", "Glaseado": "crema", "Chispas": "colores", "Forma": "con hueco"},
    "Unigordio" : {"Masa": "Vainilla", "Glaseado": "frutilla", "Chispas": "colores", "Forma": "con hueco.", "Adorno": "cuerno dulce"}
}

opc = random.randint(1,3)
match opc:
    case 1:
        print(donas["Saturatron"])
    case 2:
        print(donas["Diabetron"])
    case 3:
        print(donas["Unigordio"])
a = len(donas) - 1 
for dona in donas:
    print(dona, donas[dona])

def crear():
    print("Creando pedido. . .")
    primer = random.randint(1,3)
    a = random.randint (1,10)
    b = 0
    c = 0
    pedidos =[a]
    if primer > 1:
        b = random.randint (1,10)
        pedidos.append(b)
    if primer > 2:
        c = random.randint (1,10)
        pedidos.append(c)
    print("Pedido creado.")
    return pedidos

def leerpedido(pedido):
    vuelta = 0
    print("El cliente pidió: ")
    for dona in donas:
        if pedido[vuelta] > 0:
            vuelta = vuelta + 1
            print(pedido[vuelta], " donas de ", dona)

def creardona (numero):
    for dona in donas:
        if numero == 

while True:
    try:
        print("1 = crear pedido / 2 = ver pedido/ 3 = crear donas / 4 = entregar donas")
        opcion = int(input("¿Qué harás?: "))
    except:
        print("Solo interactuar con números.")
    else:
        match opcion:
            case 1:
                pedido = crear()
            
            case 2:
                while True:
                    try:
                        leerpedido(pedido)
                    except:
                        print("No hay pedidos.")
                        break
                    else:
                        break
            
            case 3:
                while True:
                    contador = 0
                    for dona in donas: 
                        contador = contador + 1
                        print(contador , " = ",dona)
                    try:
                        opcdona = int(input("¿Que dona hará?: "))
                    except:
                        print("Solo interactuar con números.")
                    else:
                        match opcdona:
                            case 1:









