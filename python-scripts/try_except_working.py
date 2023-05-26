def calcular_promedio(lista):
	return sum(lista)/len(lista)

try:
	promedio = calcular_promedio(lista=[1, 2, 3, 4, 5])
	print(f"El promedio de la lista es {int(promedio)}")
except Exception as e:
	print("La función no calculó el promedio")
	print(e)
