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
    if primer > 1:
        b = random.randint (1,10)
    if primer > 2:
        c = random.randint (1,10)
    pedidos = [a, b, c]
    return pedidos

def leerpedido(pedido):
    vuelta = 0
    print("El cliente pidió: ")
    for dona in donas:
        if pedido[vuelta] > 0:
            vuelta = vuelta + 1
            print(pedido[vuelta], " donas de ", dona)



while True:
    try:
        opcion = int(input("¿Qué harás?: "))
    except:
        print("Solo interactuar con números.")
    else:
        match opcion:
            case 1:
                pedido = crear()







