class Token():
    lexema = ''
    tipo = 0
    fila = 0
    columna = 0

    #ENUM
    VIRGULILLA = 1
    RIGHT_ANGLE = 2
    LEFT_ANGLE = 3
    CORCHETE_IZQ = 4
    CORCHETE_DER = 5
    COLON = 6
    COMMMA = 7
    CHAIN = 8
    SIMPLE_CHAIN = 9
    TIPO = 10
    VALOR = 11
    FONDO = 12
    VALORES = 13
    EVENTO = 14
    WORDS = 15
    UNKNOWN = 16
    NOMBRE = 17

    #Constructor de la clase
    def __init__(self,lexema,tipo,fila,columna):
        self.lexema = lexema
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def getLexema(self):
        return self.lexema

    def getFila(self):
        return self.fila
    
    def getColumna(self):
        return self.columna

    def getTipo(self):
        if self.tipo == self.VIRGULILLA:
            return 'VIRGULILLA'
        elif self.tipo == self.RIGHT_ANGLE:
            return 'RIGHT_ANGLE'
        elif self.tipo == self.LEFT_ANGLE:
            return 'LEFT_ANGLE'
        elif self.tipo == self.CORCHETE_IZQ:
            return 'CORCHETE_IZQ'
        elif self.tipo == self.CORCHETE_DER:
            return 'CORCHETE_DER'
        elif self.tipo == self.COLON:
            return 'COLON'
        elif self.tipo == self.COMMMA:
            return "COMMMA"
        elif self.tipo == self.CHAIN:
            return "CHAIN"
        elif self.tipo == self.SIMPLE_CHAIN:
            return "SIMPLE_CHAIN"
        elif self.tipo == self.TIPO:
            return "TIPO"
        elif self.tipo == self.VALOR:
            return "VALOR"
        elif self.tipo == self.FONDO:
            return "FONDO"
        elif self.tipo == self.VALORES:
            return "VALORES"
        elif self.tipo == self.EVENTO:
            return "EVENTO"
        elif self.tipo == self.WORDS:
            return "WORDS"
        elif self.tipo == self.UNKNOWN:
            return "UNKNOWN"
        elif self.tipo == self.NOMBRE:
            return "NOMBRE"