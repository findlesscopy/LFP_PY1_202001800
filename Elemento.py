class Elemento:

    def __init__(self,tipo, valor, fondo, valores, evento, nombre):
        self.tipo = tipo
        self.valor = valor
        self.fondo = fondo
        self.valores = valores
        self.evento = evento
        self.nombre = nombre


    def __repr__(self):
        return f'\n Tipo {self.tipo} Valor {self.valor} Fondo {self.fondo} Valores {self.valores} Evento {self.evento} Nombre {self.nombre}'
