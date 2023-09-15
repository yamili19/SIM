from math import *
from copy import deepcopy
import random
import customtkinter
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from tkinter import ttk
import tkinter as tk
class vectDatos:
    def __init__(self, evento, reloj,
                 rndtiempollegadatipo1, tiempollegadatipo1, horallegadatipo1,
                 rndtiemposerviciotipo1, tiemposerviciotipo1, horaserviciotipo1,
                 rndtiempollegadatipo2, tiempollegadatipo2, horallegadatipo2,
                 rndtiemposerviciotipo2, tiemposerviciotipo2, horaserviciotipo2,
                 rndtiempollegadatipo3, tiempollegadatipo3, horallegadatipo3,
                 rndtiemposerviciotipo3, tiemposerviciotipo3, horaserviciotipo3,
                 rndtiempollegadatipo4, tiempollegadatipo4, horallegadatipo4,
                 rndtiemposerviciotipo4, tiemposerviciotipo4, horaserviciotipo4,
                 rndtiempollegadatipo5, tiempollegadatipo5, horallegadatipo5,
                 rndtiemposerviciotipo5, tiemposerviciotipo5, horaserviciotipo5,
                 rndtiempollegadatipo6, tiempollegadatipo6, horallegadatipo6,
                 rndtiemposerviciotipo6, tiemposerviciotipo6, horaserviciotipo6,
                 rndtiempollegadatipo7, tiempollegadatipo7, horallegadatipo7,
                 rndtiemposerviciotipo7, tiemposerviciotipo7, horaserviciotipo7,
                 rndtiempollegadatipo8, tiempollegadatipo8, horallegadatipo8,
                 rndtiemposerviciotipo8, tiemposerviciotipo8, horaserviciotipo8,
                 zona1, zona2, zona3, zona4, zona5, zona6, zona7, zona8,
                 colazona1, colazona2, colazona3, colazona4, colazona5, colazona6, colazona7, colazona8,
                 colaTotal,
                 cantidadsemanas, cantidadsobrecargas, cantLlegadas, porcentajesobrecargas, ampliar,
                 objetocamion):
        # inicio
        self.evento = evento
        self.reloj = reloj

        # llegadas tipo 1
        self.rndtiempollegadatipo1 = rndtiempollegadatipo1
        self.tiempollegadatipo1 = tiempollegadatipo1
        self.horallegadatipo1 = horallegadatipo1

        # llegadas tipo 2
        self.rndtiempollegadatipo2 = rndtiempollegadatipo2
        self.tiempollegadatipo2 = tiempollegadatipo2
        self.horallegadatipo2 = horallegadatipo2

        # llegadas tipo 3
        self.rndtiempollegadatipo3 = rndtiempollegadatipo3
        self.tiempollegadatipo3 = tiempollegadatipo3
        self.horallegadatipo3 = horallegadatipo3

        # llegadas tipo 4
        self.rndtiempollegadatipo4 = rndtiempollegadatipo4
        self.tiempollegadatipo4 = tiempollegadatipo4
        self.horallegadatipo4 = horallegadatipo4

        # llegadas tipo 5
        self.rndtiempollegadatipo5 = rndtiempollegadatipo5
        self.tiempollegadatipo5 = tiempollegadatipo5
        self.horallegadatipo5 = horallegadatipo5

        # llegadas tipo 6
        self.rndtiempollegadatipo6 = rndtiempollegadatipo6
        self.tiempollegadatipo6 = tiempollegadatipo6
        self.horallegadatipo6 = horallegadatipo6

        # llegadas tipo 7
        self.rndtiempollegadatipo7 = rndtiempollegadatipo7
        self.tiempollegadatipo7 = tiempollegadatipo7
        self.horallegadatipo7 = horallegadatipo7

        # llegadas tipo 8
        self.rndtiempollegadatipo8 = rndtiempollegadatipo8
        self.tiempollegadatipo8 = tiempollegadatipo8
        self.horallegadatipo8 = horallegadatipo8

        # tiempos de servicio tipo 1
        self.rndtiemposerviciotipo1 = rndtiemposerviciotipo1
        self.tiemposerviciotipo1 = tiemposerviciotipo1
        self.horaserviciotipo1 = horaserviciotipo1

        # tiempos de servicio tipo 2
        self.rndtiemposerviciotipo2 = rndtiemposerviciotipo2
        self.tiemposerviciotipo2 = tiemposerviciotipo2
        self.horaserviciotipo2 = horaserviciotipo2

        # tiempos de servicio tipo 3
        self.rndtiemposerviciotipo3 = rndtiemposerviciotipo3
        self.tiemposerviciotipo3 = tiemposerviciotipo3
        self.horaserviciotipo3 = horaserviciotipo3

        # tiempos de servicio tipo 4
        self.rndtiemposerviciotipo4 = rndtiemposerviciotipo4
        self.tiemposerviciotipo4 = tiemposerviciotipo4
        self.horaserviciotipo4 = horaserviciotipo4

        # tiempos de servicio tipo 5
        self.rndtiemposerviciotipo5 = rndtiemposerviciotipo5
        self.tiemposerviciotipo5 = tiemposerviciotipo5
        self.horaserviciotipo5 = horaserviciotipo5
        # tiempos de servicio tipo 6
        self.rndtiemposerviciotipo6 = rndtiemposerviciotipo6
        self.tiemposerviciotipo6 = tiemposerviciotipo6
        self.horaserviciotipo6 = horaserviciotipo6

        # tiempos de servicio tipo 7
        self.rndtiemposerviciotipo7 = rndtiemposerviciotipo7
        self.tiemposerviciotipo7 = tiemposerviciotipo7
        self.horaserviciotipo7 = horaserviciotipo7

        # tiempos de servicio tipo 8
        self.rndtiemposerviciotipo8 = rndtiemposerviciotipo8
        self.tiemposerviciotipo8 = tiemposerviciotipo8
        self.horaserviciotipo8 = horaserviciotipo8

        # zonas
        self.zona1 = zona1
        self.zona2 = zona2
        self.zona3 = zona3
        self.zona4 = zona4
        self.zona5 = zona5
        self.zona6 = zona6
        self.zona7 = zona7
        self.zona8 = zona8

        # colas en zona
        self.colazona1 = colazona1
        self.colazona2 = colazona2
        self.colazona3 = colazona3
        self.colazona4 = colazona4
        self.colazona5 = colazona5
        self.colazona6 = colazona6
        self.colazona7 = colazona7
        self.colazona8 = colazona8
        self.colaTotal = colaTotal

        # cantidad de semanas
        self.cantidadsemanas = cantidadsemanas

        # cantidad de sobrecargas
        self.cantidadsobrecargas = cantidadsobrecargas

        #cantidada llegadas
        self.cantLlegadas = cantLlegadas

        # porcentaje de sobrecargas
        self.porcentajesobrecargas = porcentajesobrecargas

        self.ampliar = ampliar

        # objeto camión
        self.objetocamion = objetocamion

def determinarMenorTiempo(vectorEstado, i):
    j = 0
    indice = 0
    if i == 1:
        j = 1
    eventos = [vectorEstado[j].horallegadatipo1, vectorEstado[j].horallegadatipo2, vectorEstado[j].horallegadatipo3,
               vectorEstado[j].horallegadatipo4, vectorEstado[j].horallegadatipo5, vectorEstado[j].horallegadatipo6,
               vectorEstado[j].horallegadatipo7, vectorEstado[j].horallegadatipo8, vectorEstado[j].horaserviciotipo1,
               vectorEstado[j].horaserviciotipo2, vectorEstado[j].horaserviciotipo3, vectorEstado[j].horaserviciotipo4,
               vectorEstado[j].horaserviciotipo5, vectorEstado[j].horaserviciotipo6, vectorEstado[j].horaserviciotipo7,
               vectorEstado[j].horaserviciotipo8]
    menor = min(variable for variable in eventos if variable != 0)
    for i in range(len(eventos)):
        if eventos[i] == menor:
            indice = i
            break
    return menor, indice

def determinarEvento(vectorEstado, reloj):
    if vectorEstado.horallegadatipo1 == reloj:
        return "llegadaTipo1"
    elif vectorEstado.horallegadatipo2 == reloj:
        return "llegadaTipo2"
    elif vectorEstado.horallegadatipo3 == reloj:
        return "llegadaTipo3"
    elif vectorEstado.horallegadatipo4 == reloj:
        return "llegadaTipo4"
    elif vectorEstado.horallegadatipo5 == reloj:
        return "llegadaTipo5"
    elif vectorEstado.horallegadatipo6 == reloj:
        return "llegadaTipo6"
    elif vectorEstado.horallegadatipo7 == reloj:
        return "llegadaTipo7"
    elif vectorEstado.horallegadatipo8 == reloj:
        return "llegadaTipo8"
    elif vectorEstado.horaserviciotipo1 == reloj:
        return "finServicioTipo1"
    elif vectorEstado.horaserviciotipo2 == reloj:
        return "finServicioTipo2"
    elif vectorEstado.horaserviciotipo3 == reloj:
        return "finServicioTipo3"
    elif vectorEstado.horaserviciotipo4 == reloj:
        return "finServicioTipo4"
    elif vectorEstado.horaserviciotipo5 == reloj:
        return "finServicioTipo5"
    elif vectorEstado.horaserviciotipo6 == reloj:
        return "finServicioTipo6"
    elif vectorEstado.horaserviciotipo7 == reloj:
        return "finServicioTipo7"
    elif vectorEstado.horaserviciotipo8 == reloj:
        return "finServicioTipo8"
    else:
        return "ftw"

def llegadaTipo1(vectorEstado, indice, l1, sigma, mu):
    j = 0
    if indice == 1:
        j = 1
    vectorEstado[indice].rndtiempollegadatipo1 = float("{:.2f}".format(random.random()))
    while vectorEstado[indice].rndtiempollegadatipo1 == 1:
        vectorEstado[indice].rndtiempollegadatipo1 = float("{:.2f}".format(random.random()))
    vectorEstado[indice].tiempollegadatipo1 = -(l1)*log(1-vectorEstado[indice].rndtiempollegadatipo1)
    vectorEstado[indice].horallegadatipo1 = vectorEstado[indice].reloj + vectorEstado[indice].tiempollegadatipo1
    if vectorEstado[indice].zona1 == "libre":
        rnd1 = float("{:.2f}".format(random.random()))
        rnd2 = float("{:.2f}".format(random.random()))
        while rnd1 == 1 or rnd2 == 1 or rnd1 == 0 or rnd2 == 0:
            rnd1 = float("{:.2f}".format(random.random()))
            rnd2 = float("{:.2f}".format(random.random()))
        numero1 = abs(((-2 * log(rnd1)) ** (1 / 2) * cos(2 * pi * rnd2)) * sigma + mu)
        numero2 = ((-2 * log(rnd1)) ** (1 / 2) * sin(2 * pi * rnd2)) * sigma + mu
        vectorEstado[indice].rndtiemposerviciotipo1 = str(rnd1) + " - " + str(rnd2)
        vectorEstado[indice].tiemposerviciotipo1 = numero1
        vectorEstado[indice].horaserviciotipo1 = vectorEstado[indice].reloj + vectorEstado[indice].tiemposerviciotipo1
        vectorEstado[indice].zona1 = "ocupado"
        vectorEstado[indice].objetocamion.append("EnZona1")
    else:
        vectorEstado[indice].colazona1 += 1
        vectorEstado[indice].objetocamion.append("EnColaZona1")
    return vectorEstado

def llegadaTipo2(vectorEstado, indice, l2, sigma, mu):
    j = 0
    if indice == 1:
        j = 1
    vectorEstado[indice].rndtiempollegadatipo2 = float("{:.2f}".format(random.random()))
    while vectorEstado[indice].rndtiempollegadatipo2 == 1:
        vectorEstado[indice].rndtiempollegadatipo2 = float("{:.2f}".format(random.random()))
    vectorEstado[indice].tiempollegadatipo2 = -(l2) * log(1 - vectorEstado[indice].rndtiempollegadatipo2)
    vectorEstado[indice].horallegadatipo2 = vectorEstado[indice].reloj + vectorEstado[indice].tiempollegadatipo2
    if vectorEstado[indice].zona2 == "libre":
        rnd1 = float("{:.2f}".format(random.random()))
        rnd2 = float("{:.2f}".format(random.random()))
        while rnd1 == 1 or rnd2 == 1 or rnd1 == 0 or rnd2 == 0:
            rnd1 = float("{:.2f}".format(random.random()))
            rnd2 = float("{:.2f}".format(random.random()))
        numero1 = abs(((-2 * log(rnd1)) ** (1 / 2) * cos(2 * pi * rnd2)) * sigma + mu)
        numero2 = ((-2 * log(rnd1)) ** (1 / 2) * sin(2 * pi * rnd2)) * sigma + mu
        vectorEstado[indice].rndtiemposerviciotipo2 = str(rnd1) + " - " + str(rnd2)
        vectorEstado[indice].tiemposerviciotipo2 = numero1
        vectorEstado[indice].horaserviciotipo2 = vectorEstado[indice].reloj + vectorEstado[indice].tiemposerviciotipo2
        vectorEstado[indice].zona2 = "ocupado"
        vectorEstado[indice].objetocamion.append("EnZona2")
    else:
        vectorEstado[indice].colazona2 += 1
        vectorEstado[indice].objetocamion.append("EnColaZona2")
    return vectorEstado

def llegadaTipo3(vectorEstado, indice, l3, sigma, mu):
    j = 0
    if indice == 1:
        j = 1
    vectorEstado[indice].rndtiempollegadatipo3 = float("{:.2f}".format(random.random()))
    while vectorEstado[indice].rndtiempollegadatipo3 == 1:
        vectorEstado[indice].rndtiempollegadatipo3 = float("{:.2f}".format(random.random()))
    vectorEstado[indice].tiempollegadatipo3 = -(l3) * log(1 - vectorEstado[indice].rndtiempollegadatipo3)
    vectorEstado[indice].horallegadatipo3 = vectorEstado[indice].reloj + vectorEstado[indice].tiempollegadatipo3
    if vectorEstado[indice].zona3 == "libre":
        rnd1 = float("{:.2f}".format(random.random()))
        rnd2 = float("{:.2f}".format(random.random()))
        while rnd1 == 1 or rnd2 == 1 or rnd1 == 0 or rnd2 == 0:
            rnd1 = float("{:.2f}".format(random.random()))
            rnd2 = float("{:.2f}".format(random.random()))
        numero1 = abs(((-2 * log(rnd1)) ** (1 / 2) * cos(2 * pi * rnd2)) * sigma + mu)
        numero2 = ((-2 * log(rnd1)) ** (1 / 2) * sin(2 * pi * rnd2)) * sigma + mu
        vectorEstado[indice].rndtiemposerviciotipo3 = str(rnd1) + " - " + str(rnd2)
        vectorEstado[indice].tiemposerviciotipo3 = numero1
        vectorEstado[indice].horaserviciotipo3 = vectorEstado[indice].reloj + vectorEstado[indice].tiemposerviciotipo3
        vectorEstado[indice].zona3 = "ocupado"
        vectorEstado[indice].objetocamion.append("EnZona3")
    else:
        vectorEstado[indice].colazona3 += 1
        vectorEstado[indice].objetocamion.append("EnColaZona3")
    return vectorEstado

def llegadaTipo4(vectorEstado, indice, l4, sigma, mu):
    j = 0
    if indice == 1:
        j = 1
    vectorEstado[indice].rndtiempollegadatipo4 = float("{:.2f}".format(random.random()))
    while vectorEstado[indice].rndtiempollegadatipo4 == 1:
        vectorEstado[indice].rndtiempollegadatipo4 = float("{:.2f}".format(random.random()))
    vectorEstado[indice].tiempollegadatipo4 = -(l4) * log(1 - vectorEstado[indice].rndtiempollegadatipo4)
    vectorEstado[indice].horallegadatipo4 = vectorEstado[indice].reloj + vectorEstado[indice].tiempollegadatipo4
    if vectorEstado[indice].zona4 == "libre":
        rnd1 = float("{:.2f}".format(random.random()))
        rnd2 = float("{:.2f}".format(random.random()))
        while rnd1 == 1 or rnd2 == 1 or rnd1 == 0 or rnd2 == 0:
            rnd1 = float("{:.2f}".format(random.random()))
            rnd2 = float("{:.2f}".format(random.random()))
        numero1 = abs(((-2 * log(rnd1)) ** (1 / 2) * cos(2 * pi * rnd2)) * sigma + mu)
        numero2 = ((-2 * log(rnd1)) ** (1 / 2) * sin(2 * pi * rnd2)) * sigma + mu
        vectorEstado[indice].rndtiemposerviciotipo4 = str(rnd1) + " - " + str(rnd2)
        vectorEstado[indice].tiemposerviciotipo4 = numero1
        vectorEstado[indice].horaserviciotipo4 = vectorEstado[indice].reloj + vectorEstado[indice].tiemposerviciotipo4
        vectorEstado[indice].zona4 = "ocupado"
        vectorEstado[indice].objetocamion.append("EnZona4")
    else:
        vectorEstado[indice].colazona4 += 1
        vectorEstado[indice].objetocamion.append("EnColaZona4")
    return vectorEstado

def llegadaTipo5(vectorEstado, indice, l5, sigma, mu):
    j = 0
    if indice == 1:
        j = 1
    vectorEstado[indice].rndtiempollegadatipo5 = float("{:.2f}".format(random.random()))
    while vectorEstado[indice].rndtiempollegadatipo5 == 1:
        vectorEstado[indice].rndtiempollegadatipo5 = float("{:.2f}".format(random.random()))
    vectorEstado[indice].tiempollegadatipo5 = -(l5) * log(1 - vectorEstado[indice].rndtiempollegadatipo5)
    vectorEstado[indice].horallegadatipo5 = vectorEstado[indice].reloj + vectorEstado[indice].tiempollegadatipo5
    if vectorEstado[indice].zona5 == "libre":
        rnd1 = float("{:.2f}".format(random.random()))
        rnd2 = float("{:.2f}".format(random.random()))
        while rnd1 == 1 or rnd2 == 1 or rnd2 == 0 or rnd1 == 0:
            rnd1 = float("{:.2f}".format(random.random()))
            rnd2 = float("{:.2f}".format(random.random()))
        numero1 = abs(((-2 * log(rnd1)) ** (1 / 2) * cos(2 * pi * rnd2)) * sigma + mu)
        numero2 = ((-2 * log(rnd1)) ** (1 / 2) * sin(2 * pi * rnd2)) * sigma + mu
        vectorEstado[indice].rndtiemposerviciotipo5 = str(rnd1) + " - " + str(rnd2)
        vectorEstado[indice].tiemposerviciotipo5 = numero1
        vectorEstado[indice].horaserviciotipo5 = vectorEstado[indice].reloj + vectorEstado[indice].tiemposerviciotipo5
        vectorEstado[indice].zona5 = "ocupado"
        vectorEstado[indice].objetocamion.append("EnZona5")
    else:
        vectorEstado[indice].colazona5 += 1
        vectorEstado[indice].objetocamion.append("EnColaZona5")
    return vectorEstado

def llegadaTipo6(vectorEstado, indice, l6, sigma, mu):
    j = 0
    if indice == 1:
        j = 1
    vectorEstado[indice].rndtiempollegadatipo6 = float("{:.2f}".format(random.random()))
    while vectorEstado[indice].rndtiempollegadatipo6 == 1:
        vectorEstado[indice].rndtiempollegadatipo6 = float("{:.2f}".format(random.random()))
    vectorEstado[indice].tiempollegadatipo6 = -(l6) * log(1 - vectorEstado[indice].rndtiempollegadatipo4)
    vectorEstado[indice].horallegadatipo6 = vectorEstado[indice].reloj + vectorEstado[indice].tiempollegadatipo4
    if vectorEstado[indice].zona6 == "libre":
        rnd1 = float("{:.2f}".format(random.random()))
        rnd2 = float("{:.2f}".format(random.random()))
        while rnd1 == 1 or rnd2 == 1 or rnd1 == 0 or rnd2 == 0:
            rnd1 = float("{:.2f}".format(random.random()))
            rnd2 = float("{:.2f}".format(random.random()))
        numero1 = abs(((-2 * log(rnd1)) ** (1 / 2) * cos(2 * pi * rnd2)) * sigma + mu)
        numero2 = ((-2 * log(rnd1)) ** (1 / 2) * sin(2 * pi * rnd2)) * sigma + mu
        vectorEstado[indice].rndtiemposerviciotipo6 = str(rnd1) + " - " + str(rnd2)
        vectorEstado[indice].tiemposerviciotipo6 = numero1
        vectorEstado[indice].horaserviciotipo6 = vectorEstado[indice].reloj + vectorEstado[indice].tiemposerviciotipo6
        vectorEstado[indice].zona6 = "ocupado"
        vectorEstado[indice].objetocamion.append("EnZona6")
    else:
        vectorEstado[indice].colazona6 += 1
        vectorEstado[indice].objetocamion.append("EnColaZona6")
    return vectorEstado

def llegadaTipo7(vectorEstado, indice, l7, sigma, mu):
    j = 0
    if indice == 1:
        j = 1
    vectorEstado[indice].rndtiempollegadatipo7 = float("{:.2f}".format(random.random()))
    while vectorEstado[indice].rndtiempollegadatipo7 == 1:
        vectorEstado[indice].rndtiempollegadatipo7 = float("{:.2f}".format(random.random()))
    vectorEstado[indice].tiempollegadatipo7 = -(l7) * log(1 - vectorEstado[indice].rndtiempollegadatipo7)
    vectorEstado[indice].horallegadatipo7 = vectorEstado[indice].reloj + vectorEstado[indice].tiempollegadatipo7
    if vectorEstado[indice].zona7 == "libre":
        rnd1 = float("{:.2f}".format(random.random()))
        rnd2 = float("{:.2f}".format(random.random()))
        while rnd1 == 1 or rnd2 == 1 or rnd1 == 0 or rnd2 == 0:
            rnd1 = float("{:.2f}".format(random.random()))
            rnd2 = float("{:.2f}".format(random.random()))
        numero1 = abs(((-2 * log(rnd1)) ** (1 / 2) * cos(2 * pi * rnd2)) * sigma + mu)
        numero2 = ((-2 * log(rnd1)) ** (1 / 2) * sin(2 * pi * rnd2)) * sigma + mu
        vectorEstado[indice].rndtiemposerviciotipo7 = str(rnd1) + " - " + str(rnd2)
        vectorEstado[indice].tiemposerviciotipo7 = numero1
        vectorEstado[indice].horaserviciotipo7 = vectorEstado[indice].reloj + vectorEstado[indice].tiemposerviciotipo7
        vectorEstado[indice].zona7 = "ocupado"
        vectorEstado[indice].objetocamion.append("EnZona7")
    else:
        vectorEstado[indice].colazona7 += 1
        vectorEstado[indice].objetocamion.append("EnColaZona7")
    return vectorEstado

def llegadaTipo8(vectorEstado, indice, l8, sigma, mu):
    j = 0
    if indice == 1:
        j = 1
    vectorEstado[indice].rndtiempollegadatipo8 = float("{:.2f}".format(random.random()))
    while vectorEstado[indice].rndtiempollegadatipo8 == 1:
        vectorEstado[indice].rndtiempollegadatipo8 = float("{:.2f}".format(random.random()))
    vectorEstado[indice].tiempollegadatipo8 = -(l8) * log(1 - vectorEstado[indice].rndtiempollegadatipo8)
    vectorEstado[indice].horallegadatipo8 = vectorEstado[indice].reloj + vectorEstado[indice].tiempollegadatipo8
    if vectorEstado[indice].zona8 == "libre":
        rnd1 = float("{:.2f}".format(random.random()))
        rnd2 = float("{:.2f}".format(random.random()))
        while rnd1 == 1 or rnd2 == 1 or rnd1 == 0 or rnd2 == 0:
            rnd1 = float("{:.2f}".format(random.random()))
            rnd2 = float("{:.2f}".format(random.random()))
        numero1 = abs(((-2 * log(rnd1)) ** (1 / 2) * cos(2 * pi * rnd2)) * sigma + mu)
        numero2 = ((-2 * log(rnd1)) ** (1 / 2) * sin(2 * pi * rnd2)) * sigma + mu
        vectorEstado[indice].rndtiemposerviciotipo8 = str(rnd1) + " - " + str(rnd2)
        vectorEstado[indice].tiemposerviciotipo8 = numero1
        vectorEstado[indice].horaserviciotipo8 = vectorEstado[indice].reloj + vectorEstado[indice].tiemposerviciotipo8
        vectorEstado[indice].zona8 = "ocupado"
        vectorEstado[indice].objetocamion.append("EnZona8")
    else:
        vectorEstado[indice].colazona8 += 1
        vectorEstado[indice].objetocamion.append("EnColaZona8")
    return vectorEstado

def finServicioTipo1(vectorEstado, indice, sigma, mu):
    j = 0
    if indice == 1:
        j = 1
    vectorEstado[indice].horaserviciotipo1 = 0
    if vectorEstado[j].colazona1 > 0:
        rnd1 = float("{:.2f}".format(random.random()))
        rnd2 = float("{:.2f}".format(random.random()))
        while rnd1 == 1 or rnd2 == 1 or rnd1 == 0 or rnd2 == 0:
            rnd1 = float("{:.2f}".format(random.random()))
            rnd2 = float("{:.2f}".format(random.random()))
        numero1 = abs(((-2 * log(rnd1)) ** (1 / 2) * cos(2 * pi * rnd2)) * sigma + mu)
        numero2 = ((-2 * log(rnd1)) ** (1 / 2) * sin(2 * pi * rnd2)) * sigma + mu
        vectorEstado[indice].rndtiemposerviciotipo1 = str(rnd1) + " - " + str(rnd2)
        vectorEstado[indice].tiemposerviciotipo1 = numero1
        vectorEstado[indice].horaserviciotipo1 = vectorEstado[indice].reloj + vectorEstado[indice].tiemposerviciotipo1
        vectorEstado[indice].colazona1 -= 1

        for i in range(len(vectorEstado[indice].objetocamion)):
            if vectorEstado[indice].objetocamion[i] == "EnColaZona1":
                vectorEstado[indice].objetocamion[i] = "EnZona1"
                break
    else:
        vectorEstado[indice].zona1 = "libre"

    vectorEstado[indice].objetocamion.remove("EnZona1")
    vectorEstado = determinarColaTotal(indice, vectorEstado)
    return vectorEstado

def finServicioTipo2(vectorEstado, indice, sigma, mu):
    j = 0
    if indice == 1:
        j = 1
    vectorEstado[indice].horaserviciotipo2 = 0
    if vectorEstado[j].colazona2 > 0:
        rnd1 = float("{:.2f}".format(random.random()))
        rnd2 = float("{:.2f}".format(random.random()))
        while rnd1 == 1 or rnd2 == 1 or rnd1 == 0 or rnd2 == 0:
            rnd1 = float("{:.2f}".format(random.random()))
            rnd2 = float("{:.2f}".format(random.random()))
        numero1 = abs(((-2 * log(rnd1)) ** (1 / 2) * cos(2 * pi * rnd2)) * sigma + mu)
        numero2 = ((-2 * log(rnd1)) ** (1 / 2) * sin(2 * pi * rnd2)) * sigma + mu
        vectorEstado[indice].rndtiemposerviciotipo2 = str(rnd1) + " - " + str(rnd2)
        vectorEstado[indice].tiemposerviciotipo2 = numero1
        vectorEstado[indice].horaserviciotipo2 = vectorEstado[indice].reloj + vectorEstado[indice].tiemposerviciotipo2
        vectorEstado[indice].colazona2 -= 1

        for i in range(len(vectorEstado[indice].objetocamion)):
            if vectorEstado[indice].objetocamion[i] == "EnColaZona2":
                vectorEstado[indice].objetocamion[i] = "EnZona2"
                break
    else:
        vectorEstado[indice].zona2 = "libre"
        vectorEstado[indice].horaserviciotipo2 = 0

    vectorEstado[indice].objetocamion.remove("EnZona2")
    vectorEstado = determinarColaTotal(indice, vectorEstado)
    return vectorEstado

def finServicioTipo3(vectorEstado, indice, sigma, mu):
    j = 0
    if indice == 1:
        j = 1
    vectorEstado[indice].horaserviciotipo3 = 0
    if vectorEstado[j].colazona3 > 0:
        rnd1 = float("{:.2f}".format(random.random()))
        rnd2 = float("{:.2f}".format(random.random()))
        while rnd1 == 1 or rnd2 == 1 or rnd1 == 0 or rnd2 == 0:
            rnd1 = float("{:.2f}".format(random.random()))
            rnd2 = float("{:.2f}".format(random.random()))
        numero1 = abs(((-2 * log(rnd1)) ** (1 / 2) * cos(2 * pi * rnd2)) * sigma + mu)
        numero2 = ((-2 * log(rnd1)) ** (1 / 2) * sin(2 * pi * rnd2)) * sigma + mu
        vectorEstado[indice].rndtiemposerviciotipo3 = str(rnd1) + " - " + str(rnd2)
        vectorEstado[indice].tiemposerviciotipo3 = numero1
        vectorEstado[indice].horaserviciotipo3 = vectorEstado[indice].reloj + vectorEstado[indice].tiemposerviciotipo3
        vectorEstado[indice].colazona3 -= 1

        for i in range(len(vectorEstado[indice].objetocamion)):
            if vectorEstado[indice].objetocamion[i] == "EnColaZona3":
                vectorEstado[indice].objetocamion[i] = "EnZona3"
                break
    else:
        vectorEstado[indice].zona3 = "libre"
        vectorEstado[indice].horaserviciotipo3 = 0
    vectorEstado[indice].objetocamion.remove("EnZona3")
    vectorEstado = determinarColaTotal(indice, vectorEstado)
    return vectorEstado

def finServicioTipo4(vectorEstado, indice, sigma, mu):
    j = 0
    if indice == 1:
        j = 1
    vectorEstado[indice].horaserviciotipo4 = 0
    if vectorEstado[j].colazona4 > 0:
        rnd1 = float("{:.2f}".format(random.random()))
        rnd2 = float("{:.2f}".format(random.random()))
        while rnd1 == 1 or rnd2 == 1 or rnd1 == 0 or rnd2 == 0:
            rnd1 = float("{:.2f}".format(random.random()))
            rnd2 = float("{:.2f}".format(random.random()))
        numero1 = abs(((-2 * log(rnd1)) ** (1 / 2) * cos(2 * pi * rnd2)) * sigma + mu)
        numero2 = ((-2 * log(rnd1)) ** (1 / 2) * sin(2 * pi * rnd2)) * sigma + mu
        vectorEstado[indice].rndtiemposerviciotipo4 = str(rnd1) + " - " + str(rnd2)
        vectorEstado[indice].tiemposerviciotipo4 = numero1
        vectorEstado[indice].horaserviciotipo4 = vectorEstado[indice].reloj + vectorEstado[indice].tiemposerviciotipo4
        vectorEstado[indice].colazona4 -= 1

        for i in range(len(vectorEstado[indice].objetocamion)):
            if vectorEstado[indice].objetocamion[i] == "EnColaZona4":
                vectorEstado[indice].objetocamion[i] = "EnZona4"
                break
    else:
        vectorEstado[indice].zona4 = "libre"
        vectorEstado[indice].horaserviciotipo4 = 0
    vectorEstado[indice].objetocamion.remove("EnZona4")
    vectorEstado = determinarColaTotal(indice, vectorEstado)
    return vectorEstado

def finServicioTipo5(vectorEstado, indice, sigma, mu):
    j = 0
    if indice == 1:
        j = 1
    vectorEstado[j].horaserviciotipo5 = 0
    if vectorEstado[indice].colazona5 > 0:
        rnd1 = float("{:.2f}".format(random.random()))
        rnd2 = float("{:.2f}".format(random.random()))
        while rnd1 == 1 or rnd2 == 1 or rnd1 == 0 or rnd2 == 0:
            rnd1 = float("{:.2f}".format(random.random()))
            rnd2 = float("{:.2f}".format(random.random()))
        numero1 = abs(((-2 * log(rnd1)) ** (1 / 2) * cos(2 * pi * rnd2)) * sigma + mu)
        numero2 = ((-2 * log(rnd1)) ** (1 / 2) * sin(2 * pi * rnd2)) * sigma + mu
        vectorEstado[indice].rndtiemposerviciotipo5 = str(rnd1) + " - " + str(rnd2)
        vectorEstado[indice].tiemposerviciotipo5 = numero1
        vectorEstado[indice].horaserviciotipo5 = vectorEstado[indice].reloj + vectorEstado[indice].tiemposerviciotipo5
        vectorEstado[indice].colazona5 -= 1

        for i in range(len(vectorEstado[indice].objetocamion)):
            if vectorEstado[indice].objetocamion[i] == "EnColaZona5":
                vectorEstado[indice].objetocamion[i] = "EnZona5"
                break
    else:
        vectorEstado[indice].zona5 = "libre"
        vectorEstado[indice].horaserviciotipo5 = 0
    vectorEstado[indice].objetocamion.remove("EnZona5")
    vectorEstado = determinarColaTotal(indice, vectorEstado)
    return vectorEstado

def finServicioTipo6(vectorEstado, indice, sigma, mu):
    j = 0
    if indice == 1:
        j = 1
    vectorEstado[indice].horaserviciotipo6 = 0
    if vectorEstado[j].colazona6 > 0:
        rnd1 = float("{:.2f}".format(random.random()))
        rnd2 = float("{:.2f}".format(random.random()))
        while rnd1 == 1 or rnd2 == 1 or rnd1 == 0 or rnd2 == 0:
            rnd1 = float("{:.2f}".format(random.random()))
            rnd2 = float("{:.2f}".format(random.random()))
        numero1 = abs(((-2 * log(rnd1)) ** (1 / 2) * cos(2 * pi * rnd2)) * sigma + mu)
        numero2 = ((-2 * log(rnd1)) ** (1 / 2) * sin(2 * pi * rnd2)) * sigma + mu
        vectorEstado[indice].rndtiemposerviciotipo6 = str(rnd1) + " - " + str(rnd2)
        vectorEstado[indice].tiemposerviciotipo6 = numero1
        vectorEstado[indice].horaserviciotipo6 = vectorEstado[indice].reloj + vectorEstado[indice].tiemposerviciotipo6
        vectorEstado[indice].colazona6 -= 1

        for i in range(len(vectorEstado[indice].objetocamion)):
            if vectorEstado[indice].objetocamion[i] == "EnColaZona6":
                vectorEstado[indice].objetocamion[i] = "EnZona6"
                break
    else:
        vectorEstado[indice].zona6 = "libre"
        vectorEstado[indice].horaserviciotipo6 = 0
    vectorEstado[indice].objetocamion.remove("EnZona6")
    return vectorEstado

def finServicioTipo7(vectorEstado, indice, sigma, mu):
    j = 0
    if indice == 1:
        j = 1
    vectorEstado[indice].horaserviciotipo7 = 0
    if vectorEstado[indice].colazona7 > 0:
        rnd1 = float("{:.2f}".format(random.random()))
        rnd2 = float("{:.2f}".format(random.random()))
        while rnd1 == 1 or rnd2 == 1 or rnd1 == 0 or rnd2 == 0:
            rnd1 = float("{:.2f}".format(random.random()))
            rnd2 = float("{:.2f}".format(random.random()))
        numero1 = abs(((-2 * log(rnd1)) ** (1 / 2) * cos(2 * pi * rnd2)) * sigma + mu)
        numero2 = ((-2 * log(rnd1)) ** (1 / 2) * sin(2 * pi * rnd2)) * sigma + mu
        vectorEstado[indice].rndtiemposerviciotipo7 = str(rnd1) + " - " + str(rnd2)
        vectorEstado[indice].tiemposerviciotipo7 = numero1
        vectorEstado[indice].horaserviciotipo7 = vectorEstado[indice].reloj + vectorEstado[indice].tiemposerviciotipo7
        vectorEstado[indice].colazona7 -= 1


        for i in range(len(vectorEstado[indice].objetocamion)):
            if vectorEstado[indice].objetocamion[i] == "EnColaZona7":
                vectorEstado[indice].objetocamion[i] = "EnZona7"
                break
    else:
        vectorEstado[indice].zona7 = "libre"
        vectorEstado[indice].horaserviciotipo7 = 0
    vectorEstado[indice].objetocamion.remove("EnZona7")
    vectorEstado = determinarColaTotal(indice, vectorEstado)
    return vectorEstado

def finServicioTipo8(vectorEstado, indice, sigma, mu):
    j = 0
    if indice == 1:
        j = 1
    vectorEstado[indice].horaserviciotipo8 = 0
    j = 0
    if indice == 1:
        j = 1
    if vectorEstado[j].colazona8 > 0:
        rnd1 = float("{:.2f}".format(random.random()))
        rnd2 = float("{:.2f}".format(random.random()))
        while rnd1 == 1 or rnd2 == 1 or rnd1 == 0 or rnd2 == 0:
            rnd1 = float("{:.2f}".format(random.random()))
            rnd2 = float("{:.2f}".format(random.random()))
        numero1 = abs(((-2 * log(rnd1)) ** (1 / 2) * cos(2 * pi * rnd2)) * sigma + mu)
        numero2 = ((-2 * log(rnd1)) ** (1 / 2) * sin(2 * pi * rnd2)) * sigma + mu
        vectorEstado[indice].rndtiemposerviciotipo8 = str(rnd1) + " - " + str(rnd2)
        vectorEstado[indice].tiemposerviciotipo8 = numero1
        vectorEstado[indice].horaserviciotipo8 = vectorEstado[indice].reloj + vectorEstado[indice].tiemposerviciotipo8
        vectorEstado[indice].colazona8 -= 1

        for i in range(len(vectorEstado[indice].objetocamion)):
            if vectorEstado[indice].objetocamion[i] == "EnColaZona8":
                vectorEstado[indice].objetocamion[i] = "EnZona8"
                break
    else:
        vectorEstado[indice].zona8 = "libre"
        vectorEstado[indice].horaserviciotipo8 = 0
    vectorEstado[indice].objetocamion.remove("EnZona8")
    vectorEstado = determinarColaTotal(indice, vectorEstado)
    return vectorEstado

def determinarSemanas(vectorEstado, indice):
    vectorEstado[indice].cantidadsemanas = (vectorEstado[indice].reloj // (7*24)) + 1
    return vectorEstado


def haySobrecarga(vectorEstado, indice, capacidad):
    colaTotal = vectorEstado[indice].colazona1 + vectorEstado[indice].colazona2 + vectorEstado[indice].colazona3 + \
                vectorEstado[indice].colazona4 + vectorEstado[indice].colazona5 + vectorEstado[indice].colazona6 + \
                vectorEstado[indice].colazona7 + vectorEstado[indice].colazona8

    if colaTotal > capacidad:
        vectorEstado[indice].cantidadsobrecargas += 1
    vectorEstado[indice].porcentajesobrecargas = vectorEstado[indice].cantidadsobrecargas / vectorEstado[indice].reloj
    vectorEstado[indice].colaTotal = colaTotal
    return vectorEstado

def determinarColaTotal(j, vectorEstado):
    colaTotal = vectorEstado[j].colazona1 + vectorEstado[j].colazona2 + vectorEstado[j].colazona3 + \
                vectorEstado[j].colazona4 + vectorEstado[j].colazona5 + vectorEstado[j].colazona6 + \
                vectorEstado[j].colazona7 + vectorEstado[j].colazona8
    vectorEstado[j].colaTotal = colaTotal
    return vectorEstado

def funcionPrincipal(n, v, l1, l2, l3, l4, l5, l6, l7, l8, ms1, ds1, ms2, ds2, ms3, ds3, ms4, ds4, ms5, ds5, ms6, ds6,
                     ms7, ds7, ms8, ds8, r, capacidad, mismo):
    vectorEstado = [
        vectDatos(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, []),
        vectDatos(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, [])
    ]
    j = 0
    nroEvento = []
    eventos = []
    relojes = []

    rnd_llegadas_tipo1 = []
    tiempos_llegadas_tipo1 = []
    horas_llegadas_tipo1 = []

    rnd_llegadas_tipo2 = []
    tiempos_llegadas_tipo2 = []
    horas_llegadas_tipo2 = []

    rnd_llegadas_tipo3 = []
    tiempos_llegadas_tipo3 = []
    horas_llegadas_tipo3 = []

    rnd_llegadas_tipo4 = []
    tiempos_llegadas_tipo4 = []
    horas_llegadas_tipo4 = []

    rnd_llegadas_tipo5 = []
    tiempos_llegadas_tipo5 = []
    horas_llegadas_tipo5 = []

    rnd_llegadas_tipo6 = []
    tiempos_llegadas_tipo6 = []
    horas_llegadas_tipo6 = []

    rnd_llegadas_tipo7 = []
    tiempos_llegadas_tipo7 = []
    horas_llegadas_tipo7 = []

    rnd_llegadas_tipo8 = []
    tiempos_llegadas_tipo8 = []
    horas_llegadas_tipo8 = []

    rnd_tiempo_servicio_tipo1 = []
    tiempos_servicio_tipo1 = []
    horas_servicio_tipo1 = []

    rnd_tiempo_servicio_tipo2 = []
    tiempos_servicio_tipo2 = []
    horas_servicio_tipo2 = []

    rnd_tiempo_servicio_tipo3 = []
    tiempos_servicio_tipo3 = []
    horas_servicio_tipo3 = []

    rnd_tiempo_servicio_tipo4 = []
    tiempos_servicio_tipo4 = []
    horas_servicio_tipo4 = []

    rnd_tiempo_servicio_tipo5 = []
    tiempos_servicio_tipo5 = []
    horas_servicio_tipo5 = []

    rnd_tiempo_servicio_tipo6 = []
    tiempos_servicio_tipo6 = []
    horas_servicio_tipo6 = []

    rnd_tiempo_servicio_tipo7 = []
    tiempos_servicio_tipo7 = []
    horas_servicio_tipo7 = []

    rnd_tiempo_servicio_tipo8 = []
    tiempos_servicio_tipo8 = []
    horas_servicio_tipo8 = []

    zona1, zona2, zona3, zona4, zona5, zona6, zona7, zona8 = [], [], [], [], [], [], [], []
    colazona1, colazona2, colazona3, colazona4, colazona5, colazona6, colazona7, colazona8 = [], [], [], [], [], [], [], []
    colaTotal = []

    cantidad_semanas = []

    cantidad_sobrecargas = []

    porcentaje_sobrecargas = []

    objetos_camion = []

    for i in range(n):
        if i == 0:
            vectorEstado[0].evento = "Inicio"
            vectorEstado[0].reloj = 0
            vectorEstado[0].rndtiempollegadatipo1 = float("{:.2f}".format(random.random()))
            while vectorEstado[0].rndtiempollegadatipo1 == 1:
                vectorEstado[0].rndtiempollegadatipo1 = float("{:.2f}".format(random.random()))
            vectorEstado[0].tiempollegadatipo1 = -(l1)*log(1-vectorEstado[0].rndtiempollegadatipo1)
            vectorEstado[0].horallegadatipo1 = vectorEstado[0].reloj + vectorEstado[0].tiempollegadatipo1
            vectorEstado[0].rndtiempollegadatipo2 = float("{:.2f}".format(random.random()))
            while vectorEstado[0].rndtiempollegadatipo2 == 1:
                vectorEstado[0].rndtiempollegadatipo2 = float("{:.2f}".format(random.random()))
            vectorEstado[0].tiempollegadatipo2 = -(l2)*log(1-vectorEstado[0].rndtiempollegadatipo2)
            vectorEstado[0].horallegadatipo2 = vectorEstado[0].reloj + vectorEstado[0].tiempollegadatipo2
            vectorEstado[0].rndtiempollegadatipo3 = float("{:.2f}".format(random.random()))
            while  vectorEstado[0].rndtiempollegadatipo3 == 1:
                vectorEstado[0].rndtiempollegadatipo3 = float("{:.2f}".format(random.random()))
            vectorEstado[0].tiempollegadatipo3 = -(l3)*log(1-vectorEstado[0].rndtiempollegadatipo3)
            vectorEstado[0].horallegadatipo3 = vectorEstado[0].reloj + vectorEstado[0].tiempollegadatipo3
            vectorEstado[0].rndtiempollegadatipo4 = float("{:.2f}".format(random.random()))
            while vectorEstado[0].rndtiempollegadatipo4 == 1:
                vectorEstado[0].rndtiempollegadatipo4 = float("{:.2f}".format(random.random()))
            vectorEstado[0].tiempollegadatipo4 = -(l4)*log(1-vectorEstado[0].rndtiempollegadatipo4)
            vectorEstado[0].horallegadatipo4 = vectorEstado[0].reloj + vectorEstado[0].tiempollegadatipo4
            vectorEstado[0].rndtiempollegadatipo5 = float("{:.2f}".format(random.random()))
            while vectorEstado[0].rndtiempollegadatipo5 == 1:
                vectorEstado[0].rndtiempollegadatipo5 = float("{:.2f}".format(random.random()))
            vectorEstado[0].tiempollegadatipo5 = -(l5)*log(1-vectorEstado[0].rndtiempollegadatipo5)
            vectorEstado[0].horallegadatipo5 = vectorEstado[0].reloj + vectorEstado[0].tiempollegadatipo5
            vectorEstado[0].rndtiempollegadatipo6 = float("{:.2f}".format(random.random()))
            while vectorEstado[0].rndtiempollegadatipo6 == 1:
                vectorEstado[0].rndtiempollegadatipo6 = float("{:.2f}".format(random.random()))
            vectorEstado[0].tiempollegadatipo6 = -(l6)*log(1-vectorEstado[0].rndtiempollegadatipo6)
            vectorEstado[0].horallegadatipo6 = vectorEstado[0].reloj + vectorEstado[0].tiempollegadatipo6
            vectorEstado[0].rndtiempollegadatipo7 = float("{:.2f}".format(random.random()))
            while vectorEstado[0].rndtiempollegadatipo7 == 1:
                vectorEstado[0].rndtiempollegadatipo7 = float("{:.2f}".format(random.random()))
            vectorEstado[0].tiempollegadatipo7 = -(l7)*log(1-vectorEstado[0].rndtiempollegadatipo7)
            vectorEstado[0].horallegadatipo7 = vectorEstado[0].reloj + vectorEstado[0].tiempollegadatipo7
            vectorEstado[0].rndtiempollegadatipo8 = float("{:.2f}".format(random.random()))
            while vectorEstado[0].rndtiempollegadatipo8 == 1:
                vectorEstado[0].rndtiempollegadatipo8 = float("{:.2f}".format(random.random()))
            vectorEstado[0].tiempollegadatipo8 = -(l8)*log(1-vectorEstado[0].rndtiempollegadatipo8)
            vectorEstado[0].horallegadatipo8 = vectorEstado[0].reloj + vectorEstado[0].tiempollegadatipo8
            vectorEstado[0].zona1 = "libre"
            vectorEstado[0].zona2 = "libre"
            vectorEstado[0].zona3 = "libre"
            vectorEstado[0].zona4 = "libre"
            vectorEstado[0].zona5 = "libre"
            vectorEstado[0].zona6 = "libre"
            vectorEstado[0].zona7 = "libre"
            vectorEstado[0].zona8 = "libre"
            vectorEstado[0].objetocamion = []
        elif (i % 2 != 0):
            j = 1
            vectorEstado[1] = deepcopy(vectorEstado[0])
            menor, indice = determinarMenorTiempo(vectorEstado, 1)
            vectorEstado[1].reloj = menor
            vectorEstado[1].evento = determinarEvento(vectorEstado[0], vectorEstado[1].reloj)
            vectorEstado = determinarSemanas(vectorEstado, 1)
            if indice == 0:
                vectorEstado = llegadaTipo1(vectorEstado, 1, l1, ds1, ms1)
                vectorEstado = haySobrecarga(vectorEstado, 1, capacidad)
            elif indice == 1:
                vectorEstado = llegadaTipo2(vectorEstado, 1, l2, ds2, ms2)
                vectorEstado = haySobrecarga(vectorEstado, 1, capacidad)
            elif indice == 2:
                vectorEstado = llegadaTipo3(vectorEstado, 1, l3, ds3, ms3)
                vectorEstado = haySobrecarga(vectorEstado, 1, capacidad)
            elif indice == 3:
                vectorEstado = llegadaTipo4(vectorEstado, 1, l4, ds4, ms4)
                vectorEstado = haySobrecarga(vectorEstado, 1, capacidad)
            elif indice == 4:
                vectorEstado = llegadaTipo5(vectorEstado, 1, l5, ds5, ms5)
                vectorEstado = haySobrecarga(vectorEstado, 1, capacidad)
            elif indice == 5:
                vectorEstado = llegadaTipo6(vectorEstado, 1, l6, ds6, ms6)
                vectorEstado = haySobrecarga(vectorEstado, 1, capacidad)
            elif indice == 6:
                vectorEstado = llegadaTipo7(vectorEstado, 1, l7, ds7, ms7)
                vectorEstado = haySobrecarga(vectorEstado, 1, capacidad)
            elif indice == 7:
                vectorEstado = llegadaTipo8(vectorEstado, 1, l8, ds8, ms8)
                vectorEstado = haySobrecarga(vectorEstado, 1, capacidad)
            elif indice == 8:
                vectorEstado = finServicioTipo1(vectorEstado, 1, ds1, ms1)
            elif indice == 9:
                vectorEstado = finServicioTipo2(vectorEstado, 1, ds2, ms2)
            elif indice == 10:
                vectorEstado = finServicioTipo3(vectorEstado, 1, ds3, ms3)
            elif indice == 11:
                vectorEstado = finServicioTipo4(vectorEstado, 1, ds4, ms4)
            elif indice == 12:
                vectorEstado = finServicioTipo5(vectorEstado, 1, ds5, ms5)
            elif indice == 13:
                vectorEstado = finServicioTipo6(vectorEstado, 1, ds6, ms6)
            elif indice == 14:
                vectorEstado = finServicioTipo7(vectorEstado, 1, ds7, ms7)
            elif indice == 15:
                vectorEstado = finServicioTipo8(vectorEstado, 1, ds8, ms8)
            if vectorEstado[1].cantidadsemanas != vectorEstado[0].cantidadsemanas:
                   l1, l2, l3, l4, l5, l6, l7, l8 = l1 + l1 * r/100, l2 + l2 * r/100,l3 + l3 * r/100, l4 + l4 * r/100, \
                   l5 + l5 * r/100, l6 + l6 * r/100, \
                   l7 + l7 * r/100, l8 + l8 * r/100
        elif (i % 2 == 0):
            j = 0
            vectorEstado[0] = deepcopy(vectorEstado[1])
            menor, indice = determinarMenorTiempo(vectorEstado, 0)
            vectorEstado[0].reloj = menor
            vectorEstado[0].evento = determinarEvento(vectorEstado[1], vectorEstado[0].reloj)
            vectorEstado = determinarSemanas(vectorEstado, 0)
            if indice == 0:
                vectorEstado = llegadaTipo1(vectorEstado, 0, l1, ds1, ms1)
                vectorEstado = haySobrecarga(vectorEstado, 0, capacidad)
            elif indice == 1:
                vectorEstado = llegadaTipo2(vectorEstado, 0, l2, ds2, ms2)
                vectorEstado = haySobrecarga(vectorEstado, 0, capacidad)
            elif indice == 2:
                vectorEstado = llegadaTipo3(vectorEstado, 0, l3, ds3, ms3)
                vectorEstado = haySobrecarga(vectorEstado, 0, capacidad)
            elif indice == 3:
                vectorEstado = llegadaTipo4(vectorEstado, 0, l4, ds4, ms4)
                vectorEstado = haySobrecarga(vectorEstado, 0, capacidad)
            elif indice == 4:
                vectorEstado = llegadaTipo5(vectorEstado, 0, l5, ds5, ms5)
                vectorEstado = haySobrecarga(vectorEstado, 0, capacidad)
            elif indice == 5:
                vectorEstado = llegadaTipo6(vectorEstado, 0, l6, ds6, ms6)
                vectorEstado = haySobrecarga(vectorEstado, 0, capacidad)
            elif indice == 6:
                vectorEstado = llegadaTipo7(vectorEstado, 0, l7, ds7, ms7)
                vectorEstado = haySobrecarga(vectorEstado, 0, capacidad)
            elif indice == 7:
                vectorEstado = llegadaTipo8(vectorEstado, 0, l8, ds8, ms8)
                vectorEstado = haySobrecarga(vectorEstado, 0, capacidad)
            elif indice == 8:
                vectorEstado = finServicioTipo1(vectorEstado, 0, ds1, ms1)
            elif indice == 9:
                vectorEstado = finServicioTipo2(vectorEstado, 0, ds2, ms2)
            elif indice == 10:
                vectorEstado = finServicioTipo3(vectorEstado, 0, ds3, ms3)
            elif indice == 11:
                vectorEstado = finServicioTipo4(vectorEstado, 0, ds4, ms4)
            elif indice == 12:
                vectorEstado = finServicioTipo5(vectorEstado, 0, ds5, ms5)
            elif indice == 13:
                vectorEstado = finServicioTipo6(vectorEstado, 0, ds6, ms6)
            elif indice == 14:
                vectorEstado = finServicioTipo7(vectorEstado, 0, ds7, ms7)
            elif indice == 15:
                vectorEstado = finServicioTipo8(vectorEstado, 0, ds8, ms8)
            if vectorEstado[0].cantidadsemanas != vectorEstado[1].cantidadsemanas:
                   l1, l2, l3, l4, l5, l6, l7, l8 = l1 + l1 * r/100, l2 + l2 * r/100, l3 + l3 * r/100, l4 + l4 * r/100, \
                   l5 + l5 * r/100, l6 + l6 * r/100, \
                   l7 + l7 * r/100, l8 + l8 * r/100

        if (i >= v - 1 and i <= v - 1 + 500) or (i == n - 1):
            nroEvento.append(i+1)
            eventos.append(vectorEstado[j].evento)
            relojes.append(vectorEstado[j].reloj)
            rnd_llegadas_tipo1.append(vectorEstado[j].rndtiempollegadatipo1)
            tiempos_llegadas_tipo1.append(vectorEstado[j].tiempollegadatipo1)
            horas_llegadas_tipo1.append(vectorEstado[j].horallegadatipo1)
            rnd_llegadas_tipo2.append(vectorEstado[j].rndtiempollegadatipo2)
            tiempos_llegadas_tipo2.append(vectorEstado[j].tiempollegadatipo2)
            horas_llegadas_tipo2.append(vectorEstado[j].horallegadatipo2)
            rnd_llegadas_tipo3.append(vectorEstado[j].rndtiempollegadatipo3)
            tiempos_llegadas_tipo3.append(vectorEstado[j].tiempollegadatipo3)
            horas_llegadas_tipo3.append(vectorEstado[j].horallegadatipo3)
            rnd_llegadas_tipo4.append(vectorEstado[j].rndtiempollegadatipo4)
            tiempos_llegadas_tipo4.append(vectorEstado[j].tiempollegadatipo4)
            horas_llegadas_tipo4.append(vectorEstado[j].horallegadatipo4)
            rnd_llegadas_tipo5.append(vectorEstado[j].rndtiempollegadatipo5)
            tiempos_llegadas_tipo5.append(vectorEstado[j].tiempollegadatipo5)
            horas_llegadas_tipo5.append(vectorEstado[j].horallegadatipo5)
            rnd_llegadas_tipo6.append(vectorEstado[j].rndtiempollegadatipo6)
            tiempos_llegadas_tipo6.append(vectorEstado[j].tiempollegadatipo6)
            horas_llegadas_tipo6.append(vectorEstado[j].horallegadatipo6)
            rnd_llegadas_tipo7.append(vectorEstado[j].rndtiempollegadatipo7)
            tiempos_llegadas_tipo7.append(vectorEstado[j].tiempollegadatipo7)
            horas_llegadas_tipo7.append(vectorEstado[j].horallegadatipo7)
            rnd_llegadas_tipo8.append(vectorEstado[j].rndtiempollegadatipo8)
            tiempos_llegadas_tipo8.append(vectorEstado[j].tiempollegadatipo8)
            horas_llegadas_tipo8.append(vectorEstado[j].horallegadatipo8)
            rnd_tiempo_servicio_tipo1.append(vectorEstado[j].rndtiemposerviciotipo1)
            tiempos_servicio_tipo1.append(vectorEstado[j].tiemposerviciotipo1)
            horas_servicio_tipo1.append(vectorEstado[j].horaserviciotipo1)
            rnd_tiempo_servicio_tipo2.append(vectorEstado[j].rndtiemposerviciotipo2)
            tiempos_servicio_tipo2.append(vectorEstado[j].tiemposerviciotipo2)
            horas_servicio_tipo2.append(vectorEstado[j].horaserviciotipo2)
            rnd_tiempo_servicio_tipo3.append(vectorEstado[j].rndtiemposerviciotipo3)
            tiempos_servicio_tipo3.append(vectorEstado[j].tiemposerviciotipo3)
            horas_servicio_tipo3.append(vectorEstado[j].horaserviciotipo3)
            rnd_tiempo_servicio_tipo4.append(vectorEstado[j].rndtiemposerviciotipo4)
            tiempos_servicio_tipo4.append(vectorEstado[j].tiemposerviciotipo4)
            horas_servicio_tipo4.append(vectorEstado[j].horaserviciotipo4)
            rnd_tiempo_servicio_tipo5.append(vectorEstado[j].rndtiemposerviciotipo5)
            tiempos_servicio_tipo5.append(vectorEstado[j].tiemposerviciotipo5)
            horas_servicio_tipo5.append(vectorEstado[j].horaserviciotipo5)
            rnd_tiempo_servicio_tipo6.append(vectorEstado[j].rndtiemposerviciotipo6)
            tiempos_servicio_tipo6.append(vectorEstado[j].tiemposerviciotipo6)
            horas_servicio_tipo6.append(vectorEstado[j].horaserviciotipo6)
            rnd_tiempo_servicio_tipo7.append(vectorEstado[j].rndtiemposerviciotipo7)
            tiempos_servicio_tipo7.append(vectorEstado[j].tiemposerviciotipo7)
            horas_servicio_tipo7.append(vectorEstado[j].horaserviciotipo7)
            rnd_tiempo_servicio_tipo8.append(vectorEstado[j].rndtiemposerviciotipo8)
            tiempos_servicio_tipo8.append(vectorEstado[j].tiemposerviciotipo8)
            horas_servicio_tipo8.append(vectorEstado[j].horaserviciotipo8)
            zona1.append(vectorEstado[j].zona1)
            zona2.append(vectorEstado[j].zona2)
            zona3.append(vectorEstado[j].zona3)
            zona4.append(vectorEstado[j].zona4)
            zona5.append(vectorEstado[j].zona5)
            zona6.append(vectorEstado[j].zona6)
            zona7.append(vectorEstado[j].zona7)
            zona8.append(vectorEstado[j].zona8)
            colazona1.append(vectorEstado[j].colazona1)
            colazona2.append(vectorEstado[j].colazona2)
            colazona3.append(vectorEstado[j].colazona3)
            colazona4.append(vectorEstado[j].colazona4)
            colazona5.append(vectorEstado[j].colazona5)
            colazona6.append(vectorEstado[j].colazona6)
            colazona7.append(vectorEstado[j].colazona7)
            colazona8.append(vectorEstado[j].colazona8)
            colaTotal.append(vectorEstado[j].colaTotal)
            cantidad_semanas.append(vectorEstado[j].cantidadsemanas)
            cantidad_sobrecargas.append(vectorEstado[j].cantidadsobrecargas)
            porcentaje_sobrecargas.append(vectorEstado[j].porcentajesobrecargas)
            objetos = ""
            for m in range(len(vectorEstado[j].objetocamion)):
                objetos = objetos + f"EstadoCamion{m+1}: " + str(vectorEstado[j].objetocamion[m]) + ", "
            objetos_camion.append(objetos)
        mismo.progress.set(i + 1)
        mismo.master.update_idletasks()
    data = {
        'nroEvento': nroEvento,
        'evento': eventos,
        'reloj': relojes,
        'rnd_llegadas_tipo1': rnd_llegadas_tipo1,
        'tiempos_llegadas_tipo1': tiempos_llegadas_tipo1,
        'horas_llegadas_tipo1': horas_llegadas_tipo1,
        'rnd_llegadas_tipo2': rnd_llegadas_tipo2,
        'tiempos_llegadas_tipo2': tiempos_llegadas_tipo2,
        'horas_llegadas_tipo2': horas_llegadas_tipo2,
        'rnd_llegadas_tipo3': rnd_llegadas_tipo3,
        'tiempos_llegadas_tipo3': tiempos_llegadas_tipo3,
        'horas_llegadas_tipo3': horas_llegadas_tipo3,
        'rnd_llegadas_tipo4': rnd_llegadas_tipo4,
        'tiempos_llegadas_tipo4': tiempos_llegadas_tipo4,
        'horas_llegadas_tipo4': horas_llegadas_tipo4,
        'rnd_llegadas_tipo5': rnd_llegadas_tipo5,
        'tiempos_llegadas_tipo5': tiempos_llegadas_tipo5,
        'horas_llegadas_tipo5': horas_llegadas_tipo5,
        'rnd_llegadas_tipo6': rnd_llegadas_tipo6,
        'tiempos_llegadas_tipo6': tiempos_llegadas_tipo6,
        'horas_llegadas_tipo6': horas_llegadas_tipo6,
        'rnd_llegadas_tipo7': rnd_llegadas_tipo7,
        'tiempos_llegadas_tipo7': tiempos_llegadas_tipo7,
        'horas_llegadas_tipo7': horas_llegadas_tipo7,
        'rnd_llegadas_tipo8': rnd_llegadas_tipo8,
        'tiempos_llegadas_tipo8': tiempos_llegadas_tipo8,
        'horas_llegadas_tipo8': horas_llegadas_tipo8,
        'rnd_tiempo_servicio_tipo1': rnd_tiempo_servicio_tipo1,
        'tiempos_servicio_tipo1': tiempos_servicio_tipo1,
        'horas_servicio_tipo1': horas_servicio_tipo1,
        'rnd_tiempo_servicio_tipo2': rnd_tiempo_servicio_tipo2,
        'tiempos_servicio_tipo2': tiempos_servicio_tipo2,
        'horas_servicio_tipo2': horas_servicio_tipo2,
        'rnd_tiempo_servicio_tipo3': rnd_tiempo_servicio_tipo3,
        'tiempos_servicio_tipo3': tiempos_servicio_tipo3,
        'horas_servicio_tipo3': horas_servicio_tipo3,
        'rnd_tiempo_servicio_tipo4': rnd_tiempo_servicio_tipo4,
        'tiempos_servicio_tipo4': tiempos_servicio_tipo4,
        'horas_servicio_tipo4': horas_servicio_tipo4,
        'rnd_tiempo_servicio_tipo5': rnd_tiempo_servicio_tipo5,
        'tiempos_servicio_tipo5': tiempos_servicio_tipo5,
        'horas_servicio_tipo5': horas_servicio_tipo5,
        'rnd_tiempo_servicio_tipo6': rnd_tiempo_servicio_tipo6,
        'tiempos_servicio_tipo6': tiempos_servicio_tipo6,
        'horas_servicio_tipo6': horas_servicio_tipo6,
        'rnd_tiempo_servicio_tipo7': rnd_tiempo_servicio_tipo7,
        'tiempos_servicio_tipo7': tiempos_servicio_tipo7,
        'horas_servicio_tipo7': horas_servicio_tipo7,
        'rnd_tiempo_servicio_tipo8': rnd_tiempo_servicio_tipo8,
        'tiempos_servicio_tipo8': tiempos_servicio_tipo8,
        'horas_servicio_tipo8': horas_servicio_tipo8,
        'zona1': zona1,
        'zona2': zona2,
        'zona3': zona3,
        'zona4': zona4,
        'zona5': zona5,
        'zona6': zona6,
        'zona7': zona7,
        'zona8': zona8,
        'cola_zona1': colazona1,
        'cola_zona2': colazona2,
        'cola_zona3': colazona3,
        'cola_zona4': colazona4,
        'cola_zona5': colazona5,
        'cola_zona6': colazona6,
        'cola_zona7': colazona7,
        'cola_zona8': colazona8,
        'cola_total': colaTotal,
        'cantidad_semanas': cantidad_semanas,
        'cantidad_sobrecargas': cantidad_sobrecargas,
        'porcentaje_sobrecargas': porcentaje_sobrecargas,
        'camiones': objetos_camion
    }

    df = pd.DataFrame(data)
    workbook = Workbook()
    hoja_activa = workbook.active
    # Agregar los nombres de las columnas como encabezado
    encabezado = list(df.columns)
    hoja_activa.append(encabezado)
    # Agregar los datos del DataFrame a la hoja de Excel
    for fila in dataframe_to_rows(df, index=False, header=False):
        hoja_activa.append(fila)
    # Congelar los paneles con los encabezados de las columnas
    hoja_activa.freeze_panes = "A2"

    # Ajustar automáticamente el ancho de las columnas
    for columna in hoja_activa.columns:
        max_length = 0
        for celda in columna:
            if celda.value:
                max_length = max(max_length, len(str(celda.value)))
        adjusted_width = (max_length + 2) * 1.2
        hoja_activa.column_dimensions[columna[0].column_letter].width = adjusted_width

    # Guardar los cambios en el archivo de Excel
    excel_file = 'final.xlsx'
    workbook.save(excel_file)
    return vectorEstado[j]

class colasApp:
    def __init__(self, master):
        self.master = master
        master.title("Simulador")
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("green")
        self.progress = tk.DoubleVar()
        self.progress.set(0.0)
        # Creamos el contenedor para la cantidad de simulaciones
        self.cantidad_frame = customtkinter.CTkFrame(master=master)
        self.cantidad_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
        self.cantidad_lbl = customtkinter.CTkLabel(master=self.cantidad_frame, text="Cantidad de ""\nsimulaciones")
        self.cantidad_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.cantidad_numeros_var = customtkinter.StringVar()
        self.cantidad_numeros_var.set("10000")
        self.cantidad_numeros_entry = customtkinter.CTkEntry(self.cantidad_frame, textvariable=self.cantidad_numeros_var)
        self.cantidad_numeros_entry.grid(row=1, column=0, padx=5, pady=5)

        #Creamos el contenedor para indicar desde donde queremos que sea vea la simulacio, ademas de la ultima linea
        self.ver_desde_frame = customtkinter.CTkFrame(master=master)
        self.ver_desde_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nw")
        self.ver_desde_lbl = customtkinter.CTkLabel(master=self.ver_desde_frame, text="Ver desde")
        self.ver_desde_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.ver_desde_var = customtkinter.StringVar()
        self.ver_desde_var.set("9000")
        self.ver_desde_entry = customtkinter.CTkEntry(self.ver_desde_frame, textvariable=self.ver_desde_var)
        self.ver_desde_entry.grid(row=1, column=0, padx=5, pady=5)

        #Creamos el contenedor para indicar el tiempo entre llegadas de tipo 1
        self.llegadatipo1_frame = customtkinter.CTkFrame(master=master)
        self.llegadatipo1_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nw")
        self.llegadatipo1_lbl = customtkinter.CTkLabel(master=self.llegadatipo1_frame, text="llegadaTipo1")
        self.llegadatipo1_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.llegadatipo1_var = customtkinter.StringVar()
        self.llegadatipo1_var.set("0.43")
        self.llegadatipo1_entry = customtkinter.CTkEntry(self.llegadatipo1_frame, textvariable=self.llegadatipo1_var)
        self.llegadatipo1_entry.grid(row=1, column=0, padx=5, pady=5)

        #Creamos el contenedor para indicar el tiempo entre llegagas tipo 2
        self.llegadatipo2_frame = customtkinter.CTkFrame(master=master)
        self.llegadatipo2_frame.grid(row=0, column=3, padx=10, pady=10, sticky="nw")
        self.llegadatipo2_lbl = customtkinter.CTkLabel(master=self.llegadatipo2_frame, text="llegadaTipo2")
        self.llegadatipo2_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.llegadatipo2_var = customtkinter.StringVar()
        self.llegadatipo2_var.set("0.16")
        self.llegadatipo2_entry = customtkinter.CTkEntry(self.llegadatipo2_frame, textvariable=self.llegadatipo2_var)
        self.llegadatipo2_entry.grid(row=1, column=0, padx=5, pady=5)

        # Creamos el contenedor para indicar el tiempo entre llegadas de tipo 3
        self.llegadatipo3_frame = customtkinter.CTkFrame(master=master)
        self.llegadatipo3_frame.grid(row=0, column=4, padx=10, pady=10, sticky="nw")
        self.llegadatipo3_lbl = customtkinter.CTkLabel(master=self.llegadatipo3_frame, text="llegadaTipo3")
        self.llegadatipo3_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.llegadatipo3_var = customtkinter.StringVar()
        self.llegadatipo3_var.set("0.14")
        self.llegadatipo3_entry = customtkinter.CTkEntry(self.llegadatipo3_frame, textvariable=self.llegadatipo3_var)
        self.llegadatipo3_entry.grid(row=1, column=0, padx=5, pady=5)

        # Creamos el contenedor para indicar el tiempo entre llegadas de tipo 4
        self.llegadatipo4_frame = customtkinter.CTkFrame(master=master)
        self.llegadatipo4_frame.grid(row=0, column=5, padx=10, pady=10, sticky="nw")
        self.llegadatipo4_lbl = customtkinter.CTkLabel(master=self.llegadatipo4_frame, text="llegadaTipo4")
        self.llegadatipo4_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.llegadatipo4_var = customtkinter.StringVar()
        self.llegadatipo4_var.set("0.1")
        self.llegadatipo4_entry = customtkinter.CTkEntry(self.llegadatipo4_frame, textvariable=self.llegadatipo4_var)
        self.llegadatipo4_entry.grid(row=1, column=0, padx=5, pady=5)

        # Creamos el contenedor para indicar el tiempo entre llegadas de tipo 5
        self.llegadatipo5_frame = customtkinter.CTkFrame(master=master)
        self.llegadatipo5_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nw")
        self.llegadatipo5_lbl = customtkinter.CTkLabel(master=self.llegadatipo5_frame, text="llegadaTipo5")
        self.llegadatipo5_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.llegadatipo5_var = customtkinter.StringVar()
        self.llegadatipo5_var.set("0.09")
        self.llegadatipo5_entry = customtkinter.CTkEntry(self.llegadatipo5_frame, textvariable=self.llegadatipo5_var)
        self.llegadatipo5_entry.grid(row=1, column=0, padx=5, pady=5)

        # Creamos el contenedor para indicar el tiempo entre llegadas de tipo 6
        self.llegadatipo6_frame = customtkinter.CTkFrame(master=master)
        self.llegadatipo6_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nw")
        self.llegadatipo6_lbl = customtkinter.CTkLabel(master=self.llegadatipo6_frame, text="llegadaTipo6")
        self.llegadatipo6_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.llegadatipo6_var = customtkinter.StringVar()
        self.llegadatipo6_var.set("0.08")
        self.llegadatipo6_entry = customtkinter.CTkEntry(self.llegadatipo6_frame, textvariable=self.llegadatipo6_var)
        self.llegadatipo6_entry.grid(row=1, column=0, padx=5, pady=5)

        # Creamos el contenedor para indicar el tiempo entre llegadas de tipo 7
        self.llegadatipo7_frame = customtkinter.CTkFrame(master=master)
        self.llegadatipo7_frame.grid(row=1, column=2, padx=10, pady=10, sticky="nw")
        self.llegadatipo7_lbl = customtkinter.CTkLabel(master=self.llegadatipo7_frame, text="llegadaTipo7")
        self.llegadatipo7_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.llegadatipo7_var = customtkinter.StringVar()
        self.llegadatipo7_var.set("0.05")
        self.llegadatipo7_entry = customtkinter.CTkEntry(self.llegadatipo7_frame, textvariable=self.llegadatipo7_var)
        self.llegadatipo7_entry.grid(row=1, column=0, padx=5, pady=5)

        # Creamos el contenedor para indicar el tiempo entre llegadas de tipo 8
        self.llegadatipo8_frame = customtkinter.CTkFrame(master=master)
        self.llegadatipo8_frame.grid(row=1, column=3, padx=10, pady=10, sticky="nw")
        self.llegadatipo8_lbl = customtkinter.CTkLabel(master=self.llegadatipo8_frame, text="llegadaTipo8")
        self.llegadatipo8_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.llegadatipo8_var = customtkinter.StringVar()
        self.llegadatipo8_var.set("0.05")
        self.llegadatipo8_entry = customtkinter.CTkEntry(self.llegadatipo8_frame, textvariable=self.llegadatipo8_var)
        self.llegadatipo8_entry.grid(row=1, column=0, padx=5, pady=5)

        #Creamos el contenedor para indicar el tiempo que va a tardar en realizarse el servicio tipo 1
        self.serviciotipo1_frame = customtkinter.CTkFrame(master=master)
        self.serviciotipo1_frame.grid(row=1, column=4, padx=10, pady=10, sticky="nw")
        self.serviciotipo1_lbl = customtkinter.CTkLabel(master=self.serviciotipo1_frame, text="mediaServicioTipo1")
        self.serviciotipo1_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.serviciotipo1_var = customtkinter.StringVar()
        self.serviciotipo1_var.set("2")
        self.serviciotipo1_entry = customtkinter.CTkEntry(self.serviciotipo1_frame, textvariable=self.serviciotipo1_var)
        self.serviciotipo1_entry.grid(row=1, column=0, padx=5, pady=5)

        # Creamos el contenedor para indicar el tiempo que va a tardar en realizarse el servicio tipo 1
        self.dserviciotipo1_frame = customtkinter.CTkFrame(master=master)
        self.dserviciotipo1_frame.grid(row=1, column=5, padx=10, pady=10, sticky="nw")
        self.dserviciotipo1_lbl = customtkinter.CTkLabel(master=self.dserviciotipo1_frame, text="desvServicioTipo1")
        self.dserviciotipo1_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.dserviciotipo1_var = customtkinter.StringVar()
        self.dserviciotipo1_var.set("1.1")
        self.dserviciotipo1_entry = customtkinter.CTkEntry(self.dserviciotipo1_frame, textvariable=self.dserviciotipo1_var)
        self.dserviciotipo1_entry.grid(row=1, column=0, padx=5, pady=5)

        # Creamos el contenedor para indicar el tiempo que va a tardar en realizarse el servicio tipo 2
        self.serviciotipo2_frame = customtkinter.CTkFrame(master=master)
        self.serviciotipo2_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nw")
        self.serviciotipo2_lbl = customtkinter.CTkLabel(master=self.serviciotipo2_frame, text="mediaServicioTipo2")
        self.serviciotipo2_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.serviciotipo2_var = customtkinter.StringVar()
        self.serviciotipo2_var.set("5.8")
        self.serviciotipo2_entry = customtkinter.CTkEntry(self.serviciotipo2_frame, textvariable=self.serviciotipo2_var)
        self.serviciotipo2_entry.grid(row=1, column=0, padx=5, pady=5)

        # Creamos el contenedor para indicar el tiempo que va a tardar en realizarse el servicio tipo 2
        self.dserviciotipo2_frame = customtkinter.CTkFrame(master=master)
        self.dserviciotipo2_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nw")
        self.dserviciotipo2_lbl = customtkinter.CTkLabel(master=self.dserviciotipo2_frame, text="desvServicioTipo2")
        self.dserviciotipo2_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.dserviciotipo2_var = customtkinter.StringVar()
        self.dserviciotipo2_var.set("3.1")
        self.dserviciotipo2_entry = customtkinter.CTkEntry(self.dserviciotipo2_frame, textvariable=self.dserviciotipo2_var)
        self.dserviciotipo2_entry.grid(row=1, column=0, padx=5, pady=5)

        # Creamos el contenedor para indicar el tiempo que va a tardar en realizarse el servicio tipo 3
        self.serviciotipo3_frame = customtkinter.CTkFrame(master=master)
        self.serviciotipo3_frame.grid(row=2, column=2, padx=10, pady=10, sticky="nw")
        self.serviciotipo3_lbl = customtkinter.CTkLabel(master=self.serviciotipo3_frame, text="mediaServicioTipo3")
        self.serviciotipo3_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.serviciotipo3_var = customtkinter.StringVar()
        self.serviciotipo3_var.set("6.2")
        self.serviciotipo3_entry = customtkinter.CTkEntry(self.serviciotipo3_frame, textvariable=self.serviciotipo3_var)
        self.serviciotipo3_entry.grid(row=1, column=0, padx=5, pady=5)

        # Creamos el contenedor para indicar el tiempo que va a tardar en realizarse el servicio tipo 3
        self.dserviciotipo3_frame = customtkinter.CTkFrame(master=master)
        self.dserviciotipo3_frame.grid(row=2, column=3, padx=10, pady=10, sticky="nw")
        self.dserviciotipo3_lbl = customtkinter.CTkLabel(master=self.dserviciotipo3_frame, text="desvServicioTipo3")
        self.dserviciotipo3_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.dserviciotipo3_var = customtkinter.StringVar()
        self.dserviciotipo3_var.set("2.7")
        self.dserviciotipo3_entry = customtkinter.CTkEntry(self.dserviciotipo3_frame, textvariable=self.dserviciotipo3_var)
        self.dserviciotipo3_entry.grid(row=1, column=0, padx=5, pady=5)

        # Creamos el contenedor para indicar el tiempo que va a tardar en realizarse el servicio tipo 4
        self.serviciotipo4_frame = customtkinter.CTkFrame(master=master)
        self.serviciotipo4_frame.grid(row=2, column=4, padx=10, pady=10, sticky="nw")
        self.serviciotipo4_lbl = customtkinter.CTkLabel(master=self.serviciotipo4_frame, text="mediaServicioTipo4")
        self.serviciotipo4_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.serviciotipo4_var = customtkinter.StringVar()
        self.serviciotipo4_var.set("6.1")
        self.serviciotipo4_entry = customtkinter.CTkEntry(self.serviciotipo4_frame, textvariable=self.serviciotipo4_var)
        self.serviciotipo4_entry.grid(row=1, column=0, padx=5, pady=5)

        # Creamos el contenedor para indicar el tiempo que va a tardar en realizarse el servicio tipo 4
        self.dserviciotipo4_frame = customtkinter.CTkFrame(master=master)
        self.dserviciotipo4_frame.grid(row=2, column=5, padx=10, pady=10, sticky="nw")
        self.dserviciotipo4_lbl = customtkinter.CTkLabel(master=self.dserviciotipo4_frame, text="desvServicioTipo4")
        self.dserviciotipo4_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.dserviciotipo4_var = customtkinter.StringVar()
        self.dserviciotipo4_var.set("6.1")
        self.dserviciotipo4_entry = customtkinter.CTkEntry(self.dserviciotipo4_frame, textvariable=self.dserviciotipo4_var)
        self.dserviciotipo4_entry.grid(row=1, column=0, padx=5, pady=5)

        # Creamos el contenedor para indicar el tiempo que va a tardar en realizarse el servicio tipo 5
        self.serviciotipo5_frame = customtkinter.CTkFrame(master=master)
        self.serviciotipo5_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nw")
        self.serviciotipo5_lbl = customtkinter.CTkLabel(master=self.serviciotipo5_frame, text="mediaServicioTipo5")
        self.serviciotipo5_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.serviciotipo5_var = customtkinter.StringVar()
        self.serviciotipo5_var.set("10.9")
        self.serviciotipo5_entry = customtkinter.CTkEntry(self.serviciotipo5_frame,
                                                           textvariable=self.serviciotipo5_var)
        self.serviciotipo5_entry.grid(row=1, column=0, padx=5, pady=5)

        # Creamos el contenedor para indicar el tiempo que va a tardar en realizarse el servicio tipo 5
        self.dserviciotipo5_frame = customtkinter.CTkFrame(master=master)
        self.dserviciotipo5_frame.grid(row=3, column=1, padx=10, pady=10, sticky="nw")
        self.dserviciotipo5_lbl = customtkinter.CTkLabel(master=self.dserviciotipo5_frame, text="desvServicioTipo5")
        self.dserviciotipo5_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.dserviciotipo5_var = customtkinter.StringVar()
        self.dserviciotipo5_var.set("5.2")
        self.dserviciotipo5_entry = customtkinter.CTkEntry(self.dserviciotipo5_frame,
                                                           textvariable=self.dserviciotipo5_var)
        self.dserviciotipo5_entry.grid(row=1, column=0, padx=5, pady=5)

        # Creamos el contenedor para indicar el tiempo que va a tardar en realizarse el servicio tipo 6
        self.serviciotipo6_frame = customtkinter.CTkFrame(master=master)
        self.serviciotipo6_frame.grid(row=3, column=2, padx=10, pady=10, sticky="nw")
        self.serviciotipo6_lbl = customtkinter.CTkLabel(master=self.serviciotipo6_frame, text="mediaServicioTipo6")
        self.serviciotipo6_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.serviciotipo6_var = customtkinter.StringVar()
        self.serviciotipo6_var.set("11.2")
        self.serviciotipo6_entry = customtkinter.CTkEntry(self.serviciotipo6_frame,
                                                           textvariable=self.serviciotipo6_var)
        self.serviciotipo6_entry.grid(row=1, column=0, padx=5, pady=5)

        # Creamos el contenedor para indicar el tiempo que va a tardar en realizarse el servicio tipo 6
        self.dserviciotipo6_frame = customtkinter.CTkFrame(master=master)
        self.dserviciotipo6_frame.grid(row=3, column=3, padx=10, pady=10, sticky="nw")
        self.dserviciotipo6_lbl = customtkinter.CTkLabel(master=self.dserviciotipo6_frame, text="desvServicioTipo6")
        self.dserviciotipo6_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.dserviciotipo6_var = customtkinter.StringVar()
        self.dserviciotipo6_var.set("3.9")
        self.dserviciotipo6_entry = customtkinter.CTkEntry(self.dserviciotipo6_frame,
                                                           textvariable=self.dserviciotipo6_var)
        self.dserviciotipo6_entry.grid(row=1, column=0, padx=5, pady=5)

        # Creamos el contenedor para indicar el tiempo que va a tardar en realizarse el servicio tipo 7
        self.serviciotipo7_frame = customtkinter.CTkFrame(master=master)
        self.serviciotipo7_frame.grid(row=3, column=4, padx=10, pady=10, sticky="nw")
        self.serviciotipo7_lbl = customtkinter.CTkLabel(master=self.serviciotipo7_frame, text="mediaServicioTipo7")
        self.serviciotipo7_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.serviciotipo7_var = customtkinter.StringVar()
        self.serviciotipo7_var.set("9")
        self.serviciotipo7_entry = customtkinter.CTkEntry(self.serviciotipo7_frame,
                                                           textvariable=self.serviciotipo7_var)
        self.serviciotipo7_entry.grid(row=1, column=0, padx=5, pady=5)

        # Creamos el contenedor para indicar el tiempo que va a tardar en realizarse el servicio tipo 7
        self.dserviciotipo7_frame = customtkinter.CTkFrame(master=master)
        self.dserviciotipo7_frame.grid(row=3, column=5, padx=10, pady=10, sticky="nw")
        self.dserviciotipo7_lbl = customtkinter.CTkLabel(master=self.dserviciotipo7_frame, text="desvServicioTipo7")
        self.dserviciotipo7_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.dserviciotipo7_var = customtkinter.StringVar()
        self.dserviciotipo7_var.set("5.8")
        self.dserviciotipo7_entry = customtkinter.CTkEntry(self.dserviciotipo7_frame,
                                                           textvariable=self.dserviciotipo7_var)
        self.dserviciotipo7_entry.grid(row=1, column=0, padx=5, pady=5)

        # Creamos el contenedor para indicar el tiempo que va a tardar en realizarse el servicio tipo 8
        self.serviciotipo8_frame = customtkinter.CTkFrame(master=master)
        self.serviciotipo8_frame.grid(row=4, column=0, padx=10, pady=10, sticky="nw")
        self.serviciotipo8_lbl = customtkinter.CTkLabel(master=self.serviciotipo8_frame, text="mediaServicioTipo8")
        self.serviciotipo8_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.serviciotipo8_var = customtkinter.StringVar()
        self.serviciotipo8_var.set("18.7")
        self.serviciotipo8_entry = customtkinter.CTkEntry(self.serviciotipo8_frame,
                                                           textvariable=self.serviciotipo8_var)
        self.serviciotipo8_entry.grid(row=1, column=0, padx=5, pady=5)

        # Creamos el contenedor para indicar el tiempo que va a tardar en realizarse el servicio tipo 8
        self.dserviciotipo8_frame = customtkinter.CTkFrame(master=master)
        self.dserviciotipo8_frame.grid(row=4, column=1, padx=10, pady=10, sticky="nw")
        self.dserviciotipo8_lbl = customtkinter.CTkLabel(master=self.dserviciotipo8_frame, text="desvServicioTipo8")
        self.dserviciotipo8_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.dserviciotipo8_var = customtkinter.StringVar()
        self.dserviciotipo8_var.set("13")
        self.dserviciotipo8_entry = customtkinter.CTkEntry(self.dserviciotipo8_frame,
                                                           textvariable=self.dserviciotipo8_var)
        self.dserviciotipo8_entry.grid(row=1, column=0, padx=5, pady=5)

        # Creamos el contenedor para indicar la razon de aumento
        self.razon_frame = customtkinter.CTkFrame(master=master)
        self.razon_frame.grid(row=4, column=2, padx=10, pady=10, sticky="nw")
        self.razon_lbl = customtkinter.CTkLabel(master=self.razon_frame, text="razonAumento")
        self.razon_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.razon_var = customtkinter.StringVar()
        self.razon_var.set("0.24")
        self.razon_entry = customtkinter.CTkEntry(self.razon_frame,
                                                           textvariable=self.razon_var)
        self.razon_entry.grid(row=1, column=0, padx=5, pady=5)

        # Creamos el contenedor para indicar la maxima capacidad
        self.capacidad_frame = customtkinter.CTkFrame(master=master)
        self.capacidad_frame.grid(row=4, column=3, padx=10, pady=10, sticky="nw")
        self.capacidad_lbl = customtkinter.CTkLabel(master=self.capacidad_frame, text="capacidad")
        self.capacidad_lbl.grid(row=0, column=0, padx=10, pady=0, sticky="s")
        self.capacidad_var = customtkinter.StringVar()
        self.capacidad_var.set("85")
        self.capacidad_entry = customtkinter.CTkEntry(self.capacidad_frame,
                                                  textvariable=self.capacidad_var)
        self.capacidad_entry.grid(row=1, column=0, padx=5, pady=5)

        #Creamos contenedor para la conclusion
        self.conclu_frame = customtkinter.CTkFrame(master=master)
        self.conclu_frame.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="news")
        self.conclu_metrics = customtkinter.CTkLabel(master=self.conclu_frame, text="Conclusión")
        self.conclu_metrics.grid(row=5, column=0, padx=10, pady=0, sticky="swe")

        self.conclu_lbl1 = customtkinter.CTkLabel(master=self.conclu_frame, text="")
        self.conclu_lbl1.grid(row=6, column=0, padx=10, pady=0, sticky="sw")

        # Creamos la barra de progreso
        self.progressbar = ttk.Progressbar(master, variable=self.progress)
        self.progressbar.grid(row=8, column=0, columnspan=6, padx=10, pady=10, sticky="we")

        self.generar_button = customtkinter.CTkButton(self.master, text="Generar simulaciones",
                                                      font=('Calibri', 16, 'bold'), command=self.principal)
        self.generar_button.grid(row=9, column=1, padx=10, pady=10)

    def definirConclusion(self, vectorEstado):
        if vectorEstado.porcentajesobrecargas > 0.20:
            texto = "Reparaciones Limited deberá ampliar sus instalaciones de espera en " + str(vectorEstado.cantidadsemanas) + " semanas"
        else:
            texto = "La cantidad de simulaciones no permite estimar en cuantas semanas se deberá ampliar las instalaciones"
        self.conclu_lbl1.configure(text=texto)

    def principal(self):
         total_simulations = int(self.cantidad_numeros_var.get())
         self.progressbar["maximum"] = total_simulations
         vector = funcionPrincipal(int(self.cantidad_numeros_var.get()), int(self.ver_desde_var.get()),
                         float(self.llegadatipo1_var.get()), float(self.llegadatipo2_var.get()),
                         float(self.llegadatipo3_var.get()), float(self.llegadatipo4_var.get()),
                         float(self.llegadatipo5_var.get()), float(self.llegadatipo6_var.get()),
                         float(self.llegadatipo7_var.get()), float(self.llegadatipo8_var.get()),
                         float(self.serviciotipo1_var.get()), float(self.dserviciotipo1_var.get()),
                         float(self.serviciotipo2_var.get()), float(self.dserviciotipo2_var.get()),
                         float(self.serviciotipo3_var.get()), float(self.dserviciotipo4_var.get()),
                         float(self.serviciotipo4_var.get()), float(self.dserviciotipo4_var.get()),
                         float(self.serviciotipo5_var.get()), float(self.dserviciotipo5_var.get()),
                         float(self.serviciotipo6_var.get()), float(self.dserviciotipo6_var.get()),
                         float(self.serviciotipo7_var.get()), float(self.dserviciotipo7_var.get()),
                         float(self.serviciotipo8_var.get()), float(self.dserviciotipo8_var.get()),
                         float(self.razon_var.get()), int(self.capacidad_var.get()), self)
         self.definirConclusion(vector)
vent = customtkinter.CTk()
app = colasApp(vent)
vent.mainloop()