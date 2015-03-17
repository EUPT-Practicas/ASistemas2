'''
@autores: Ricardo y Javier

'''

#!/usr/bin/python
import sys, os, string, commands

def listar(directorio):
	lista = []
	print "|"+directorio+"|"
	print "\n ----------------- "
	print " Directorio: "+directorio
	if os.path.isdir(directorio):
		permisos = string.rsplit(commands.getoutput("ls -l " + directorio + " | grep -v 'total' | cut -d ' ' -f 1"),"\n") 		
		archivos = string.rsplit(commands.getoutput("ls -1 " + directorio),"\n")
		print " Permisos   Nombre "
		print " ----------------- "
		for i in range(len(permisos)):
			print permisos[i] + " " + archivos[i]
			if os.path.isdir(archivos[i]):
				lista.append(archivos[i])
	else:
		print directorio + ": No es un directorio valido."
	for i in range(len(lista)):
		if comprob_permisos(lista[i]):
			print lista[i]
			listar(lista[i])

def comprob_permisos(archivo):
	status, out = commands.getstatusoutput("ls -l " + archivo)
	if status > 0:
		print "\nERROR: El directorio "+archivo+" no es accesible por el usuario.\n"
		return False
	else:
		return True


#Inicio programa

if len(sys.argv) == 1:
	directorio = raw_input("Introduzca el nombre del directorio: ")
	if comprob_permisos(directorio):
		listar(directorio)
else:
	print "ERROR: No debe de introducir ningun parametro"
