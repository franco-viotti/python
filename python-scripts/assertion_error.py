def promedio_lista(lista):
	assert len(lista) > 0, "La lista esta vacia"
	return sum(lista)/len(lista)

promedio = promedio_lista(lista=[1,2,3,4,5,6])
print("No hubo errores")
