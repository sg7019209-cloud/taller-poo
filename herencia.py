class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento

    def describir(self):
        return f"Vehiculo {self.marca} a {self.velocidad} km/h"


class Carro(Vehiculo):
    def __init__(self, marca, puertas):
        super().__init__(marca)          # llama al constructor de Vehiculo
        self.puertas = puertas

    def describir(self):                 # sobrescribe el metodo del padre
        return f"Carro {self.marca} de {self.puertas} puertas a {self.velocidad} km/h"

    def tocar_bocina(self):
        print("Pii pii!")


class Moto(Vehiculo):
    def __init__(self, marca, cilindraje):
        super().__init__(marca)
        self.cilindraje = cilindraje

    def describir(self):
        return f"Moto {self.marca} de {self.cilindraje}cc a {self.velocidad} km/h"

    def hacer_caballito(self):
        print("Haciendo un caballito...")


if __name__ == "__main__":
    carro = Carro("Mazda", 4)
    moto = Moto("Yamaha", 150)

    carro.acelerar(60)       # metodo heredado de Vehiculo
    moto.acelerar(80)

    print(carro.describir())
    print(moto.describir())
    carro.tocar_bocina()
    moto.hacer_caballito()