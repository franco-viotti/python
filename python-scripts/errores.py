def validar_x(x):
	if(x<1):
		raise Exception("La variable x debe ser mayor que 1")
	else:
		print("x es mayor que 1")

x=0
validar_x(x)
