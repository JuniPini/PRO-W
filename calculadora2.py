from tkinter import *
from tkinter import ttk, messagebox


class Calculadora:


    def __init__(self):

        self.raiz = Tk()
        self.raiz.geometry('505x258')
        #self.raiz.configure(bg = 'beige')
        self.raiz.title('Calculadora')
        #self.raiz.resizable(0,0)


        style = ttk.Style(self.raiz)
        style.configure("borrar.TButton", foreground="red", background="white")


        frame_pantalla = Frame(self.raiz)
        frame_pantalla.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

        frame_fila789 = Frame(self.raiz)
        frame_fila789.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

        frame_fila456 = Frame(self.raiz)
        frame_fila456.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

        frame_fila123 = Frame(self.raiz)
        frame_fila123.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

        frame_fila0 = Frame(self.raiz)
        frame_fila0.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

        self.pantalla               = ttk.Entry(frame_pantalla, width=62, justify=RIGHT, style="")     
        

        self.boton1                 = ttk.Button(frame_fila123, text = '1', command = lambda : self.escribir_numero(1))
        self.boton2                 = ttk.Button(frame_fila123, text = '2', command = lambda : self.escribir_numero(2))
        self.boton3                 = ttk.Button(frame_fila123, text = '3', command = lambda : self.escribir_numero(3))
        self.boton_multiplicacion   = ttk.Button(frame_fila123, text = 'x', command = lambda : self.escribir_operacion('*'))
        
        self.boton4                 = ttk.Button(frame_fila456, text = '4', command = lambda : self.escribir_numero(4))
        self.boton5                 = ttk.Button(frame_fila456, text = '5', command = lambda : self.escribir_numero(5))
        self.boton6                 = ttk.Button(frame_fila456, text = '6', command = lambda : self.escribir_numero(6))
        self.boton_resta            = ttk.Button(frame_fila456, text = '-', command = lambda : self.escribir_operacion('-'))

        self.boton7                 = ttk.Button(frame_fila789, text = '7', command = lambda : self.escribir_numero(7))
        self.boton8                 = ttk.Button(frame_fila789, text = '8', command = lambda : self.escribir_numero(8))
        self.boton9                 = ttk.Button(frame_fila789, text = '9', command = lambda : self.escribir_numero(9))
        self.boton_suma             = ttk.Button(frame_fila789, text = '+', command = lambda : self.escribir_operacion('+'))

        
        self.boton0                 = ttk.Button(frame_fila0, text = '0', width=30, command = lambda : self.escribir_numero(0))      
        self.boton_division         = ttk.Button(frame_fila0, text = '÷', command = lambda : self.escribir_operacion('/'))
        self.boton_borrar           = ttk.Button(frame_fila0, text = 'Borrar', command = self.borrar, style="borrar.TButton")
        self.boton_calcular         = ttk.Button(frame_fila0, text = '=', width=20, command = self.resultado)
        

        self.pantalla.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5, ipadx=50)