"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    cont = {}
    with open("files/input/data.csv", "r") as data:
        for line in data:
            letters = line.split()[4].split(",")
            for i in letters:
                letter = i.split(":")[0]
                number = int(i.split(":")[1])
                if letter not in cont:
                    cont[letter] = [number]
                else:
                    cont[letter].append(number)
    
    result = []
    for letter in sorted(cont):
        max_value = max(cont[letter])
        min_value = min(cont[letter])
        result.append((letter, min_value, max_value))
    
    return result