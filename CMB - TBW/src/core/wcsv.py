# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons
import csv
import os
import xlrd

def wcsv(data, name, folder):	
	csvsalida = open (folder + name, 'w')
	salida = csv.writer(csvsalida, delimiter=',')
	
	if 'combustion' in folder:
		FEmissions = os.path.join('..', 'data', 'in','EmissionFactors', 'FactoresEmision.xlsx')
	if 'wear' in folder:
		FEmissions = os.path.join('..', 'data', 'in', 'EmissionFactors', 'FEBrake.xlsx')
	
	workbook = xlrd.open_workbook(FEmissions)
	names = workbook.sheet_by_index(1)

	listpollutant = []
	for pos in range (1, names.nrows):
		listpollutant.append(str(names.cell_value(pos, 0)))
	salida.writerow(['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h'])
	ID_Grilla = data.keys()

	for ID in ID_Grilla:
		pollutant = data[ID]['pollutants'].keys()
		pollutant = pollutant[0]
		csvsalida.write(data[ID]['General']['ROW'][0])
		csvsalida.write(',')
		csvsalida.write(data[ID]['General']['COL'][0])
		csvsalida.write(',')
		csvsalida.write(data[ID]['General']['LAT'][0])
		csvsalida.write(',')
		csvsalida.write(data[ID]['General']['LON'][0])
		csvsalida.write(',')
		csvsalida.write(pollutant)
		csvsalida.write(',')
		if pollutant in listpollutant:
			csvsalida.write('mol/h')	
		else:
			csvsalida.write('g/h')
		csvsalida.write(',')
		hours = data[ID]['pollutants'][pollutant].keys()
		for hour in hours:
			csvsalida.write(str(data[ID]['pollutants'][pollutant][hour][0]))
			csvsalida.write(',')
		csvsalida.write(str(data[ID]['pollutants'][pollutant][0][0]))
		csvsalida.write('\n')

	data = None
	csvsalida.close()
	
def writematriz(matriz, folder):

	csvsalida = open(folder + '.csv', 'w')
	salida = csv.writer(csvsalida, delimiter=',')

	for x in range(0, matriz.shape[0]):
		salida.writerow(matriz[x])
	matriz = None
	csvsalida.close()

def writesum(data):
	folder = os.path.join('..', 'data', 'flows', '')
	csvsalida = open(folder +'sumcol.csv', 'w')
	salida = csv.writer(csvsalida, delimiter=',')

	salida.writerow(['Estacion', 'IDEstacion', 'IDNodo', '>C5', 'AL', 'AT', 'B', 'BA', 'BT', 'C', 'C2G', 'C2P', 'C3-C4', 'C5', 'ESP', 'INT', 'L', 'M', 'TOTAL', 'NH_>C5', 'NH_AL', 'NH_AT', 'NH_B', 'NH_BA', 'NH_BT', 'NH_C', 'NH_C2G', 'NH_C2P', 'NH_C3-C4', 'NH_C5', 'NH_ESP', 'NH_INT', 'NH_L', 'NH_M', 'NH_TOTAL'])

	IDEstation = data.keys()
	
	for ID in IDEstation: 

		flujos = sorted(data[ID]['HABIL'].keys())

		for veh in range(0, 3):
			csvsalida.write(data[ID]['GENERAL'][veh])
			csvsalida.write(',')
		
		for vehicles in flujos:
				csvsalida.write(str(data[ID]['HABIL'][vehicles]))
				csvsalida.write(',')

		for vehicles in flujos:
				csvsalida.write(str(data[ID]['NOHAB'][vehicles]))
				csvsalida.write(',')
		csvsalida.write('\n')
	data = None
	csvsalida.close()

def writebinding(folder, data, name):

	csvsalida = open(folder + name +'binding.csv', 'w')
	nameData = ['FID','hora'] #'>C5_DSEL', '>C5_GNV', '>C5_GAS', 'AL_DSEL', 'AT_DSEL', 'AUT_GNV', 'AUT_GAS', 'BA_DSEL', 'BT_DSEL', 'B_DSEL', 'C2G_DSEL', 'C2G_GNV', 'C2G_GAS', 'C2P_DSEL', 'C2P_GNV', 'C2P_GAS', 'C3-C4_DSEL', 'C3-C4_GNV', 'C3-C4_GAS', 'CC_DSEL', 'CC_GNV', 'CC_GAS', 'ESP_DSEL', 'ESP_GNV', 'ESP_GAS', 'INT_DSEL', 'INT_GNV', 'INT_GAS', 'MB_DSEL', 'M_GAS', 'TX_GNV', 'TX_GAS', 'C5_DSEL', 'C5_GNV', 'C5_GAS', 'NH>C5_DSEL', 'NH>C5_GNV', 'NH>C5_GAS', 'NHAL_DSEL', 'NHAT_DSEL', 'NHAUT_GNV', 'NHAUT_GAS', 'NHBA_DSEL', 'NHBT_DSEL', 'NHB_DSEL', 'NHC2G_DSEL', 'NHC2G_GNV', 'NHC2G_GAS', 'NHC2P_DSEL', 'NHC2P_GNV', 'NHC2P_GAS', 'NHC3-C4_DSEL', 'NHC3-C4_GNV', 'NHC3-C4_GAS', 'NHCC_DSEL', 'NHCC_GNV', 'NHCC_GAS', 'NHESP_DSEL', 'NHESP_GNV', 'NHESP_GAS', 'NHINT_DSEL', 'NHINT_GNV', 'NHINT_GAS', 'NHMB_DSEL', 'NHM_GAS', 'NHTX_GNV', 'NHTX_GAS', 'NHC5_DSEL', 'NHC5_GNV', 'NHC5_GAS']
	FID = data.keys()

	nameVehicle = sorted(data[FID[0]]['flows']['HABIL'][0])
	nameHabil = nameData + nameVehicle
	nameNHabil = nameVehicle

	cont = 0
	
	for ID in FID:
		nameslinks = data[ID]['link'].keys()
		namevehicle = sorted(data[ID]['flows']['HABIL'][0].keys())
		hours = data[ID]['flows']['HABIL'].keys()

		if cont == 0:
			for name in nameslinks:
				csvsalida.write(name)
				csvsalida.write(',')
	
			for name in nameHabil:
				csvsalida.write(name)
				csvsalida.write(',')
			
			for name in nameNHabil:
				if name == nameNHabil[0]:
					csvsalida.write('NH' + name)
				else: 
					csvsalida.write(',')
					csvsalida.write('NH' + name)
			csvsalida.write('\n')
			cont += 1
	 	

		for hour in hours:

		 	for name in nameslinks:
		 		csvsalida.write(data[ID]['link'][name][0])
		 		csvsalida.write(',')
		 	csvsalida.write(str(ID))
		 	csvsalida.write(',')
		 	csvsalida.write(str(hour))
		 	csvsalida.write(',')

		 	for vehicle in nameVehicle:
		 		csvsalida.write (str(data[ID]['flows']['HABIL'][hour][vehicle]))
		 		csvsalida.write(',')
		 	cont = 0
		 	for vehicle in nameVehicle:
		 		if cont == 0:
		 			csvsalida.write (str(data[ID]['flows']['HABIL'][hour][vehicle]))
		 			cont += 1
		 		else:
		 			csvsalida.write(',')
		 			csvsalida.write (str(data[ID]['flows']['NOHAB'][hour][vehicle]))
		 			
		 	csvsalida.write('\n')
		data[ID] = None
	data = None
	csvsalida.close()

def writeBindingSecondary(folder, data, name, Typo):

	csvsalida = open(folder + name + '_' + Typo + '_' +'binding.csv', 'w')
	nameData = ['FID','hora']
	#if Typo == 'HABIL':
	#	namevehiclefull = ['FID','hora'] '>C5_DSEL', '>C5_GNV', '>C5_GAS', 'AL_DSEL', 'AT_DSEL', 'AUT_GNV', 'AUT_GAS', 'BA_DSEL', 'BT_DSEL', 'B_DSEL', 'C2G_DSEL', 'C2G_GNV', 'C2G_GAS', 'C2P_DSEL', 'C2P_GNV', 'C2P_GAS', 'C3-C4_DSEL', 'C3-C4_GNV', 'C3-C4_GAS', 'CC_DSEL', 'CC_GNV', 'CC_GAS', 'ESP_DSEL', 'ESP_GNV', 'ESP_GAS', 'INT_DSEL', 'INT_GNV', 'INT_GAS', 'MB_DSEL', 'M_GAS', 'TX_GNV', 'TX_GAS', 'C5_DSEL', 'C5_GNV', 'C5_GAS']
	#elif Typo == 'NOHAB': 
	#	namevehiclefull = ['FID','hora', 'NH>C5_DSEL', 'NH>C5_GNV', 'NH>C5_GAS', 'NHAL_DSEL', 'NHAT_DSEL', 'NHAUT_GNV', 'NHAUT_GAS', 'NHBA_DSEL', 'NHBT_DSEL', 'NHB_DSEL', 'NHC2G_DSEL', 'NHC2G_GNV', 'NHC2G_GAS', 'NHC2P_DSEL', 'NHC2P_GNV', 'NHC2P_GAS', 'NHC3-C4_DSEL', 'NHC3-C4_GNV', 'NHC3-C4_GAS', 'NHCC_DSEL', 'NHCC_GNV', 'NHCC_GAS', 'NHESP_DSEL', 'NHESP_GNV', 'NHESP_GAS', 'NHINT_DSEL', 'NHINT_GNV', 'NHINT_GAS', 'NHMB_DSEL', 'NHM_GAS', 'NHTX_GNV', 'NHTX_GAS', 'NHC5_DSEL', 'NHC5_GNV', 'NHC5_GAS']
	FID = data.keys()

	nameCategories = sorted(data[FID[0]]['flows'][Typo][0])
	nameVehicle = nameData + nameCategories


	cont = 0
	for ID in FID:
		nameslinks = data[ID]['link'].keys()
		Typ = data[ID]['flows'].keys()
		Typ = Typ[0]
		#namevehicle = sorted(data[ID]['flows'][Typ][0].keys())
		hours = data[ID]['flows'][Typ].keys()

		if cont == 0:
			for name in nameslinks:
				csvsalida.write(name)
				csvsalida.write(',')
			if Typo == 'HABIL':
				for name in nameVehicle:
					if name == nameVehicle[0]:
						csvsalida.write(name)			
					else: 
						csvsalida.write(',')
						csvsalida.write(name)
				csvsalida.write('\n')
			if Typo == 'NOHAB': 
				for name in nameVehicle:
					if name == nameVehicle[0]:
						csvsalida.write('NH' + name)			
					else: 
						csvsalida.write(',')
						csvsalida.write('NH' + name)
				csvsalida.write('\n')		
			cont += 1

		for hour in hours:

		 	for name in nameslinks:
		 		csvsalida.write(data[ID]['link'][name][0])
		 		csvsalida.write(',')
		 	csvsalida.write(str(ID))
		 	csvsalida.write(',')
		 	csvsalida.write(str(hour))
		 	for vehicle in nameCategories:
		 		csvsalida.write(',')
		 		csvsalida.write(str(data[ID]['flows'][Typo][hour][vehicle][0]))
		 	csvsalida.write('\n')
		data[ID] = None
	data = None
	csvsalida.close()	

def writeemsions(data, name, pollutant, Typo, id): 

	name = name + '_' + pollutant + '_' + Typo
	if id == 1: 
		folder = os.path.join('..', 'data','out','emissions', 'link', 'combustion', '')
	if id == 2:
		folder = os.path.join('..', 'data','out','emissions', 'link', 'wear', '')

	csvsalida = open(folder + name + '.csv', 'w')
	salida = csv.writer(csvsalida, delimiter=',')


	salida.writerow(['FID_LINK', 'FID_Grilla', 'ROW', 'COL', 'LAT', 'LON', 'Contaminante', 'Hora 0','', 'Hora 1','', 'Hora 2','', 'Hora 3','', 'Hora 4','', 'Hora 5','', 'Hora 6','', 'Hora 7','', 'Hora 8','', 'Hora 9','', 'Hora 10','', 'Hora 11','', 'Hora 12','', 'Hora 13','', 'Hora 14','', 'Hora 15','', 'Hora 16','', 'Hora 17','', 'Hora 18','', 'Hora 19','', 'Hora 20','', 'Hora 21','', 'Hora 22','', 'Hora 23',''])
		
	FID_LINK = data.keys()

	for ID in FID_LINK:
		csvsalida.write(str(int(float(ID))))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['FID_Grilla'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['ROW'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['COL'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['LAT'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['LON'][0]))
		csvsalida.write(',')
		csvsalida.write(pollutant)
		csvsalida.write(',')
		
		hours = data[ID]['pollutants'].keys()

		for hour in hours:
			if hour == 23:
				csvsalida.write(str(data[ID]['pollutants'][hour][Typo][0]))
				csvsalida.write(',')
				csvsalida.write(str(data[ID]['pollutants'][hour][Typo][1]))
			
			else:
				csvsalida.write(str(data[ID]['pollutants'][hour][Typo][0]))
				csvsalida.write(',')
				csvsalida.write(str(data[ID]['pollutants'][hour][Typo][1]))
				csvsalida.write(',')



		csvsalida.write('\n')

	data = None
	csvsalida.close()	

def PMC(data, noun, folder):

	if 'TIRE' in noun or 'BRAKE' in noun:
		folder = os.path.join('..', 'data','out', 'emissions', 'grid', 'PMC', 'Wear', '')
	else: 
		folder = os.path.join('..', 'data' ,'out', 'emissions', 'grid', 'PMC', 'Combustion', '')
	csvsalida = open(folder + noun + '.csv', 'w')
	salida = csv.writer(csvsalida, delimiter=',')
	keys = data.keys()

	salida.writerow(['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h'])
	for key in keys: 
		csvsalida.write(str(int(data[key]['GENERAL']['ROW'][0])))
		csvsalida.write(',')
		csvsalida.write(str(int(data[key]['GENERAL']['COL'][0])))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['GENERAL']['LAT'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['GENERAL']['LON'][0]))
		csvsalida.write(',')
		csvsalida.write('PMC')
		csvsalida.write(',')
		if data[key]['GENERAL']['UNIT'][0] == 'mol/h':
			csvsalida.write('mol/s')
		if data[key]['GENERAL']['UNIT'][0] == 'g/h':
			csvsalida.write('g/s')
		hours = data[key]['hours'].keys()
		for hour in hours:
			csvsalida.write(',')
			csvsalida.write(str(data[key]['hours'][hour][0]))
		csvsalida.write('\n')
			
	data = None
	csvsalida.close()	

def writevehicle(data, noun, pollutant, Typo, id):
	
	if id == 1:
		folder = os.path.join('..', 'data', 'out', 'category', 'link', '')
		
		keys = data.keys()
		csvsalida = open(folder + noun + '_' + pollutant +'_'+ Typo + '.csv', 'w')
		salida = csv.writer(csvsalida, delimiter=',')
		salida.writerow(['FID_LINK', 'FID_Grilla', 'COL', 'ROW', 'LAT', 'LON', 'Type', 'POLNAME' ,'Category','Hora 0', 'Hora 1', 'Hora 2', 'Hora 3', 'Hora 4', 'Hora 5', 'Hora 6', 'Hora 7', 'Hora 8', 'Hora 9', 'Hora 10', 'Hora 11', 'Hora 12', 'Hora 13', 'Hora 14', 'Hora 15', 'Hora 16', 'Hora 17', 'Hora 18', 'Hora 19', 'Hora 20', 'Hora 21', 'Hora 22', 'Hora 23'])		
		
		for key in keys: 
			Types = data[key]['pollutants'][0].keys()	
			for Type in Types: 
				categories = data[key]['pollutants'][0][Type].keys()
				for category in categories:
					csvsalida.write(str(key))
					csvsalida.write(',')
					csvsalida.write(str(data[key]['General']['FID_Grilla'][0]))
					csvsalida.write(',')
					csvsalida.write(str(data[key]['General']['COL'][0]))
					csvsalida.write(',')
					csvsalida.write(str(data[key]['General']['ROW'][0]))
					csvsalida.write(',')
					csvsalida.write(str(data[key]['General']['LAT'][0]))
					csvsalida.write(',')
					csvsalida.write(str(data[key]['General']['LON'][0]))
					csvsalida.write(',')
					csvsalida.write(Type)
					csvsalida.write(',')
					csvsalida.write(pollutant)
					csvsalida.write(',')
					csvsalida.write(category)
					hours = data[key]['pollutants'].keys()

					for hour in hours: 
						csvsalida.write(',')
						csvsalida.write(str(float(data[key]['pollutants'][hour][Type][category])))
					csvsalida.write('\n')				
		data = None
		csvsalida.close()

	if id == 2: 

		folder = os.path.join('..', 'data','out', 'category', 'grid', '')
		
		csvsalida = open(folder + noun, 'w')
		salida = csv.writer(csvsalida, delimiter=',')

		salida.writerow(['FID_Grilla', 'Type', 'Category' , 'COL', 'ROW', 'LAT', 'LON', 'POLNAME', 'Hora 0', 'Hora 1', 'Hora 2', 'Hora 3', 'Hora 4', 'Hora 5', 'Hora 6', 'Hora 7', 'Hora 8', 'Hora 9', 'Hora 10', 'Hora 11', 'Hora 12', 'Hora 13', 'Hora 14', 'Hora 15', 'Hora 16', 'Hora 17', 'Hora 18', 'Hora 19', 'Hora 20', 'Hora 21', 'Hora 22', 'Hora 23'])
		keys = data.keys ()

		for key in keys: 
			Types = data[key]['Type'].keys()
			for Type in Types:
				categories = data[key]['Type'][Type].keys()
				for category in categories: 
					csvsalida.write(str(key))
					csvsalida.write(',')
					csvsalida.write(Type)
					csvsalida.write(',')
					csvsalida.write(category)
					csvsalida.write(',')
					csvsalida.write(data[key]['General']['COL'][0])
					csvsalida.write(',')
					csvsalida.write(data[key]['General']['ROW'][0])
					csvsalida.write(',')
					csvsalida.write(data[key]['General']['LAT'][0])
					csvsalida.write(',')
					csvsalida.write(data[key]['General']['LON'][0])
					csvsalida.write(',')
					csvsalida.write(data[key]['General']['POLNAME'][0])
					hours = data[key]['Type'][Type][category].keys()
					for hour in hours: 
						csvsalida.write(',')
						csvsalida.write(str(data[key]['Type'][Type][category][hour]))

					csvsalida.write('\n')
		data = None
		csvsalida.close()

def writecarburant(data, noun, pollutant, Typo,  id):
	
	if id == 1:
		folder = os.path.join('..', 'data', 'out', 'carburant', 'link', '')
		
		keys = data.keys()
		csvsalida = open(folder + noun + '_' + pollutant+ '_' + Typo + '.csv', 'w')
		salida = csv.writer(csvsalida, delimiter=',')
		salida.writerow(['FID_LINK', 'FID_Grilla', 'COL', 'ROW', 'LAT', 'LON', 'Type', 'POLNAME' ,'Category','Hora 0', 'Hora 1', 'Hora 2', 'Hora 3', 'Hora 4', 'Hora 5', 'Hora 6', 'Hora 7', 'Hora 8', 'Hora 9', 'Hora 10', 'Hora 11', 'Hora 12', 'Hora 13', 'Hora 14', 'Hora 15', 'Hora 16', 'Hora 17', 'Hora 18', 'Hora 19', 'Hora 20', 'Hora 21', 'Hora 22', 'Hora 23'])		
		
		for key in keys: 
			Types = data[key]['pollutants'][0].keys()	
			for Type in Types: 
				categories = data[key]['pollutants'][0][Type].keys()
				for category in categories:
					csvsalida.write(str(key))
					csvsalida.write(',')
					csvsalida.write(str(data[key]['General']['FID_Grilla'][0]))
					csvsalida.write(',')
					csvsalida.write(str(data[key]['General']['COL'][0]))
					csvsalida.write(',')
					csvsalida.write(str(data[key]['General']['ROW'][0]))
					csvsalida.write(',')
					csvsalida.write(str(data[key]['General']['LAT'][0]))
					csvsalida.write(',')
					csvsalida.write(str(data[key]['General']['LON'][0]))
					csvsalida.write(',')
					csvsalida.write(Type)
					csvsalida.write(',')
					csvsalida.write(pollutant)
					csvsalida.write(',')
					csvsalida.write(category)
					hours = data[key]['pollutants'].keys()
					for hour in hours: 
						csvsalida.write(',')
						csvsalida.write(str(float(data[key]['pollutants'][hour][Type][category])))
					csvsalida.write('\n')
		data = None				
		csvsalida.close()

	if id == 2: 
		folder = os.path.join('..', 'data', 'out', 'carburant', 'grid', '')
		
		csvsalida = open(folder + noun, 'w')
		salida = csv.writer(csvsalida, delimiter=',')

		salida.writerow(['FID_Grilla', 'Type', 'Category' , 'COL', 'ROW', 'LAT', 'LON', 'POLNAME', 'Hora 0', 'Hora 1', 'Hora 2', 'Hora 3', 'Hora 4', 'Hora 5', 'Hora 6', 'Hora 7', 'Hora 8', 'Hora 9', 'Hora 10', 'Hora 11', 'Hora 12', 'Hora 13', 'Hora 14', 'Hora 15', 'Hora 16', 'Hora 17', 'Hora 18', 'Hora 19', 'Hora 20', 'Hora 21', 'Hora 22', 'Hora 23'])
		keys = data.keys ()

		for key in keys: 
			Types = data[key]['Type'].keys()
			for Type in Types:
				categories = data[key]['Type'][Type].keys()
				for category in categories: 
					csvsalida.write(str(key))
					csvsalida.write(',')
					csvsalida.write(Type)
					csvsalida.write(',')
					csvsalida.write(category)
					csvsalida.write(',')
					csvsalida.write(data[key]['General']['COL'][0])
					csvsalida.write(',')
					csvsalida.write(data[key]['General']['ROW'][0])
					csvsalida.write(',')
					csvsalida.write(data[key]['General']['LAT'][0])
					csvsalida.write(',')
					csvsalida.write(data[key]['General']['LON'][0])
					csvsalida.write(',')
					csvsalida.write(data[key]['General']['POLNAME'][0])
					hours = data[key]['Type'][Type][category].keys()
					for hour in hours: 
						csvsalida.write(',')
						csvsalida.write(str(data[key]['Type'][Type][category][hour]))

					csvsalida.write('\n')
		data = None
		csvsalida.close()

def writedeparture(data, noun, poll, Typo):
	folder = os.path.join('..', 'data','out', 'departure', '')
	keys = data.keys()
	csvsalida = open(folder + noun + '_' + poll+ '_' + Typo + '.csv', 'w')
	salida = csv.writer(csvsalida, delimiter=',')

	names = ['FID_LINK', 'FID_Grilla', 'LAT', 'LON', 'ROW', 'COL', 'hora']
	keys = data.keys()
	cont = 0

	for key in keys: 
		if cont == 0:
			names2 = data[key]['pollutants'][0][Typo].keys()
			names = names + names2
			cont2 = 0
			for name in names:
				if cont2 == 0: 
					csvsalida.write(name)
					cont2 = 1
				elif cont2 == 1:
					csvsalida.write(',')
					csvsalida.write(name)
			csvsalida.write('\n')
			cont = 1 

		hours = data[key]['pollutants'].keys()
		for hour in hours:
			csvsalida.write(str(key))
			csvsalida.write(',')
			csvsalida.write(str(data[key]['General']['FID_Grilla'][0]))
			csvsalida.write(',')
			csvsalida.write(str(data[key]['General']['LAT'][0]))
			csvsalida.write(',')
			csvsalida.write(str(data[key]['General']['LON'][0]))
			csvsalida.write(',')
			csvsalida.write(str(data[key]['General']['ROW'][0]))
			csvsalida.write(',')
			csvsalida.write(str(data[key]['General']['COL'][0]))
			csvsalida.write(',')
			csvsalida.write(str(hour))
			for name in names2:
				csvsalida.write(',')
				csvsalida.write(str(data[key]['pollutants'][hour][Typo][name][0]))
			csvsalida.write('\n')