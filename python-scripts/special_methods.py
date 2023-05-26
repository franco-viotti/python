"""Los metodos especiales son aquellos que empiezan y terminan con doble _ """
# El "init" es el metodo encargado de realizar las tareas de inicializacion 
# cuando la instancia de una clase es creada
# El "new" sirve para personalizar la creacion de las instancias de la clase.  
# En el caso del "new" no requiere un self. 
# Siempre recibe una referencia a la clase que lo esta invocando --> (super)    
# El metodo "new" requiere un 'cls' y ademas debe devolver un 'super'
# Si no ponemos el 'return' el metodo init no sera llamado  

class Clase():
    def __new__(cls):
        print("new method is being called")
        #return super().__new__(cls)
    def __init__(self):
        print("init method is breing called")
    
     
c = Clase()