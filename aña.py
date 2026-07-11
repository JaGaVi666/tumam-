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
