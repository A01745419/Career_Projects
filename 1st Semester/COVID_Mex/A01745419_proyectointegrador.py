# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:33:50 2020

@author: jlms3
"""
# Proyecto Integrador de Pensamiento computacional para ingeniería 
# José Luis Madrigal Sánchez
# A01745419
from matplotlib import pyplot as plt
import statistics as stats
def archivo_buscar(numero_caso):
    '''
    Este es el docstring del método de buscar un archivo que analizar

    Parameters
    ----------
    numero_caso : int
        número del caso que fue elegido.

    Returns
    -------
    archivo : str
        archivo a usar en csv.

    '''
    if numero_caso == 2:
        archivo = "Casos_Diarios_Estado_Nacional_Confirmados_20200927.csv"
    elif numero_caso == 3:
        archivo = "Casos_Diarios_Estado_Nacional_Defunciones_20200927.csv"
    elif numero_caso == 4:
        archivo = "Casos_Diarios_Estado_Nacional_Negativos_20200927.csv"
    elif numero_caso == 5:
        archivo = "Casos_Diarios_Estado_Nacional_Sospechosos_20200927.csv" 
    return archivo
def estado_buscar(archivo, numero_estado):
    '''
    Este es el docstring para el método de encontrar los datos de un estado

    Parameters
    ----------
    archivo : str
        archivo del caso en csv.
    numero_estado : int
        número del estado que fue elegido.

    Returns
    -------
    renglon : list
        lista de los numeros de casos que hubo en todas las fechas.

    '''    
    with open (archivo) as archivo:
        texto = archivo.readlines()
        renglon = texto[numero_estado]
        renglon = renglon.split(",")
        renglon = renglon[3:]
        renglon = [int(i) for i in renglon]
        return renglon
def tipo_caso(numero_caso):
    '''
    Este es el docstring para el método de generar el tipo de caso

    Parameters
    ----------
    numero_caso : int
        número del caso que fue elegido.

    Returns
    -------
    caso : str
        tipo de caso.

    '''
    if numero_caso == 2:
        caso = " Confirmados"
    elif numero_caso == 3:
        caso = " Defunciones"
    elif numero_caso == 4:
        caso = " Negativos"
    elif numero_caso == 5:
        caso = " Sospechosos"
    elif numero_caso == 1:
        caso = "Todos los casos"
    return caso
def nombre_estado(archivo, numero_estado):
    '''
    Este es el docstring para el método de generar el nombre del estado

    Parameters
    ----------
    archivo : str
        archivo elegido en csv.
    numero_estado : int
        número del estado que fue elegido.

    Returns
    -------
    nombre : str
        nombre del estado.

    '''
    with open (archivo) as archivo:
        texto = archivo.readlines()
        renglon = texto[numero_estado]
        renglon = renglon.split(",")
        nombre = renglon[2]
        return nombre
def color_caso(nombre_caso):
    '''
    Este es el docstring para el método de determinar el color de la gráfica.

    Parameters
    ----------
    nombre_caso : str
        el nombre del caso elegido.

    Returns
    -------
    color : str
        el color para usar en la gráfica.

    '''
    if nombre_caso == " Confirmados":
        color = "blue"
    elif nombre_caso == " Defunciones":
        color = "red"
    elif nombre_caso == " Negativos":
        color = "green"
    elif nombre_caso == " Sospechosos":
        color = "orange"
    return color    
def fechas(archivo):
    '''
    Este es el docstring para el método de encontrar las fechas en el archivo.

    Parameters
    ----------
    archivo : str
        el archivo a usar.

    Returns
    -------
    renglon : list
        las fechas que se encuentran en el archivo.

    '''
    with open (archivo) as archivo:
        texto = archivo.readlines()
        renglon = texto[0]
        renglon = renglon.split(",")
        renglon = renglon[3:]
        return renglon
def grafica_por_caso(x, y, nombre_caso, nombre_estado, color_caso):
    '''
    Este es el docstring para generar la gráfica de un caso específico. 

    Parameters
    ----------
    x : list
        eje x, que son las fechas.
    y : list
        eje y, que son los casos.
    nombre_caso : str
        el nombre del caso que fue elegido.
    nombre_estado : str
        el nombre del estado que fue elegido.
    color_caso : str
        el color a usar dependiendo del tipo de caso.

    Returns
    -------
    None. (solo muestra la gráfica)

    '''
    plt.style.use("ggplot")
    plt.bar(x, y, color = color_caso,label = "Casos por día")
    plt.legend()
    plt.title("Casos" + nombre_caso + nombre_estado)
    plt.xlabel("Fecha")
    plt.ylabel("Casos")
    plt.tight_layout()
    plt.show()
def grafica_todos(x1, x2, x3, x4, y1, y2, y3, y4, nombre_caso, nombre_estado):
    '''
    Este es el docstring para el método de generar gráfica de todos los casos

    Parameters
    ----------
    x1 : list
        primer eje x, casos confirmados.
    x2 : list
        segundo eje x, casos defunciones.
    x3 : list
        tercer eje x, casos negativos.
    x4 : list
        cuarto eje x, casos sospechosos.
    y1 : list
        primer eje y, fechas confirmados.
    y2 : list
        segundo eje y, fechas defunciones.
    y3 : list
        tercer eje y, fechas negativos.
    y4 : list
        cuarto eje y, fechas sospechosos.
    nombre_caso : str
        nombre del caso elegido.
    nombre_estado : str
        nombre del estado elegido.

    Returns
    -------
    None. (solo muestra la gráfica)

    '''
    plt.style.use("ggplot")
    plt.plot(x1, y1, color = "blue", linewidth = "1", label = "Confirmados")
    plt.plot(x2, y2, color = "red", linewidth = "1", label = "Defunciones")
    plt.plot(x3, y3, color = "green", linewidth = "1", label = "Negativos")
    plt.plot(x4, y4, color = "orange", linewidth = "1", label = "Sospechosos")
    plt.legend()
    plt.title(nombre_caso + nombre_estado)
    plt.xlabel("Fecha")
    plt.ylabel("Casos")
    plt.tight_layout()
    plt.show()
def estadistica_por_caso(archivo, nombre_caso, numero_estado):
    '''
    Este es el docstring para el método de generar una estadística de un caso, 
    medidas de centralidad y dispersión

    Parameters
    ----------
    archivo : str
        archivo del caso elegido en csv.
    nombre_caso : str
        nombre del caso elegido.
    numero_estado : str
        número del estado elegido.

    Returns
    -------
    TYPE : str
        string con los elementos y cálculos obtenidos.

    '''
    casos = estado_buscar(archivo, numero_estado)
    estado_nombre = nombre_estado(archivo, numero_estado)
    media = stats.mean(casos)
    moda = stats.mode(casos)
    mediana = stats.median(casos)
    varianza = stats.variance(casos)
    desvi_est = stats.stdev(casos)
    media = round(media, 2)
    varianza = round(varianza, 2)
    desvi_est = round(desvi_est, 2)
    media = str(media) + "|"
    moda = str(moda) + "|"
    mediana = str(mediana) + "|"
    varianza = str(varianza) + "|"
    desvi_est = str(desvi_est) + "|"
    return (estado_nombre + nombre_caso + " |Media: " + media + " |Moda: " \
            + moda + " |Mediana: " + mediana + " |Varianza: " + varianza \
                + " |Desviación estándar: " + desvi_est)
def estadistica_todos(numero_estado):
    '''
    Este es el docstring para el método de generar una estadísitca de todos
    los casos, porcentajes y tasa de letalidad

    Parameters
    ----------
    numero_estado : int
        número del estado elegido.

    Returns
    -------
    TYPE : str
        string con los elementos y cálculos obtenidos.

    '''
    archivo1 = archivo_buscar(2)
    archivo2 = archivo_buscar(3)
    archivo3 = archivo_buscar(4)
    archivo4 = archivo_buscar(5)
    casos1 = estado_buscar(archivo1, numero_estado)
    casos2 = estado_buscar(archivo2, numero_estado)
    casos3 = estado_buscar(archivo3, numero_estado)
    casos4 = estado_buscar(archivo4, numero_estado)
    estado_nombre = nombre_estado(archivo1, numero_estado)
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    for i in range (len(casos1)):
        total1 += casos1[i]
    for i in range (len(casos2)):
        total2 += casos2[i]
    for i in range (len(casos3)):
        total3 += casos3[i]
    for i in range (len(casos4)):
        total4 += casos4[i]
    letalidad = (total2 / total1) * 100
    letalidad = round(letalidad, 2)
    letalidad = str(letalidad) + " %"
    total_todos = total1 + total2 + total3 + total4
    porcentaje1 = (total1 * 100) / total_todos
    porcentaje2 = (total2 * 100) / total_todos
    porcentaje3 = (total3 * 100) / total_todos
    porcentaje4 = (total4 * 100) / total_todos
    porcentaje1 = round(porcentaje1, 2)
    porcentaje2 = round(porcentaje2, 2)
    porcentaje3 = round(porcentaje3, 2)
    porcentaje4 = round(porcentaje4, 2)
    string1 = " |Confirmados: " + str(porcentaje1) + " %|"
    string2 = " |Defunciones: " + str(porcentaje2) + " %|"
    string3 = " |Negativos: " + str(porcentaje3) + " %|"
    string4 = " |Sospechosos: " + str(porcentaje4) + " %|"
    string5 = " y tasa de letalidad (defunciones por confirmados): "
    return (estado_nombre + string1 + string2 + string3 + string4 + string5 \
            + letalidad)    
def reporte_por_caso(archivo, nombre_caso, numero_estado):
    '''
    Este es el docstring para el método de generar un reporte de un caso,
    suma total

    Parameters
    ----------
    archivo : str
        archivo del caso elegido en csv.
    nombre_caso : TYPE
        DESCRIPTION.
    numero_estado : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE : str
        string con los elementos y cálculos hechos.

    '''
    casos = estado_buscar(archivo, numero_estado)
    estado_nombre = nombre_estado(archivo, numero_estado)
    total = 0
    for i in range (len(casos)):
        total += casos[i]
    total = str(total)
    return ("El total de casos" + nombre_caso + " en " + estado_nombre + \
            " es: "+ total)
def reporte_todos(numero_estado):
    '''
    Este es el dosctring para el método de genera un reporte de todos los 
    casos, suma total, osea todo lo registrado

    Parameters
    ----------
    numero_estado : int
        número del estado elegido.

    Returns
    -------
    TYPE : str
        string con los elementos y cálculos hechos.

    '''
    archivo1 = archivo_buscar(2)
    archivo2 = archivo_buscar(3)
    archivo3 = archivo_buscar(4)
    archivo4 = archivo_buscar(5)
    casos1 = estado_buscar(archivo1, numero_estado)
    casos2 = estado_buscar(archivo2, numero_estado)
    casos3 = estado_buscar(archivo3, numero_estado)
    casos4 = estado_buscar(archivo4, numero_estado)
    estado_nombre = nombre_estado(archivo1, numero_estado)
    total = 0
    for i in range (len(casos1)):
        total += casos1[i]
    for i in range (len(casos2)):
        total += casos2[i]
    for i in range (len(casos3)):
        total += casos3[i]
    for i in range (len(casos4)):
        total += casos4[i]
    total = str(total)
    return ("Todos los casos registrados en " + estado_nombre + " son: " \
            + total)
def obtener_grafica_por_caso(archivo, nombre_caso, numero_estado):
    '''
    Este es el docstring para el método de obtener una gráfica de un caso, 
    que es de barras

    Parameters
    ----------
    archivo : str
        el archivo del caso elegido en csv.
    nombre_caso : str
        nombre del caso elegido.
    numero_estado : int
        número del estado elegido.

    Returns
    -------
    None. (solo muestra la gráfica)

    '''
    casos = estado_buscar(archivo, numero_estado)
    fecha = fechas(archivo)
    estado_nombre = nombre_estado(archivo, numero_estado)
    color_barra = color_caso(nombre_caso)
    grafica_por_caso(fecha, casos, nombre_caso, estado_nombre, color_barra)
def obtener_grafica_todos(nombre_caso, numero_estado):
    '''
    Este es el docstring para el método de generar una gráfica de todos 
    los casos, que es de dispersión o puntos

    Parameters
    ----------
    nombre_caso : str
        nombre del caso elegido.
    numero_estado : int
        número del caso elegido.

    Returns
    -------
    None. (solo muestra la gráfica)

    '''
    archivo1 = archivo_buscar(2)
    archivo2 = archivo_buscar(3)
    archivo3 = archivo_buscar(4)
    archivo4 = archivo_buscar(5)
    fechas1 = fechas(archivo1)
    fechas2 = fechas(archivo2)
    fechas3 = fechas(archivo3)
    fechas4 = fechas(archivo4)
    casos1 = estado_buscar(archivo1, numero_estado)
    casos2 = estado_buscar(archivo2, numero_estado)
    casos3 = estado_buscar(archivo3, numero_estado)
    casos4 = estado_buscar(archivo4, numero_estado)
    estado_nombre = nombre_estado(archivo1, numero_estado)
    grafica_todos(fechas1, fechas2, fechas3, fechas4, casos1, casos2, casos3,\
                  casos4, nombre_caso, estado_nombre)
# Definir un ciclo infinito y en él,
#   Mostrar la portada y las opciones de consulta (igual la de salida)
#   Pedir que acción se quiere tomar
#   Si la acción es 4,
#       Detener el ciclo
#   Mostrar las opciones de casos (igual la de todos)
#   Pedir el caso que se quiere ver
#   Si el caso es mayor a 1 y menor o igual a 5,
#       Buscar el archivo de ese caso
#   Generar el nombre del caso
#   Mostrar las opciones de estado 
#   Pedir el estado
#   Si la acción es 1 y el caso es mayor a 1 y menor o igual que 5,
#       Mostrar la estadística del caso elegido en el estado elegido
#   Si la acción es 1 y el caso es igual a 1,
#       Mostrar la estadística de todos los casos en el estado elegido
#   Si la acción es 2 y el caso es mayor a 1 y menor o igual que 5,
#       Mostrar el reporte del caso elegido en el estado elegido
#   Si la acción es 2 y el caso es igual a 1,
#       Mostrar el reporte de todos los casos en el estado elegido
#   Si la acción es 3 y el caso es mayor a 1 y menor o igual que 5,
#       Mostrar la gráfica del caso elegido en el estado elegido
#   Si la acción es 3 y el caso es igual a 1,
#       Mostrar la gráfica de todos los casos en el estado elegido
def main():    
    while True:
        print('''
          ##########  ##########  ######    ######  ######  #########
          ##########  ##########  ######    ######  ######  ############
          ####        ###    ###   #####    #####   ######  ######    ###
          ####        ###    ###    ####    ####    ######  ######    ###
          ##########  ##########     ##########     ######  ############
          ##########  ##########      ########      ######  #########
          
          Información de México
          Hecho por José Luis Madrigal
          1 = Estadística 
          2 = Reporte
          3 = Gráfica
          4 = Salir
          Se debe saber que los datos son de 31-12-2019 a 27-09-2020
          ''')
        accion = int(input("Hola, elige una acción: "))
        if accion == 4:
            break
        print('''
          1 = Todos
          2 = Confirmados
          3 = Defunciones
          4 = Negativos 
          5 = Sospechosos
        ''')
        caso = int(input("Elige un caso: "))
        if caso > 1 and caso <= 5:
            archivo = archivo_buscar(caso)
        caso_nombre = tipo_caso(caso)
        print('''
          1 = Aguascalientes         11 = Guanajuato     21 = Puebla
          2 = Baja California        12 = Guerrero       22 = Querétaro
          3 = Baja California Sur    13 = Hidalgo        23 = Quintana Roo
          4 = Campeche               14 = Jalisco        24 = San Luis Potosí
          5 = Chiapas                15 = México         25 = Sinaloa
          6 = Chihuahua              16 = Michoacan      26 = Sonora
          7 = Distrito Federal       17 = Morelos        27 = Tabasco
          8 = Coahuila               18 = Nayarit        28 = Tamaulipas
          9 = Colima                 19 = Nuevo León     29 = Tlaxcala
          10 = Durango               20 = Oaxaca         30 = Veracruz
                                         
                                     31 = Yucatán
                                     32 = Zacatecas
              ''')
        estado = int(input("Elige un estado: "))
        if accion == 1 and caso > 1 and caso <= 5:
            print(estadistica_por_caso(archivo, caso_nombre, estado))
        elif accion == 1 and caso == 1:
            print(estadistica_todos(estado))
        elif accion == 2 and caso > 1 and caso <= 5:
            print(reporte_por_caso(archivo, caso_nombre, estado))
        elif accion == 2 and caso == 1:
            print(reporte_todos(estado))
        elif accion == 3 and caso > 1 and caso <= 5:
            obtener_grafica_por_caso(archivo, caso_nombre, estado)
        elif accion == 3 and caso == 1:
            obtener_grafica_todos(caso_nombre, estado)
            
main()