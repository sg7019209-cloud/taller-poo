from abc import ABC, abstractmethod


class Pago(ABC):
    @abstractmethod
    def pagar(self, monto):
        pass


class TarjetaCredito(Pago):
    def __init__(self, numero):
        self.numero = numero

    def pagar(self, monto):
        print(f"Pagando ${monto} con tarjeta terminada en {self.numero[-4:]}")


class PayPal(Pago):
    def __init__(self, correo):
        self.correo = correo

    def pagar(self, monto):
        print(f"Pagando ${monto} con PayPal ({self.correo})")



metodos = [
    TarjetaCredito("1234567812345678"),
    PayPal("ana@correo.com"),
]


for p in metodos:
    p.pagar(50000.0)