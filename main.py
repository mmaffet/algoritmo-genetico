#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#	==================
#	Algorítmo genético
#	==================
#
#	Autor
#	Miguel Ángel Maffet Wall
#	Junio 2017
#

#	Librerias
from pprint import pprint
import random
import numpy

#	Funciones

def init(size):
   	"Creamos una matriz aleatoria de tamaño size"
   	return numpy.random.randint(10, size = (size,size))

def fitness(candidato):
   "Obtenemos el fitness de un candidato (como el costo más alto)"
   return


#	Main

def main():
	matriz = init(10)
   	pprint(matriz)
   	print "El máximo es: "
   	print numpy.max(matriz)
   	print "Tiene nodos (activos): "
   	print numpy.count_nonzero(matriz)
   	return 0;

main()