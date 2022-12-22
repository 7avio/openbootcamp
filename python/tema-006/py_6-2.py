
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
juanito.set_nota('A')

response = 'Alumni {name} reach {grade} as their final grade'.format(name = juanito._nombre, grade = juanito._nota)
print(response)