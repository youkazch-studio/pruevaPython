print ("holaa")

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo de instancia
        self.modelo = modelo  # Atributo de instancia
        self.kilometraje = 0  # Atributo de instancia con un valor inicial

    def conducir(self, distancia):
        nuevo_kilometraje = self.kilometraje + distancia  # 'distancia' es una variable local
        self.kilometraje = nuevo_kilometraje  # 'self.kilometraje' es un atributo de instancia
        print(f"El coche ha recorrido {distancia} km. Kilometraje total: {self.kilometraje} km.")

mi_coche = Coche("Toyota", "Corolla")
mi_coche.conducir(1000)  # 'distancia' es local a este método
