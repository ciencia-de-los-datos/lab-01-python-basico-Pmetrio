"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.

"""
def lectura_de_documento():
    import csv 
    #leer doc csv
    archivo_csv="data.csv"
    with open (archivo_csv,"r") as file:
        lista_texto=file.readlines()
#organizar los datos
    lista_texto=[i.replace("\n","") for i in lista_texto]
    lista_texto=[i.split("\t") for i in lista_texto]
    return lista_texto


# def pregunta_01():
#     """
#     Retorne la suma de la segunda columna.
#         def
#     Rta/
#     214

#     """
#     return
def pregunta_01():
    lectura_texto = lectura_de_documento()
    respuesta=0
    for lista_interna in lectura_texto:
        respuesta += int(lista_interna[1])

    return respuesta
#imprimir resultado pregunta_01()
print (pregunta_01())



def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordenadas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    list_text = lectura_de_documento()
    
    lista = []
    diccionario = {}

    for i in list_text:
        lista.append((i[0], 1))
        lista = sorted(lista, key=lambda x: x[0])
    
    for key, value in lista:
        if key not in diccionario.keys():
            diccionario[key] = []
        diccionario[key].append(value)

    respuesta = []

    for key, value in diccionario.items():
        respuesta.append((key, sum(value)))
    
    return respuesta


# def pregunta_03():
#     """
#     Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
#     de tuplas (letra, suma) ordendas alfabeticamente.

#     Rta/
#     [
#         ("A", 53),
#         ("B", 36),
#         ("C", 27),
#         ("D", 31),
#         ("E", 67),
#     ]

#     """
#     return
def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    list_text = lectura_de_documento()
    
    lista = []
    diccionario = {}

    for i in list_text:
        lista.append((i[0], int(i[1])))
        lista = sorted(lista, key=lambda x: x[0])
    
    for key, value in lista:
        if key not in diccionario.keys():
            diccionario[key] = []
        diccionario[key].append(value)

    respuesta = []

    for key, value in diccionario.items():
        respuesta.append((key, sum(value))) 

    return respuesta
    

# def pregunta_04():
#     """
#     La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
#     registros por cada mes, tal como se muestra a continuación.

#     Rta/
#     [
#         ("01", 3),
#         ("02", 4),
#         ("03", 2),
#         ("04", 4),
#         ("05", 3),
#         ("06", 3),
#         ("07", 5),
#         ("08", 6),
#         ("09", 3),
#         ("10", 2),
#         ("11", 2),
#         ("12", 3),
#     ]

#     """
#     return
def pregunta_04():
    lectura_texto = lectura_de_documento()
    conteo_meses = {}

    for lista_interna in lectura_texto:
        fecha = lista_interna[2]
        mes = fecha.split("-")[1]
        conteo_meses[mes] = conteo_meses.get(mes, 0) + 1

    lista_tuplas = [(mes.zfill(2), cantidad) for mes, cantidad in conteo_meses.items()]
    lista_tuplas_ordenadas = sorted(lista_tuplas)

    return lista_tuplas_ordenadas

# Imprimir el resultado de pregunta_04()
print(pregunta_04())

# def pregunta_05():
#     """
#     Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
#     letra de la columa 1.

#     Rta/
#     [
#         ("A", 9, 2),
#         ("B", 9, 1),
#         ("C", 9, 0),
#         ("D", 8, 3),
#         ("E", 9, 1),
#     ]

#     """
#     return
def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """    
    list_text =lectura_de_documento()
       
    lista = []
    diccionario = {}

    for i in list_text:        
        lista.append((i[0], int(i[1])))
        lista = sorted(lista, key=lambda x: x[0])
        
    for key, value in lista:
        if key not in diccionario.keys():
            diccionario[key] = []
        diccionario[key].append(value)

    respuesta = []

    for key, value in diccionario.items():
        respuesta.append((key, max(value), min(value)))
    
    return respuesta

# def pregunta_06():
#     """
#     La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
#     una clave y el valor despues del caracter `:` corresponde al valor asociado a la
#     clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
#     grande computados sobre todo el archivo.

#     Rta/
#     [
#         ("aaa", 1, 9),
#         ("bbb", 1, 9),
#         ("ccc", 1, 10),
#         ("ddd", 0, 9),
#         ("eee", 1, 7),
#         ("fff", 0, 9),
#         ("ggg", 3, 10),
#         ("hhh", 0, 9),
#         ("iii", 0, 9),
#         ("jjj", 5, 17),
#     ]

#     """
#     return
def pregunta_06():
    lectura_texto = lectura_de_documento()
    valores_extremos_por_clave = {}

    for lista_interna in lectura_texto:
        diccionario_codificado = lista_interna[4]

        # Decodificar el diccionario codificado en la columna 5
        diccionario_decodificado = {}
        parejas = diccionario_codificado.split(',')
        for pareja in parejas:
            clave, valor = pareja.split(':')
            diccionario_decodificado[clave] = int(valor)

        # Actualizar los valores extremos por clave
        for clave, valor in diccionario_decodificado.items():
            if clave not in valores_extremos_por_clave:
                valores_extremos_por_clave[clave] = [valor, valor]
            else:
                valores_extremos_por_clave[clave][0] = min(valores_extremos_por_clave[clave][0], valor)
                valores_extremos_por_clave[clave][1] = max(valores_extremos_por_clave[clave][1], valor)

    # Ordenar los resultados alfabéticamente por clave
    lista_resultados_ordenados = sorted(valores_extremos_por_clave.items())

    # Convertir el diccionario a una lista de tuplas (clave, valor_min, valor_max)
    lista_tuplas_resultados = [(clave, valores[0], valores[1]) for clave, valores in lista_resultados_ordenados]

    return lista_tuplas_resultados

# Imprimir el resultado de pregunta_06()
print(pregunta_06())

# def pregunta_07():
#     """
#     Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
#     valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
#     a dicho valor de la columna 2.

#     Rta/
#     [
#         (0, ["C"]),
#         (1, ["E", "B", "E"]),
#         (2, ["A", "E"]),
#         (3, ["A", "B", "D", "E", "E", "D"]),
#         (4, ["E", "B"]),
#         (5, ["B", "C", "D", "D", "E", "E", "E"]),
#         (6, ["C", "E", "A", "B"]),
#         (7, ["A", "C", "E", "D"]),
#         (8, ["E", "D", "E", "A", "B"]),
#         (9, ["A", "B", "E", "A", "A", "C"]),
#     ]

#     """
#     return
def pregunta_07():
   
    list_text = lectura_de_documento()
    
    lista = []
    diccionario = {}

    for i in list_text:
        lista.append((int(i[1]), i[0]))
        lista = sorted(lista, key=lambda x: x[0])
        
    for key, value in lista:
        if key not in diccionario.keys():
            diccionario[key] = []
        diccionario[key].append(value)

    respuesta = []

    for key, value in diccionario.items():
        respuesta.append((key, value))
        
    return respuesta

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    list_text = lectura_de_documento()
    
    lista = []
    diccionario  ={}

    for i in list_text:
        lista.append((int(i[1]), i[0]))
        lista = sorted(lista, key=lambda x: x[1])
        lista = sorted(lista, key=lambda x: x[0])
        
    for key, value in lista:
        
        if key not in diccionario.keys():
            diccionario[key] = []    
        
        diccionario[key].append(value)
        
    respuesta = []

    for key, value in diccionario.items():
        value = list(set(value))
        values = "".join(value)
        values = sorted(values)
        respuesta.append((key, values))
    
    return respuesta

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    list_text = lectura_de_documento()
    
    lista = [i[4].split(",") for i in list_text[0:]]

    diccionario = {}
    list_P3 = []

    for i in lista:
        for j in i:
            list_P2 = tuple(j.split(":"))
            list_P3.append(list_P2)

    list_P3 = sorted(list_P3, key=lambda x: x[0])
    
    for key, value in list_P3:
        if key not in diccionario.keys():
            diccionario[key] = []
        diccionario[key].append((len(value)))
        
    list_Prob = []
    
    for key, value in diccionario.items():
        list_P = len(value)
        list_Prob.append((key, list_P))
                
    respuesta = {key:value for key, value in list_Prob}

    return respuesta


# def pregunta_10():
#     """
#     Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
#     cantidad de elementos de las columnas 4 y 5.

#     Rta/
#     [
#         ("E", 3, 5),
#         ("A", 3, 4),
#         ("B", 4, 4),
#         ...
#         ("C", 4, 3),
#         ("E", 2, 3),
#         ("E", 3, 3),
#     ]


#     """
#     return
def pregunta_10():
    lectura_texto = lectura_de_documento()
    lista_tuplas = []

    for fila in lectura_texto:
        letra_columna1 = fila[0]
        cantidad_columna4 = len(fila[3].split(',')) if fila[3] else 0
        cantidad_columna5 = len(fila[4].split(',')) if fila[4] else 0
        lista_tuplas.append((letra_columna1, cantidad_columna4, cantidad_columna5))

    return lista_tuplas

# Imprimir el resultado de pregunta_10()
print(pregunta_10())

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    list_text = lectura_de_documento()
        
    lista = []
    diccionario ={}

    for i in list_text:        
        lista.append((i[3].split(","), int(i[1])))
        
    list_tupla = []

    for key, value in lista:        
        for i in key:
            list_tupla.append((i, value))            

    list_tupla = sorted(list_tupla, key=lambda x: x[0])

    for key, value in list_tupla:
        if key not in diccionario.keys():
            diccionario[key] = []
        diccionario[key].append(value)
    
    list_prob = []
    respuesta = {}

    for key, value in diccionario.items():
            list_prob.append((key, sum(value)))    

    respuesta = {key:value for key, value in list_prob}

    return respuesta

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    list_text = lectura_de_documento()
    
    lista = []
    diccionario ={}

    for i in list_text:
        
        lista.append((i[0], i[4].split(",") ))         

    list_tupla = []
    list_tupla_2 = []
    
    for key, value in lista:        
        for i in value:
            list_tupla.append((key, i.split(":")))
            
    for key, value in list_tupla:
        list_tupla_2.append((key, int(value[1])))

    list_tupla_2 = sorted(list_tupla_2, key=lambda x: x[0])

    for key, value in list_tupla_2:
        if key not in diccionario.keys():
            diccionario[key] = []
        diccionario[key].append(value)
        
    list_Prob = []

    for key, value in diccionario.items():
            list_Prob.append((key, sum(value)))

    respuesta = {key:value for key, value in list_Prob}    

    return respuesta

def lectura_documento():
    
    # ================== Lectura del documento csv =============================
    directory = "data.csv"
    with open(directory, "r") as file:
        list_text = file.readlines()        
    
    # =================== Eliminación de líneas de carro y tabuladores ========= 
    list_text = [i.replace("\n", "") for i in list_text]
    list_text = [i.split("\t") for i in list_text]
    
    return list_text