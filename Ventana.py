# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:13:25 2024

Interfaz gráfica para visualizar los términos de fibonacci.

@author: Angel de Hoyos Sainz
"""
import tkinter as tk 
from tkinter import ttk
from PIL import Image, ImageTk
from Fibonacci import fibonacciTopDown,fibonacciBottomUp
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt 
import numpy as np

class VentanaFib(tk.Frame):
    
    def __init__(self, master, *args):
        """
        Constructor que crea una ventana interactiva para calcular
        y visualizar los términos de la serie de Fibonacci mediante 
        las estrategias de programación dináminca TopDown y BottomUp.

        Parameters
        ----------
        master : tk.Tk
            ventana raíz.
        """
        # herencia
        super().__init__(master, *args)
        # atributos
    
        # colocar en el centro de la pantalla
        raiz_width = 500
        raiz_height = 450
        cent_x = int((self.master.winfo_screenwidth() - raiz_width)/2) 
        cent_y = int((self.master.winfo_screenheight() - raiz_height)/2)
        self.master.geometry(f"{raiz_width}x{raiz_height}+{cent_x}+{cent_y}")
        
        # disposición de la ventana
        self.master.columnconfigure(0, weight = 1, uniform="c1")
        self.master.columnconfigure(1, weight = 1, uniform="c1")
        
        self.master.rowconfigure(0, weight = 20, uniform="r1")
        self.master.rowconfigure(1, weight = 9, uniform="r1")
        self.master.rowconfigure(2, weight = 9, uniform="r1")
        self.master.rowconfigure(3, weight = 9, uniform="r1")
        self.master.rowconfigure(4, weight = 50, uniform="r1")
        self.master.rowconfigure(5, weight = 8, uniform="r1")
        self.master.rowconfigure(6, weight = 8, uniform="r1")
        self.master.rowconfigure(7, weight = 1, uniform="r1")
        
        # Se crean los widgets y se grafica la espiral de fibonacci
        self.widgets()
        self.espiral()
        
    
    
    def widgets(self):
        """
        Crea los widgets de la ventana y establece sus funcionalidades.

        Returns
        -------
        None.

        """
        # PORTADA
        # imagen
        img = Image.open("portada.jpg")
        rz_img_port = img.resize((500, 80))
        self.img_port = ImageTk.PhotoImage(rz_img_port)
        
        # lienzo
        canvas = tk.Canvas(self.master)
        canvas.create_image(0, 0, image = self.img_port, anchor='nw')
        canvas.create_text(100,35,text="FIBONACCI", font=("Times New Roman",20),
                           fill='white')
        canvas.grid(row=0, column=0, columnspan=2, sticky='nsew')# se coloca el lienzo
        
        # NÚMERO DEL TÉRMINO DE LA SUCESIÓN
        lb_n = tk.Label(self.master,text="Termino de la sucesión a calcular:",
                        font=('Calibri',12),background='SteelBlue3')
        lb_n.grid(row=1, column=0, padx=5, sticky='se')
        
        n = tk.Entry(self.master,width= 6)
        n.grid(row=1, column=1, padx=10, sticky='sw')
        
        
        lb_n1 = tk.Label(self.master,text="Estrategia de programación:",
                         font=('Calibri',12),background='SteelBlue3')
        lb_n1.grid(row=2, column=0, padx=21, sticky='w')
        
        estrategia = ttk.Combobox(self.master,values=['TopDown','BottomUp'],
                                  state="readonly",width=10)
        estrategia.set("BottomUp")
        estrategia.grid(row=2, column=1,columnspan=2,padx=10, sticky='w')
        
        lb_Fn = tk.Label(self.master,text="Fn =",
                         font=('Calibri',12),background='SteelBlue3')
        lb_Fn.grid(row=3, column=0,padx =23, sticky='w')
        
        self.entry_Fn = tk.Entry(self.master,width= 6,state='disabled')
        self.entry_Fn.grid(row=3, column = 0,columnspan=2,padx= 60, sticky='w')
        
        bt_apply = tk.Button(self.master, text='Aplicar',width=10,
                             command= lambda: self.aplicarPD(n.get(),
                                                            estrategia.get()))
        bt_apply.grid(row=6, column = 0,columnspan=2,sticky='s')
        
        # GRÁFICO   
        # formato y estilo
        plt.style.use('ggplot')
        
        # figura
        fig = Figure(figsize = (5, 5), 
                 dpi = 97)
        # se crean los ejes del gráfico
        left = 0
        bottom = 0 
        width = 1
        height = 1
        self.ax = fig.add_axes([left, bottom, width, height])
        
        # Se crea el canvas de tkinter que contiene a la figura
        self.canvas = FigureCanvasTkAgg(fig, master = self.master)   
        self.canvas.draw() 
        # colocar el canvas en la ventana 
        self.canvas.get_tk_widget().grid(row = 4,columnspan=2,padx=10,sticky='nw')
        
        # toolbar
        frame_toolbar = tk.Frame(self.master)
        frame_toolbar.grid(row = 5, columnspan=2, sticky='n')
        toolbar = NavigationToolbar2Tk(self.canvas,frame_toolbar)
        toolbar.pack()
        
    
    def aplicarPD(self,n: int,estrategia: str):
        """
        Se realiza las llamadas a los metodos TopDown y BottomUp para calcular
        el termino de la sucesión de Fibonacci seleccionado.

        Parameters
        ----------
        n : int
            Termino de la sucesión de Fibonacci seleccionado.
        estrategia : str
            estrategia de progrmación dinámica selleccionado en el Combobox.

        Returns
        -------
        None.
        """
        # Posibles errores de seleccion
        if not n.isalnum():
            self.entry_Fn.configure(state= 'normal') 
            self.entry_Fn.delete(0,tk.END)
            self.entry_Fn.insert(0,-1) 
            self.entry_Fn.configure(state= 'disabled')
            return
        
        n = int(n)
        # BottomUp
        if estrategia == 'BottomUp':
           Fn = fibonacciBottomUp(n)
   
        # TopDown    
        else:
            Fn = fibonacciTopDown(n, [None] * (n+1))
        self.entry_Fn.configure(state= 'normal')  
        self.entry_Fn.delete(0,tk.END)
        self.entry_Fn.insert(0,Fn) 
        self.entry_Fn.configure(state= 'disabled') 
            
    
    def espiral(self):     
        """
        Se grafica la espiral de fibonacci con arcos hasta el octavo término
        de la sucesión.

        Returns
        -------
        None.

        """
        # ARCOS DE CIRCUNFERENCIA
        # C1
        x = np.linspace(0, 1, 200, endpoint=True)
        y = 1 - np.sqrt(1 - (x-1)**2)
        # dibuja el circulo con lineas cortas
        self.ax.plot(x, y, color="red", markersize=1)
        
        # C2 
        y = 1 + np.sqrt(1 - (x-1)**2)
        # dibuja el circulo con lineas cortas
        self.ax.plot(x, y, color="red", markersize=1)
        
        # C3
        x = np.linspace(1, 3, 200, endpoint=True)
        y = np.sqrt(4 - (x-1)**2)
        # dibuja el circulo con lineas cortas
        self.ax.plot(x, y, color="red", markersize=1) 
        
        # C4
        x = np.linspace(0, 3, 200, endpoint=True)
        y = -np.sqrt(9 - x**2)
        # dibuja el circulo con lineas cortas
        self.ax.plot(x, y, color="red", markersize=1)
        
        # C5
        x = np.linspace(-5, 0, 200)
        y = 2-np.sqrt(25 - x**2)
        # dibuja el circulo con lineas cortas
        self.ax.plot(x, y, color="red", markersize=1)
        
        # C6
        x = np.linspace(-5, 3, 200, endpoint=True)
        y = 2+np.sqrt(64 - (x-3)**2)
        # dibuja el circulo con lineas cortas
        self.ax.plot(x, y, color="red", markersize=1)
        
        # C7
        x = np.linspace(3, 16, 200, endpoint=True)
        y = -3+np.sqrt(169 - (x-3)**2)
        # dibuja el circulo con lineas cortas
        self.ax.plot(x, y, color="red", markersize=1)
        
        # C8
        x = np.linspace(-5, 16, 200, endpoint=True)
        y = -3-np.sqrt(21**2 - (x+5)**2)
        # dibuja el circulo con lineas cortas
        self.ax.plot(x, y, color="red", markersize=1)
        
        self.canvas.draw()
        

# Ventana raiz ################################################################
if __name__ == '__main__':
    raiz = tk.Tk()
    
    # titulo de la ventana
    raiz.title('Sucesión de Fibonacci!!')
    
    # color de fondo
    raiz.configure(background='SteelBlue3')
    
    # ventana no reescalable
    raiz.resizable(False,False)
    
    # icono
    img_icon= ImageTk.PhotoImage(Image.open("fibonacci.png"))
    raiz.iconphoto(False,img_icon,img_icon)
    
    # se crean todos los widgets de la ventana con sus funciones
    ventana = VentanaFib(raiz)
    
    # mantener la ventana abierta
    raiz.mainloop()

















