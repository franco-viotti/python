import threading
import time

class MiHilo(threading.Thread): #Esto significa que heredamos de Threading
    def run(self): #Este metodo se hereda
        print("{} inicio ".format(self.getName()))
        time.sleep(1)
        print("{} terminado ".format(self.getName()))

if __name__ == "__main__":
    for x in range(4):
        hilo = MiHilo(name = "Thread-{}".format(x+1))
        hilo.start()
        time.sleep(1) #Jugando con este timpo podemos ver como la creacion y terminacion de los hilos se solapa entre ellos