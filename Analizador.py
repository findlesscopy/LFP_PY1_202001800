from asyncore import write
from time import process_time_ns
from traceback import print_tb
from Token import Token
from tkinter import messagebox
import webbrowser
from Elemento import Elemento

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

    elementos = []

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
                    self.AddToken(tipos.SIMPLE_CHAIN)

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
    
    def ReporteToken(self):
        
        messagebox.showinfo(message="Se ha genera el reporte de token", title="Reporte")
        f = open('Reporte Token.html','w')
        f.write("<!doctype html>")
        f.write("<html lang=\"en\">")
        f.write("<head>")
        
        f.write(" <meta charset=\"utf-8\">")
        f.write("<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">")
        f.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
        f.write("<title>Reporte del Tokens</title>")
        f.write("<style>"
            "body {background-color: #F5EFB1;font-family: \"Lucida Console\", \"Courier New\", monospace;}"
            "h1 {background-color: #87DABF;}"
            "table, th, td {border: 1px solid black; text-align: center}""</style>")
        f.write("</head>")
        f.write("<body>")
        f.write("<H1><center>REPORTE DE TOKENS</center></H1>")
        f.write("<center><table><tr><th>No. </th><th>Símbolo</th><th>Tipo</th><th>Fila</th><th>Columna</th>")
        tipos = Token("lexema", -1, -1, -1)
        i=0
        for x in self.tokens:
            i+=1
            if x.tipo != tipos.UNKNOWN:
                f.write("<tr>")
                f.write("<center><td><h4>" + str(i) + "</td></h4>"+"<td><h4>" + str(x.getLexema() ) +"</td></h4>"+"<td><h4>" + str(x.getTipo() ) +"</td></h4>"+ "<td><h4>" + str(x.getFila()) +"</td></h4>"+ "<td><h4>" + str(x.getColumna()) +"</td></h4>"+"</center>")
                f.write("</tr>")
        f.write("</table></center>")
        f.write("</body>")
        f.write("</html>")
        f.close()
        webbrowser.open('Reporte Token.html') 

    def ReporteErrores(self):
        messagebox.showinfo(message="Se ha genera el reporte de errores", title="Reporte")
        f = open('Reporte Errores.html','w')
        f.write("<!doctype html>")
        f.write("<html lang=\"en\">")
        f.write("<head>")
        
        f.write(" <meta charset=\"utf-8\">")
        f.write("<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">")
        f.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
        f.write("<title>Reporte del Tokens</title>")
        f.write("<style>"
            "body {background-color: #F5EFB1;font-family: \"Lucida Console\", \"Courier New\", monospace;}"
            "h1 {background-color: #87DABF;}"
            "table, th, td {border: 1px solid black; text-align: center}""</style>")
        f.write("</head>")
        f.write("<body>")
        f.write("<H1><center>REPORTE DE TOKENS</center></H1>")
        #TABLA DE PRODUCTOS ASCENDENTE
        f.write("<center><table><tr><th>No. </th><th>Símbolo</th><th>Tipo</th><th>Fila</th><th>Columna</th>")
        tipos = Token("lexema", -1, -1, -1)
        i=0
        for x in self.tokens:
            i+=1
            if x.tipo == tipos.UNKNOWN:
                f.write("<tr>")
                f.write("<center><td><h4>" + str(i) + "</td></h4>"+"<td><h4>" + str(x.getLexema() ) +"</td></h4>"+"<td><h4>" + str(x.getTipo() ) +"</td></h4>"+ "<td><h4>" + str(x.getFila()) +"</td></h4>"+ "<td><h4>" + str(x.getColumna()) +"</td></h4>"+"</center>")
                f.write("</tr>")
        f.write("</table></center>")
        f.write("</body>")
        f.write("</html>")
        f.close()
        webbrowser.open('Reporte Errores.html') 

    def GuardarDatos(self):
        tipos = Token("lexema", -1, -1, -1)
        longitud = len(self.tokens)
        for i in range(longitud):
            if self.tokens[i].tipo == tipos.TIPO:
                tipo = self.tokens[i+2].lexema
                tipo = str(tipo).replace('"',"")
                if tipo == "etiqueta":
                    valor = None
                    if self.tokens[i+4].tipo == tipos.VALOR:
                        valor = self.tokens[i+6].lexema
                        valor = str(valor).replace('"',"")
                    self.elementos.append(Elemento(tipo,valor,None,None,None,None))   
                if tipo == "texto":
                    valor = None
                    fondo = None
                    if self.tokens[i+4].tipo == tipos.VALOR:
                        valor = self.tokens[i+6].lexema
                        valor = str(valor).replace('"',"")
                    if self.tokens[i+4].tipo == tipos.FONDO:
                        fondo = self.tokens[i+6].lexema
                        fondo = str(fondo).replace('"',"")
                    if self.tokens[i+8].tipo == tipos.VALOR:
                        valor = self.tokens[i+10].lexema
                        valor = str(valor).replace('"',"")
                    if self.tokens[i+8].tipo == tipos.FONDO:
                        fondo = self.tokens[i+10].lexema
                        fondo = str(fondo).replace('"',"")
                    self.elementos.append(Elemento(tipo,valor,fondo,None,None,None))
                if tipo == "grupo-radio":
                    nombre = None
                    valores = []
                    if self.tokens[i+4].tipo == tipos.NOMBRE:
                        nombre = self.tokens[i+6].lexema
                        nombre = str(nombre).replace('"',"")
                    if self.tokens[i+8].tipo == tipos.VALORES:
                        if self.tokens[i+11].tipo == tipos.SIMPLE_CHAIN:
                            opcion = self.tokens[i+11].lexema
                            opcion = str(opcion).replace("'","")
                            valores.append(opcion)
                        if self.tokens[i+13].tipo == tipos.SIMPLE_CHAIN:
                            opcion = self.tokens[i+13].lexema
                            opcion = str(opcion).replace("'","")
                            valores.append(opcion)
                        if self.tokens[i+15].tipo == tipos.SIMPLE_CHAIN:
                            opcion = self.tokens[i+15].lexema
                            opcion = str(opcion).replace("'","")
                            valores.append(opcion)
                        if self.tokens[i+17].tipo == tipos.SIMPLE_CHAIN:
                            opcion = self.tokens[i+17].lexema
                            opcion = str(opcion).replace("'","")
                            valores.append(opcion)
                        if self.tokens[i+19].tipo == tipos.SIMPLE_CHAIN:
                            opcion = self.tokens[i+19].lexema
                            opcion = str(opcion).replace("'","")
                            valores.append(opcion)
                    self.elementos.append(Elemento(tipo,None,None,valores,None,nombre))
                if tipo == "grupo-option":
                    nombre = None
                    valores = []
                    if self.tokens[i+4].tipo == tipos.NOMBRE:
                        nombre = self.tokens[i+6].lexema
                        nombre = str(nombre).replace('"',"")
                    if self.tokens[i+8].tipo == tipos.VALORES:
                        if self.tokens[i+11].tipo == tipos.SIMPLE_CHAIN:
                            opcion = self.tokens[i+11].lexema
                            opcion = str(opcion).replace("'","")
                            valores.append(opcion)
                        if self.tokens[i+13].tipo == tipos.SIMPLE_CHAIN:
                            opcion = self.tokens[i+13].lexema
                            opcion = str(opcion).replace("'","")
                            valores.append(opcion)
                        if self.tokens[i+15].tipo == tipos.SIMPLE_CHAIN:
                            opcion = self.tokens[i+15].lexema
                            opcion = str(opcion).replace("'","")
                            valores.append(opcion)
                        if self.tokens[i+17].tipo == tipos.SIMPLE_CHAIN:
                            opcion = self.tokens[i+17].lexema
                            opcion = str(opcion).replace("'","")
                            valores.append(opcion)
                        if self.tokens[i+19].tipo == tipos.SIMPLE_CHAIN:
                            opcion = self.tokens[i+19].lexema
                            opcion = str(opcion).replace("'","")
                            valores.append(opcion)
                    self.elementos.append(Elemento(tipo,None,None,valores,None,nombre))
                if tipo == "boton":
                    valor = None
                    evento = None
                    if self.tokens[i+4].tipo == tipos.VALOR:
                        valor = self.tokens[i+6].lexema
                        valor = str(valor).replace('"',"")
                    if self.tokens[i+4].tipo == tipos.EVENTO:
                        evento = self.tokens[i+6].lexema
                        evento = str(evento).replace('"',"")
                    if self.tokens[i+8].tipo == tipos.VALOR:
                        valor = self.tokens[i+10].lexema
                        valor = str(valor).replace('"',"")
                    if self.tokens[i+8].tipo == tipos.EVENTO:
                        evento = self.tokens[i+10].lexema
                        evento = str(evento).replace('"',"")
                    self.elementos.append(Elemento(tipo,valor,None,None,evento,None))
            
                #self.elementos.append(Elemento(tipo,"None","None","None","None","None"))
        #print(repr(self.elementos))

    def generarFormulario(self):
        messagebox.showinfo(message="Se ha genera el Formulario", title="Formularios.io")
        f = open('Formulario.html','w')
        f.write("<!doctype html>")
        f.write("<html lang=\"en\">")
        f.write("<head>")
        
        f.write(" <meta charset=\"utf-8\">")
        f.write("<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">")
        f.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
        f.write("<title>Formulario</title>")
        f.write("<style>"
            "body {background-color: #F5EFB1;font-family: \"Lucida Console\", \"Courier New\", monospace;}"
            "h1 {background-color: #87DABF;}"
            "table, th, td {border: 1px solid black; text-align: center}"
            "form { margin: 0 auto; width: 400px;padding: 1em;border: 1px solid #CCC; border-radius: 1em;}"
            "ul {list-style: none;padding: 0;margin: 0;}"
            "form li + li {margin-top: 1em;}"
            "label {display: inline-block;width: 90px;text-align: right;}"
            "input{font: 1em sans-serif;width: 300px;box-sizing: border-box;border: 1px solid #999;}"
            "input:focus,textarea:focus {border-color: #000;}"
            ".button {padding-left: 90px; }"
            "button {margin-left: .5em;}"
            
            "</style>")
        f.write("</head>")
        f.write("<body>")
        f.write("<H1><center>Formulario</center></H1>")
        f.write("<form><ul>")
        tipos = Token("lexema", -1, -1, -1)
        for i in self.tokens:
            if i.tipo == tipos.LEFT_ANGLE:
                print("Empieza un nuevo elemento")
            if i.tipo == tipos.CHAIN:
                if i.lexema == '"etiqueta"':
                    f.write("<li>")
                    f.write("<label>Hola</label>")
                    f.write("</li>")
                    #print("etiqueta")
                if i.lexema == '"texto"':
                    f.write("<li>")
                    f.write("<input type='text' name='Name' />")
                    f.write("</li>")
                    #print("texto")  
                if i.lexema == '"grupo-radio"':
                    f.write("<li>")
                    f.write("<input type='radio' name='Name' />")
                    f.write("</li>")
                    #print("grupo-radio")
                if i.lexema == '"grupo-option"':
                    f.write("<li>")
                    f.write("<select name='cars' id='cars'></select>")
                    f.write("</li>")
                    #print("grupo-option")
                if i.lexema == '"boton"':
                    f.write("<li>")
                    f.write("<button type='button'>Click Me!</button>")
                    f.write("</li>")
                    #print("boton")
            if i.tipo == tipos.RIGHT_ANGLE:
                print("Termina elemento")
        f.write("</ul></form>")
        f.write("</body>")
        f.write("</html>")
        f.close()
        webbrowser.open('Formulario.html') 
            

    def generarFormulario1(self):
        messagebox.showinfo(message="Se ha genera el Formulario", title="Formularios.io")
        f = open('Formulario.html','w')
        f.write("<!doctype html>")
        f.write("<html lang=\"en\">")
        f.write("<head>")
            
        f.write(" <meta charset=\"utf-8\">")
        f.write("<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">")
        f.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
        f.write("<title>Formulario</title>")
        f.write("<style>"
            "body {background-color: #F5EFB1;font-family: \"Lucida Console\", \"Courier New\", monospace;}"
            "h1 {background-color: #87DABF;}"
            "table, th, td {border: 1px solid black; text-align: center}"
            "form { margin: 0 auto; width: 400px;padding: 1em;border: 1px solid #CCC; border-radius: 1em;}"
            "ul {list-style: none;padding: 0;margin: 0;}"
            "form li + li {margin-top: 1em;}"
            "label {display: inline-block;width: 90px;text-align: right;}"
            #"input{font: 1em sans-serif;width: 300px;box-sizing: border-box;border: 1px solid #999;}"
            "input:focus,textarea:focus {border-color: #000;}"
            ".button {padding-left: 90px; }"
            "button {margin-left: .5em;}"
                
            "</style>")
        f.write("</head>")
        f.write("<body>")
        f.write("<H1><center>Formulario</center></H1>")
        f.write("<form><ul>")
        longitud = len(self.elementos)
        for i in range(longitud):
            #print(self.elementos[i].tipo)
        
            if self.elementos[i].tipo == "etiqueta":
                f.write("<li>")
                f.write("<label>"+ self.elementos[i].valor +"</label>")
                f.write("</li>")
            if self.elementos[i].tipo == "texto":
                f.write("<li>")
                if self.elementos[i].valor !=None:
                    f.write("<label>"+ self.elementos[i].valor +"</label>")
                else:
                    None
                f.write("<input type='text' name='Name' placeholder = "+ self.elementos[i].fondo +" />")
                f.write("</li>")
            if self.elementos[i].tipo == "grupo-radio":
                f.write("<li>")
                if self.elementos[i].nombre !=None:
                    f.write("<label>"+ self.elementos[i].nombre +"</label>")
                else:
                    None
                opcion = self.elementos[i].valores
                #print(opcion)
                for x in opcion:
                    f.write("<input type='radio'>"+ x +"")
                f.write("</li>")
            if self.elementos[i].tipo == "grupo-option":
                f.write("<li>")
                if self.elementos[i].nombre !=None:
                    f.write("<label>"+ self.elementos[i].nombre +"</label>")
                else:
                    None
                opcion = self.elementos[i].valores
                print(opcion)
                f.write("<select >")
                for x in opcion:
                    f.write("<option>"+x+"</option>")
                f.write("</select>")
                f.write("</li>")
            if self.elementos[i].tipo == "boton":
                f.write("<li>")
                f.write("<button>"+ self.elementos[i].valor +"</button>")
                f.write("</li>")
        f.write("</ul></form>")
        f.write("</body>")
        f.write("</html>")
        f.close()
        webbrowser.open('Formulario.html') 
            