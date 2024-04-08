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



# def pregunta_02():
#     """
#     Retorne la cantidad de registros por cada letra de la primera columna como la lista
#     de tuplas (letra, cantidad), ordenadas alfabéticamente.

#     Rta/
#     [
#         ("A", 8),
#         ("B", 7),
#         ("C", 5),
#         ("D", 6),
#         ("E", 14),
#     ]

#     """
#     return
def pregunta_02():
    lectura_texto = lectura_de_documento()
    conteo_letras = {}

    for lista_interna in lectura_texto:
        primera_letra = lista_interna[0][0].lower()
        conteo_letras[primera_letra] = conteo_letras.get(primera_letra, 0) + 1

    lista_tuplas_ordenadas = sorted(conteo_letras.items())
    
    return lista_tuplas_ordenadas

# Imprimir el resultado de pregunta_02()
print(pregunta_02())



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
    lectura_texto = lectura_de_documento()
    suma_por_letra = {}

    for lista_interna in lectura_texto:
        letra = lista_interna[0][0].lower()
        valor_columna2 = int(lista_interna[1])  # Suponiendo que los valores son enteros en la columna 2
        suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor_columna2

    lista_tuplas_ordenadas = sorted(suma_por_letra.items())
    
    return lista_tuplas_ordenadas

# Imprimir el resultado de pregunta_03()
print(pregunta_03())
    

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
    lectura_texto = lectura_de_documento()
    max_min_por_letra = {}

    for lista_interna in lectura_texto:
        letra = lista_interna[0][0].lower()
        valor_columna2 = int(lista_interna[1])  # Suponiendo que los valores son enteros en la columna 2
        if letra not in max_min_por_letra:
            max_min_por_letra[letra] = (valor_columna2, valor_columna2)
        else:
            max_min_por_letra[letra] = (max(max_min_por_letra[letra][0], valor_columna2),
                                         min(max_min_por_letra[letra][1], valor_columna2))

    lista_tuplas = sorted([(letra, max_valor, min_valor) for letra, (max_valor, min_valor) in max_min_por_letra.items()])

    return lista_tuplas

# Imprimir el resultado de pregunta_05()
print(pregunta_05())

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
    lectura_texto = lectura_de_documento()
    asociaciones = {}

    for fila in lectura_texto:
        valor_columna1 = fila[0]
        valor_columna2 = fila[1]
        
        if valor_columna2 not in asociaciones:
            asociaciones[valor_columna2] = [valor_columna1]
        else:
            asociaciones[valor_columna2].append(valor_columna1)

    lista_tuplas_asociadas = [(valor, valores) for valor, valores in asociaciones.items()]
    
    # Ordenar la lista de tuplas por el valor numérico de la columna 2
    lista_tuplas_asociadas = sorted(lista_tuplas_asociadas, key=lambda x: int(x[0]) if x[0].isdigit() else float('inf'))

    return lista_tuplas_asociadas

# Imprimir el resultado de pregunta_07()
print(pregunta_07())

# def pregunta_08():
#     """
#     Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
#     de la segunda columna; la segunda parte de la tupla es una lista con las letras
#     (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
#     valor de la segunda columna.

#     Rta/
#     [
#         (0, ["C"]),
#         (1, ["B", "E"]),
#         (2, ["A", "E"]),
#         (3, ["A", "B", "D", "E"]),
#         (4, ["B", "E"]),
#         (5, ["B", "C", "D", "E"]),
#         (6, ["A", "B", "C", "E"]),
#         (7, ["A", "C", "D", "E"]),
#         (8, ["A", "B", "D", "E"]),
#         (9, ["A", "B", "C", "E"]),
#     ]

#     """
#     return
def pregunta_08():
    lectura_texto = lectura_de_documento()
    asociaciones = {}

    for fila in lectura_texto:
        valor_columna1 = fila[0]
        valor_columna2 = fila[1]

        if valor_columna2 not in asociaciones:
            asociaciones[valor_columna2] = [valor_columna1]
        else:
            asociaciones[valor_columna2].append(valor_columna1)

    lista_tuplas = []
    for valor, letras in sorted(asociaciones.items(), key=lambda x: int(x[0]) if x[0].isdigit() else float('inf')):
        letras_ordenadas_sin_repeticiones = sorted(set(letras))
        lista_tuplas.append((valor, letras_ordenadas_sin_repeticiones))

    return lista_tuplas

# Imprimir el resultado de pregunta_08()
print(pregunta_08())

# def pregunta_09():
#     """
#     Retorne un diccionario que contenga la cantidad de registros en que aparece cada
#     clave de la columna 5.

#     Rta/
#     {
#         "aaa": 13,
#         "bbb": 16,
#         "ccc": 23,
#         "ddd": 23,
#         "eee": 15,
#         "fff": 20,
#         "ggg": 13,
#         "hhh": 16,
#         "iii": 18,
#         "jjj": 18,
#     }

#     """
#     return
def contar_registros_columna_5():
    lectura_texto = lectura_de_documento()
    conteo = {}

    for fila in lectura_texto:
        clave_columna5 = fila[4]

        if clave_columna5 not in conteo:
            conteo[clave_columna5] = 1
        else:
            conteo[clave_columna5] += 1

    # Asegurarse de que todas las claves estén presentes en el diccionario
    claves_presentes = conteo.keys()
    claves_a_agregar = set(["aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg", "hhh", "iii", "jjj"]) - set(claves_presentes)
    for clave in claves_a_agregar:
        conteo[clave] = 0

    return conteo

# Imprimir el resultado de contar_registros_columna_5()
print(contar_registros_columna_5())



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

# def pregunta_11():
#     """
#     Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
#     columna 4, ordenadas alfabeticamente.

#     Rta/
#     {
#         "a": 122,
#         "b": 49,
#         "c": 91,
#         "d": 73,
#         "e": 86,
#         "f": 134,
#         "g": 35,
#     }


#     """
#     return

def sumar_columna_2_por_letra_columna_4():
    lectura_texto = lectura_de_documento()
    suma_por_letra = {}

    for fila in lectura_texto:
        letra_columna4 = fila[3]
        suma_columna2 = int(fila[1])

        if letra_columna4 not in suma_por_letra:
            suma_por_letra[letra_columna4] = suma_columna2
        else:
            suma_por_letra[letra_columna4] += suma_columna2

    suma_por_letra_ordenada = dict(sorted(suma_por_letra.items()))

    return suma_por_letra_ordenada

# Imprimir el resultado de sumar_columna_2_por_letra_columna_4()
print(sumar_columna_2_por_letra_columna_4())

# def pregunta_12():
#     """
#     Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
#     los valores de la columna 5 sobre todo el archivo.

#     Rta/
#     {
#         'A': 177,
#         'B': 187,
#         'C': 114,
#         'D': 136,
#         'E': 324
#     }

#     """
#     return
def suma_columna_5_por_letra_columna_1():
    lectura_texto = lectura_de_documento()
    suma_por_letra = {}

    for fila in lectura_texto:
        letra_columna1 = fila[0]
        valores_columna5 = fila[4].split(',')
        
        suma = 0
        for valor in valores_columna5:
            valor_numerico = int(valor.split(':')[1])
            suma += valor_numerico

        if letra_columna1 not in suma_por_letra:
            suma_por_letra[letra_columna1] = suma
        else:
            suma_por_letra[letra_columna1] += suma

    return suma_por_letra

# Imprimir el resultado de suma_columna_5_por_letra_columna_1()
print(suma_columna_5_por_letra_columna_1())