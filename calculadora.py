from tkinter import *
from tkinter import ttk


class Calculadora():
    def __init__(self):
        
        self.raiz= Tk()
        self.raiz.geometry('300x300')
        self.raiz.configure(bg = 'white')
        self.raiz.title('Calculadora')
        
        
        self.boton1 = ttk.Button(self.raiz, text='9', command='9').pack(side=LEFT)
        self.boton2 = ttk.Button(self.raiz, text='8', command='8').pack(side=LEFT)
        self.boton3 = ttk.Button(self.raiz, text='7', command='7').pack(side=LEFT)
        self.boton4 = ttk.Button(self.raiz, text='+', command='+').pack(side=LEFT)
        self.boton5= ttk.Button(self.raiz, text='6', command='6').pack(side=LEFT)
        self.boton6 = ttk.Button(self.raiz, text='5', command='5').pack(side=LEFT)
        self.boton7 = ttk.Button(self.raiz, text='4', command='4').pack(side=LEFT)
        self.boton8 = ttk.Button(self.raiz, text='-', command='-').pack(side=LEFT)
        self.boton9 = ttk.Button(self.raiz, text='3', command='3').pack(side=LEFT)
        self.boton10 = ttk.Button(self.raiz, text='2', command='2').pack(side=LEFT)
        self.boton11 = ttk.Button(self.raiz, text='1', command='1').pack(side=LEFT)
        self.boton12 = ttk.Button(self.raiz, text='*', command='*').pack(side=LEFT)
        self.boton13 = ttk.Button(self.raiz, text='0', command='0').pack(side=LEFT)
        self.boton14 = ttk.Button (self.raiz, text='Calcular', command = self.raiz.destroy).pack(side = BOTTOM)
        self.boton15 = ttk.Button(self.raiz, text='/', command='/').pack(side=LEFT)



        self.raiz.mainloop()




def main():
    mi_app = Calculadora()
    return 0


if __name__ == '__main__':
    main()