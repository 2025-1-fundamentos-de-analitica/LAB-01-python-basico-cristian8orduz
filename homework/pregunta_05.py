"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    cont = {}
    with open("files/input/data.csv", "r") as data:
        for line in data:
            letter = line.split()[0]
            number = int(line.split()[1])
            if letter not in cont:
                cont[letter] = [number]
            else:
                cont[letter].append(number)
    
    result = []
    for letter in sorted(cont):
        max_letter = max(cont[letter])
        min_letter = min(cont[letter])
        result.append((letter, max_letter, min_letter))
    
    return result