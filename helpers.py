from io import open
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from io import open

def Lector_Archivos():
    Tk().withdraw()
    filedir = filedialog.askopenfilename(filetypes=[("Archivo data","*.form")])
    #print(filedir)
    archivos_texto = open(filedir,"r+",encoding = "utf-8")
    texto = archivos_texto.read()
    return texto