"""Las propiedades nos permiten definir operaciones (metodos) y tratarlas como
si fueran parte de la clase (atributos)"""

class Circulo:

    def __init__(self, radio):
        self.radio = radio

    @property
    def area(self):
        return 3.1415*(self.radio**2)

c = Circulo(10)
print("El area del circulo es "+str(int(c.area)))
