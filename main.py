import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont
from tkinter import filedialog
from helpers import Lector_Archivos
from Analizador import Analizador
import webbrowser


def boton_cargaArchivo_command():
    texto = Lector_Archivos()
    text_area.insert(tk.INSERT,texto)
        

def boton_analizar_command():
    texto = text_area.get(1.0,'end')
    lexico = Analizador(texto)
    lexico.Imprimir()
    lexico.ImprimirErrores()
    lexico.GuardarDatos()
    lexico.generarFormulario1()
    


def boton_aceptarTexto_command():
    Tk().withdraw()
    filedir = filedialog.askopenfilename(filetypes=[("Archivo data","*.form")])
    #print(direccion)
    texto = text_area.get(1.0,'end')
    #print(texto)
    with open(filedir,"r+",encoding = "utf-8") as f:
        f.truncate(0)
        f.write(texto)

def boton_buscar_reporte():
    opcion = lista_reportes.get()
    if opcion == "Reporte de token":
        texto = text_area.get(1.0,'end')
        lexico = Analizador(texto)
        lexico.ReporteToken()
    elif opcion == "Reporte de errores":
        texto = text_area.get(1.0,'end')
        lexico = Analizador(texto)
        lexico.ReporteErrores()
    elif opcion == "Manual de Usuarios":
        webbrowser.open('Manual de Usuario.pdf') 
    elif opcion == "Manual Técnico":
        print("Manual Técnico")
    else:
        None

root = Tk()
root.title("Menú Principal")
ft = tkFont.Font(family='Tahoma',size=10)


content = ttk.Frame(root)
frame = ttk.Frame(content, width=600, height=450)

text_area=tk.Text(root)
text_area["font"] = ft
text_area.place(x=30,y=60,width=412,height=358)

label1=tk.Label(root)
label1["font"] = ft
label1["justify"] = "center"
label1["text"] = "Archivo ingresado"
label1.place(x=30,y=20,width=411,height=30)

boton_cargaArchivo=tk.Button(root)
boton_cargaArchivo["font"] = ft
boton_cargaArchivo["justify"] = "center"
boton_cargaArchivo["text"] = "Cargar"
boton_cargaArchivo.place(x=460,y=60,width=121,height=30)
boton_cargaArchivo["command"] = boton_cargaArchivo_command 

boton_analizar=tk.Button(root)
boton_analizar["font"] = ft
boton_analizar["justify"] = "center"
boton_analizar["text"] = "Analizar"
boton_analizar.place(x=460,y=110,width=121,height=30)
boton_analizar["command"] =boton_analizar_command

boton_aceptarTexto=tk.Button(root)
boton_aceptarTexto["font"] = ft
boton_aceptarTexto["justify"] = "center"
boton_aceptarTexto["text"] = "Guardar"
boton_aceptarTexto.place(x=460,y=160,width=120,height=30)
boton_aceptarTexto["command"] = boton_aceptarTexto_command 
        

boton_buscarReporte=tk.Button(root)
boton_buscarReporte["font"] = ft
boton_buscarReporte["justify"] = "center"
boton_buscarReporte["text"] = "Buscar Reporte"
boton_buscarReporte.place(x=460,y=280,width=120,height=30)
boton_buscarReporte["command"] = boton_buscar_reporte 
        
lista_reportes=ttk.Combobox(root)
lista_reportes["state"]="readonly"
lista_reportes["font"] = ft
lista_reportes["justify"] = "center"
lista_reportes["values"] = ["Reporte de token", "Reporte de errores", "Manual de Usuarios", "Manual Técnico"]
lista_reportes.place(x=460,y=240,width=120,height=31)

label2=tk.Label(root)
label2["font"] = ft
label2["justify"] = "center"
label2["text"] = "Seleccione una opción:"
label2.place(x=445,y=20,width=140,height=30)

label3=tk.Label(root)
label3["font"] = ft
label3["justify"] = "center"
label3["text"] = "Buscar Reportes"
label3.place(x=460,y=200,width=122,height=30)

label4=tk.Label(root)
label4["font"] = ft
label4["justify"] = "center"
label4["text"] = "findlesscopy-2022"
label4.place(x=460,y=400,width=113,height=30)



content.pack()
frame.pack()



root.mainloop()


