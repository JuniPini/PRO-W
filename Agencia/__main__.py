import ast
import json
from avion import Avion
from aeropuerto import Aeropuerto
from viaje import Viaje
from billete import Billete

from functools import partial
from tkinter import filedialog as fd

# !/usr/bin/env python
# -*- coding: utf-8 -*-

# name: main.py  (Python 3.x).
# description: Gestión de una agencia de viajes
# purpose: Gestión de una agencia de viajes
# author: juanra

# --------------------------------------------------

'''AgenciaDeViajes: Gestión de una agencia de viajes'''

__title__ = 'Agencia de Viajes'
__date__ = ''
__version__ = '0.0.1'
__license__ = 'GNU GPLv3'

import os
from tkinter import *
from tkinter import ttk, font, messagebox

class AgenciaDeViajes():
    '''Clase AgenciaDeViajes'''
    # DECLARAR MÉTODO CONSTRUCTOR DE LA APLICACIÓN
    ruta_guardado = os.path.dirname(__file__) + os.sep + 'bbdd' + os.sep + 'viajes.json'
    posx_y = 50
    def __init__(self, iconos):
        
        self.iconos = iconos

        self.raiz = Tk()

        self.raiz.title("Agencia de Viajes: El corte Francés")

        self.icono1 = PhotoImage(file=self.iconos[0])
        self.raiz.iconphoto(self.raiz, self.icono1)

        self.raiz.option_add("Font", "Helvetica 12")
        self.raiz.option_add('*tearOff', False)

        self.raiz.minsize(400, 300)

        self.fuente = font.Font(weight='normal')

        self.nombre    = StringVar(value="")
        self.apellidos = StringVar(value="")
        self.viaje     = StringVar(value="")
        self.filtro    = StringVar(value="")


        self.viajes = self.leer_viajes()


        barramenu = Menu(self.raiz)
        self.raiz['menu'] = barramenu

        icono2 = PhotoImage(file=self.iconos[1])
        icono3 = PhotoImage(file=self.iconos[2])
        icono4 = PhotoImage(file=self.iconos[3])

        barramenu.add_command(
            label       = 'ALta',
            command     = self.alta_billete,
            underline   = 0,
            accelerator = "Ctrl+a",
            image       = icono2,
            compound    = LEFT
        )


        barramenu.add_command(
            label       = 'Listado',
            command     = self.listado_viajes,
            underline   = 0,
            accelerator = "Ctrl+l",
            image       = icono3,
            compound    = LEFT
        )

        barramenu.add_command(
            label       = 'Carga',
            command     = self.carga_externa,
            underline   = 0,
            accelerator = "Ctrl+c",
            image       = icono4,
            compound    = LEFT
        )

        self.frame = Frame(self.raiz)

        self.frame.config(bg='lightblue')

        self.frame.config(width=400,height=300)
        self.frame.pack(side=TOP)


        self.raiz.bind("<Control-a>", lambda : self.alta_billete())
        self.raiz.bind("<Control-l>", lambda : self.listado_viajes())
        self.raiz.bind("<Control-c>", lambda : self.carga_externa())

        self.raiz.mainloop()

    def alta_billete(self):
        self.destruir_frames()

        etiqueta_viajes    = ttk.Label(self.frame, text="Viajes:"    ,justify="left",width=40,padding=[10])
        etiqueta_nombre    = ttk.Label(self.frame, text="Nombre:"    ,justify="left",width=40,padding=[10])
        etiqueta_apellidos = ttk.Label(self.frame, text="Apellidos:" ,justify="left",width=40,padding=[10])

        opciones = self.viajes.keys()

        select_viajes =  OptionMenu(self.frame, self.viaje,*opciones)
        nombre        = ttk.Entry(self.frame, justify="left", textvariable=self.nombre)
        apellidos     = ttk.Entry(self.frame, justify="left", textvariable=self.apellidos)

        guardar = ttk.Button(self.frame, text="Guardar", command=self.guardar_billete)


        etiqueta_viajes.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)
        select_viajes.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

        etiqueta_nombre.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)
        nombre.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)

        etiqueta_apellidos.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)
        apellidos.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)

        guardar.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

    def guardar_billete(self):
        errores = False

        texto_errores = ''

        nuevo_billete = Billete()

        try:
            nuevo_billete.viaje = self.viaje.get()

        except:
            errores = True
            texto_errores += "No se ha seleccionado ningún viaje\n"
        else:
            viaje_seleccionado = self.viajes.get(nuevo_billete.viaje)

        try:
            nuevo_billete.nombre = self.nombre.get()
        except:
            errores = True
            texto_errores += "No se ha insertado ningún nombre\n"

        try:
            nuevo_billete.apellidos = self.apellidos.get()
        except:
            errores = True
            texto_errores += "No se ha insertado ningún apellido\n"
        
        try:
            viaje_seleccionado.billetes_comprados = nuevo_billete
        except:
            errores = True
            texto_errores += "Hay algún problema con la capacidad del avión"

        if errores:
            messagebox.showinfo('Hay errores en el formulario', texto_errores)
        else:
            self.guardar_fichero()

    def guardar_fichero(self):
        f = open(self.ruta_guardado, 'w')

        dict_viajes = {}

        for viaje in self.viajes:
            dict_viajes.update(self.viajes[viaje].diccionario())

        f.write(json.dumps(dict_viajes, indent=4))

    def leer_viajes(self, ruta = ruta_guardado):
        f = open(ruta)

        texto = f.read()

        dict_viajes = ast.literal_eval(texto)

        viajes = {}

        for key in dict_viajes:
            viaje = Viaje(Aeropuerto(dict_viajes[key]['origen']),Aeropuerto(dict_viajes[key]['destino']), Avion(dict_viajes[key]['avion']))

            for nbillete in dict_viajes[key]['billetes_comprados']:
                nbillete = dict_viajes[key]['billetes_comprados'][nbillete]

                carga_billete = Billete()
                carga_billete.nombre    = nbillete.get('nombre')
                carga_billete.apellidos = nbillete.get('apellidos')
                carga_billete.viaje     = nbillete.get('viaje')

                viajes[key] = viaje

        return viajes


    def listado_viajes(self):
        self.destruir_frames()
        etiqueta_listado    = ttk.Label(self.frame, text="Filtro:"   ,justify="left",width=40,padding=[10])

        filtro  = ttk.Entry(self.frame, justify="left",textvariable=self.filtro)
        filtrar = ttk.Button(self.frame, text="Filtrar", command=self.filtrar)


        etiqueta_listado.pack   (side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        filtro.pack             (side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        filtrar.pack            (side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

        self.frame_viajes = Frame(self.frame)

        self.frame_viajes.pack(side=TOP)

        self.info_filtrar()

    def info_billetes(self,viaje):

        dialogo = Toplevel()

        AgenciaDeViajes.posx_y += 50 
        tamypos = '400x300+'+str(AgenciaDeViajes.posx_y)+ '+'+ str(AgenciaDeViajes.posx_y)
        
        #dialogo.geometry(tamypos)

        self.treeview = ttk.Treeview(dialogo, columns=('nombre', 'apellidos'))

        self.treeview.heading("#0"          ,text="Viaje")
        self.treeview.heading("nombre"      ,text="Nombre")
        self.treeview.heading("apellidos"   ,text="Apellidos")

        for billete in viaje.billetes_comprados:
            self.treeview.insert(
                "",
                END,
                text=billete.viaje,
                values=(billete.nombre, billete.apellidos)
            )   
        
        self.treeview.bind("<<TreeviewSelect>>", self.item_selected)

        self.treeview.pack()

        dialogo.mainloop() 

    def item_selected(self, event):
        item_selected = self.treeview.selection([0])
        print(self.treeview.item(item_selected))

    def info_filtrar(self, texto_filtrado=''):
        billetes = {}

        for key_viajes in self.viajes:

            contenido_viajes = str(self.viajes[key_viajes])

            if texto_filtrado == '' or texto_filtrado in contenido_viajes.lower():

                texto_listado_viajes = str(self.viajes[key_viajes])

                labelframe = LabelFrame(self.frame_viajes, text=key_viajes)
                texto_listado = Label(labelframe, text=texto_listado_viajes, anchor='w', justify="left")

                billetes = ttk.Button(labelframe, text="Info Billetes", command=partial(self.info_billetes, self.viajes[key_viajes]))
                
                labelframe.pack        (side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
                texto_listado.pack(side=LEFT,fill=BOTH, expand=True, padx=5, pady=5)
                billetes.pack(side=LEFT,fill=BOTH, expand=True, padx=5, pady=5)

    def filtrar(self):
        self.destruir_frame_viajes()

        self.info_filtrar(self.filtro.get().lower())

    def carga_externa(self):
        self.destruir_frames()
        etiqueta_carga   = ttk.Label(self.frame, text="Carga Externa:"  ,justify="left",width=40,padding=[10])
        etiqueta_carga.pack(side=TOP)

        ruta_archivo = fd.askopenfilename(initialdir='/', title = "Selecione Archivo",filetypes = (("txt files", "*.txt"),("todos los archivos","*.*")))

        nuevos_viajes = self.leer_viajes(ruta_archivo)

        self.viajes.update(nuevos_viajes)

    def destruir_frame_viajes(self):
        for widget in self.frame_viajes.winfo_children():
            widget.destroy()

    def destruir_frames(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

def f_verificar_iconos(iconos):
    ''' Verifica existencia de iconos
    iconos -- Lista de iconos '''
    for icono in iconos:
        if not os.path.exists(icono):
            print('Icono no encontrado:', icono)
            return(1)
        
    return(0)

def main():

    IMG_DIR = os.path.dirname(__file__) + os.sep + 'imagen' + os.sep

    iconos = (
        IMG_DIR + "plane_icon.png",
        IMG_DIR + "alta.png",
        IMG_DIR + "listado.png",
        IMG_DIR + "carga.png"
    )

    error1 = f_verificar_iconos(iconos)
    if not error1:
        mi_app = AgenciaDeViajes(iconos)

    return(0)

if __name__ == '__main__':
    main()