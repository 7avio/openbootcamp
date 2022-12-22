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

cavallier = Coche('Chevrolet Cavallier')

dataDictionary =  {
    'name' : cavallier.nombre,
    'color' : cavallier.color,
    'maxSpeed' : cavallier.velocidad,
    'doors' : cavallier.puertas,
    'engine' : cavallier.cilindrada,
    'tyres' : cavallier.ruedas
}

response = 'Your new car is an {name}. Color {color}, doors {doors}.\nIt reaches a maximum speed of {maxSpeed}km/h with their {engine}L engine'.format(**dataDictionary)
print(response)
