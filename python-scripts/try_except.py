def calcular_promedio(lista):
	assert len(lista) > 0, "La lista está vacía"
	return sum(lista)/len(lista)

try: 
	promedio = calcular_promedio(lista=[])
	print(promedio)
except AssertionError as assert:
	print(assert)
except Exception as e:
	print("La función no pudo ejecutarse")
	print(e)
