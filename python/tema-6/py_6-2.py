
class Alumno:
    def __init__(self):
        self._nombre = None
        self._nota = None

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_nota(self, nota):
        self._nota = nota

juanito = Alumno()
juanito.set_nombre('Juanito')
juanito.set_nota(9.7)

print(juanito._nombre)
