"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    result = {}
    with open("files/input/data.csv", "r") as data:
        for line in data:
            pairs = line.split()[4]
            pair = pairs.split(",")
            for letter in pair:
                value, _ = letter.split(":")
                if value in result:
                    result[value] += 1
                else:
                    result[value] = 1

    return dict(sorted(result.items()))