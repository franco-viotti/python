def primerD(funcion):
    def funcionDecorada(*args, **kkwars):
        print("Primer decorador")
    return funcionDecorada

@primerD
def funcion():
    print("Mi primer decorador")

funcion()


