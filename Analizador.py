from Token import Token

class Analizador:
    #Guarda lo que llevo
    lexema = ''
    #Lista de token
    tokens = []
    #Estado en el que se encuentra
    estado = 1
    #Fila en la que se encuentra
    fila = 1
    #COlumna en la que se encuentra
    columna = 1
    #Bool para errores
    generar = False


    def __init__(self, entrada):
        self.lexema = ''
        self.tokens = []
        self.estado = 1
        self.fila = 1
        self.columna = 1
        self.generar = True
        tipos = Token("lexema",-1,-1,-1)

        entrada = entrada + '$'
        actual = ''
        longitud = len(entrada)
        
        i = 0
        while(i < longitud):
            actual = entrada[i]
            i += 1
            #Manejo inicial
            if self.estado == 1:
                if actual == '~':
                    self.estado = 1
                    self.columna += 1
                    self.lexema += actual
                    self.AddToken(tipos.VIRGULILLA)
                elif actual == '>':
                    self.estado = 1
                    self.columna += 1
                    self.lexema += actual
                    self.AddToken(tipos.RIGHT_ANGLE)
                elif actual == '<':
                    self.estado = 1
                    self.columna += 1
                    self.lexema += actual
                    self.AddToken(tipos.LEFT_ANGLE)
                elif actual == '[':
                    self.estado = 1
                    self.columna += 1
                    self.lexema += actual
                    self.AddToken(tipos.CORCHETE_IZQ)
                elif actual == ']':
                    self.estado = 1
                    self.columna += 1
                    self.lexema += actual
                    self.AddToken(tipos.CORCHETE_DER)
                elif actual == ',':
                    self.estado = 1
                    self.columna += 1
                    self.lexema += actual
                    self.AddToken(tipos.COMMMA)
                elif actual == ':':
                    self.estado = 1
                    self.columna += 1
                    self.lexema += actual
                    self.AddToken(tipos.COLON)
                elif actual.isalpha():
                    self.estado = 2
                    self.columna += 1
                    self.lexema += actual
                elif actual == '"':
                    self.estado = 3
                    self.columna += 1
                    self.lexema += actual
                elif actual == "'":
                    self.estado = 4
                    self.columna += 1
                    self.lexema += actual
                elif actual == ' ':
                    self.columna +=1
                    self.estado = 1
                elif actual == '\n':
                    self.fila += 1
                    self.estado = 1
                    self.columna = 1
                elif actual =='\r':
                    self.estado = 1
                elif actual == '\t':
                    self.columna += 5
                    self.estado = 1
                elif actual == '$' and i ==longitud - 1:
                    print('Analisis terminado')
                else:
                    self.lexema += actual
                    self.AddToken(tipos.UNKNOWN)
                    self.columna += 1
                    self.generar = False
            #Manejo de Letras 
            elif self.estado == 2:
                if actual.isalpha():
                    self.estado = 2
                    self.columna += 1
                    self.lexema += actual
                    continue
                else:
                    if self.Reservada():
                        self.AddToken(self.tipo)
                        i -= 1
                        continue
                    else:
                        self.AddToken(tipos.WORDS)
                        i -= 1
                        continue
            #Manejo de Cadenas
            elif self.estado == 3:
                if actual != '"':
                    self.estado = 3
                    self.columna +=1
                    self.lexema += actual
                elif actual == '"':
                    self.estado = 4
                    self.lexema += actual
                    self.AddToken(tipos.CHAIN)
            #Manejo de Cadenas
            elif self.estado == 4:
                if actual != "'":
                    self.estado = 4
                    self.columna +=1
                    self.lexema += actual
                elif actual == "'":
                    self.estado = 4
                    self.lexema += actual
                    self.AddToken(tipos.CHAIN)

    def AddToken(self,tipo):
        self.tokens.append(Token(self.lexema, tipo, self.fila, self.columna))
        self.lexema = ""
        self.estado = 1
    
    def Reservada(self):
        palabra = self.lexema.upper();
        #lista_palabras = ['NOMBRE', 'GRAFICA','TITULO','TITULOX','TITULOY']
        if palabra == 'TIPO':
            self.tipo = Token.TIPO  
            return True
        if palabra == 'VALOR':
            self.tipo = Token.VALOR 
            return True
        if palabra == 'FONDO':
            self.tipo = Token.FONDO
            return True
        if palabra == 'VALORES':
            self.tipo = Token.VALORES
            return True
        if palabra == 'NOMBRE':
            self.tipo = Token.NOMBRE
            return True
        if palabra == 'EVENTO':
            self.tipo = Token.EVENTO
            return True
        return False
    
    def Imprimir(self):
        print("-------------Tokens--------------")
        tipos = Token("lexema", -1, -1, -1)
        for x in self.tokens:
            if x.tipo != tipos.UNKNOWN:
                print(x.getLexema()," --> ",x.getTipo(),' --> ',x.getFila(), ' --> ',x.getColumna())
    
    def ImprimirErrores(self):
        print("-------------Errores--------------")
        tipos = Token("lexema", -1, -1, -1)
        for x in self.tokens:
            if x.tipo == tipos.UNKNOWN:
                print(x.getLexema()," --> ",x.getFila(), ' --> ',x.getColumna(),'--> Error Lexico')