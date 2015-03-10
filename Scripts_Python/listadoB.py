./<'''
@autores: Ricardo y Javier

'''

#!/usr/bin/python
import sys, os, string, commands

#COMANDO = "ls -la "

if len(sys.argv) == 1:
	directorio = raw_input("Introduzca el nombre del directorio: ")
	if os.path.isdir(directorio):
		permisos = string.rsplit(commands.getoutput("ls -lR " + directorio + " | grep -v 'total' | cut -d ' ' -f 1"),"\n") 		
		archivos = string.rsplit(commands.getoutput("ls -1R " + directorio),"\n")
		#comprobar = permisos[0]
		print "Esto es:" + permisos[6] + "."
		print " Permisos   Nombre"
		for i in range(len(permisos)):
			comprobar = permisos[i]		
			if(comprobar != ""):
				if(comprobar[0] == "." and  comprobar[1] == "/"):
					print  permisos[i]
					i += 1
			print permisos[i] + " " + archivos[i]
		
	else:
		print directorio + ": No es un directorio valido."	

else:
	print "ERROR: No debe de introducir ningun parametro"
	





	

