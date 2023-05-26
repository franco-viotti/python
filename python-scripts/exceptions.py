lista = [1,2,3]

try:
    print(lista[1])
except Exception as e:
    print("Algo salio mal")
else:
    print("No hay error")
finally:
    print("Linea ejecutada si o si")