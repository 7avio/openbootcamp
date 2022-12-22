import pickle

def readFile():
    newRead = open('ejercicio_8-2.bin', 'rb')
    car = pickle.load(newRead)
    newRead.close()
    print(type(car))
    print(car)


class Vehiculo:
    def __init__(self):
        self.color = 'red'
        self.ruedas = '4'
        self.puertas = '4'


class Coche(Vehiculo):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.velocidad = 160
        self.cilindrada = 1.3

    def __str__(self):
        return  f'Your new car is an {self.nombre}. Color {self.color}, doors {self.puertas}.\nIt reaches a maximum speed of {self.velocidad}km/h with their {self.cilindrada}L engine'


def main():

    chev_cavalier = Coche('Cavalier')
    newFile = open('ejercicio_8-2.bin', 'wb')
    pickle.dump(chev_cavalier, newFile)
    newFile.close()

    readFile()


if __name__ == '__main__':
    main()
