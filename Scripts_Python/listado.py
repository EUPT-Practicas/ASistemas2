'''
@autores: Ricardo y Javier

'''

#!/usr/bin/python
import sys, os, string, commands


COMANDO = "ls -la "

if len(sys.argv) == 2:
	directorio = sys.argv[1]
	if os.path.isdir(directorio):
		permisos = string.rsplit(commands.getoutput("ls -l "+ directorio +" | grep -v 'total' | cut -d ' ' -f 1"),"\n") 		
		archivos = string.rsplit(commands.getoutput("ls -1 "+ directorio),"\n")
		print " Permisos   Nombre"
		for i in range(len(permisos)):
			print permisos[i] + " " + archivos[i]
		
	else:
		print directorio + ": No es un directorio valido."	

else:
	print "ERROR: Los parametros introducidos no son correctos"
	print "La forma correcta es: listado.py [directorio]"




	#os.system(comando + directorio)
	

