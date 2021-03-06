# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons

import os
from matriz import *
from wcsv import *
import json


def listaCSV(direccion):

	path = os.path.join(direccion,'')

	lstFilesEmissions = []

	lstDir = os.walk(path)  
	datos = {}

	for root, dirs, files in lstDir:
	    for fichero in files:
	        (nombreFichero, extension) = os.path.splitext(fichero)
	        if(extension == '.csv'):
	        	lstFilesEmissions.append(nombreFichero+extension)

	return lstFilesEmissions

def pmc(folder): 

	listEmitions = listaCSV(folder)	

	listEmitionsPM25 = []
	listEmitionsPM10 = []

	for name in listEmitions:
		if 'PM2.5' in name: 
			listEmitionsPM25.append(name)
		if 'PM10' in name: 
			listEmitionsPM10.append(name)

	for i in range (0, len(listEmitionsPM25)):
		archivePM25 = listEmitionsPM25[i]
		if '2.5' in listEmitionsPM25[i]:
			archivePM10 = listEmitionsPM25[i].replace('2.5', '10')
		elif '25' in listEmitionsPM25[i]:
			archivePM10 = listEmitionsPM25[i].replace('25', '10')
		else: 
			print 'Error'

		archivePM25 = folder + archivePM25
		archivePM10 = folder + archivePM10

		MPM25 = convertCSVMatriz(archivePM25)
		MPM10 = convertCSVMatriz(archivePM10)

		data = {}

		head = MPM25[0,:]

		index = 0
		for value in head: 
			if value == 'ROW': 
				colROW = index
			if value == 'COL':
				colCOL = index
			if value == 'LAT': 
				colLAT = index
			if value == 'LON': 
				colLON = index
			if value == 'UNIT': 
				colUNIT = index
			index += 1 

		for y in range(1, MPM25.shape[0]):
			key = MPM25[y][colROW] + MPM25[y][colCOL]
			

			if data.get(key) is None: 
				data[key] = {}
				data[key]['GENERAL'] = {'COL': [], 'ROW': [], 'LAT': [], 'LON': [], 'UNIT': []}
				data[key]['hours'] = {}


			if data[key]['GENERAL']['COL'] == []:
				data[key]['GENERAL']['COL'].append(MPM10[y][colCOL])
				data[key]['GENERAL']['ROW'].append(MPM10[y][colROW])
				data[key]['GENERAL']['LAT'].append(MPM10[y][colLAT])
				data[key]['GENERAL']['LON'].append(MPM10[y][colLON])
				data[key]['GENERAL']['UNIT'].append(MPM10[y][colUNIT])

			entryhours = data[key]['hours']
			for hour in range(0, 25):
				if entryhours.get(hour) is None: 
					entryhours[hour] = []

			hour = 0
			for x in range(6, MPM25.shape[1]): 
				data[key]['hours'][hour].append((float(MPM10[y][x])/3600) - (float(MPM25[y][x])/3600))
				hour += 1

		noun = listEmitionsPM25[i]


		if 'PM2.5 BRAKE' in noun: 
			noun = noun.replace('PM2.5 BRAKE', 'BRAKE')
		if 'PM2.5 TIRE' in noun: 
			noun = noun.replace('PM2.5 TIRE', 'TIRE')
		if '_PM2.5_' in noun:
			noun = noun.replace('_PM2.5_', '_')

		noun = 'PMC_' + noun 
		
		PMC(data, noun, folder)

def testingpmc(folder):
	List = listaCSV(folder)
	listPMC = []
	for archive in List:
		if 'PMC' in archive:
			listPMC.append(archive)

	for name in listPMC: 
		MPMC = convertCSVMatriz(folder + name)

		for  i in range(1, MPMC.shape[0]):
			for x in range(6, MPMC.shape[1]):
				number = float(MPMC[i][x])
				if  number < 0 or number < 0.0: 
					print 'Review process number <0'
				elif number > 0 or number > 0.0: 
					pass
					
def bindingpmc(folder): 
	
	listout = listaCSV(folder)
	listHabil = []
	listNHabil = []
	cont = 0
	
	folderSave = os.path.join('..', 'data', 'out', 'emissions', 'grid', 'PMC', 'Full', '')
	for archiv in listout:
		if '_NHabil' in archiv: 
			listNHabil.append(archiv)
		elif '_Habil' in archiv: 
			listHabil.append(archiv)

	if 'Wear' in folder: 
		folderSave = os.path.join(folderSave + 'Wear', '')
		
	elif 'Combustion' in folder: 
		folderSave = os.path.join(folderSave + 'Combustion', '')
		

	names = ['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h']
	
	csvsalida = open(folderSave + 'Habil_PMC_FULL.csv', 'w')
	for name in names: 
		if name == 'ROW': 
			csvsalida.write(name)
		else: 
			csvsalida.write(',')
			csvsalida.write(name)
	csvsalida.write('\n')

	for archiv in listHabil: 
		archive = folder + archiv
		matriz = convertCSVMatriz(archive)
		for i in range(1, matriz.shape[0]):
			for x in range(0, matriz.shape[1]):
				if x == 0: 
					csvsalida.write(matriz[i][x])
				else: 
					csvsalida.write(',')
					csvsalida.write(matriz[i][x])
			csvsalida.write('\n')
	
	csvsalida = open(folderSave + 'NHabil_PMC_FULL.csv', 'w')
	for name in names: 
		if name == 'ROW': 
			csvsalida.write(name)
		else: 
			csvsalida.write(',')
			csvsalida.write(name)
	csvsalida.write('\n')


	for archiv in listNHabil: 
		archive = folder + archiv
		matriz = convertCSVMatriz(archive)
		for i in range(1, matriz.shape[0]):
			for x in range(0, matriz.shape[1]):
				if x == 0: 
					csvsalida.write(matriz[i][x])
				else: 
					csvsalida.write(',')
					csvsalida.write(matriz[i][x])
			csvsalida.write('\n')

