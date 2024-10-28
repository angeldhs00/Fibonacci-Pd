# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:13:25 2024

Interfaz gráfica para visualizar los términos de fibonacci.

@author: Angel de Hoyos Sainz
"""
import tkinter as tk 
from tkinter import ttk
from PIL import Image, ImageTk

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
        
        self.master.rowconfigure(0, weight = 18, uniform="r1")
        self.master.rowconfigure(1, weight = 11, uniform="r1")
        self.master.rowconfigure(2, weight = 11, uniform="r1")
        self.master.rowconfigure(3, weight = 11, uniform="r1")
        self.master.rowconfigure(4, weight = 50, uniform="r1")
        self.master.rowconfigure(5, weight = 2, uniform="r1")
        
        # Se crean los widgets
        self.widgets()
        
    
    
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
        lb_n.grid(row=1, column=0, sticky='se')
        
        n = tk.Entry(self.master,width= 6)
        n.grid(row=1, column=1, padx=10, sticky='sw')
        
        
        lb_n1 = tk.Label(self.master,text="Estrategia de programación:",
                         font=('Calibri',12),background='SteelBlue3')
        lb_n1.grid(row=2, column=0, padx=22, sticky='w')
        
        estrategia = ttk.Combobox(self.master,values=['TopDown','BottomUp'],
                                  state="readonly",width=10)
        estrategia.set("TopDown")
        estrategia.grid(row=2, column=1, padx=10, sticky='w')
        
        bt_apply = tk.Button(self.master, text='Aplicar',width=20,
                             command= lambda: self.aplicarPD(int(n.get()),
                                                            estrategia.get()))
        bt_apply.grid(row=3, columnspan=2,padx=170, sticky='w')
        
        esquema = tk.Text(self.master,state='disabled',width= 85,borderwidth=3,
                           height=20)
        esquema.grid(row=4, columnspan=2,padx=5, sticky='nw')
        
    
    # def aplicarPD(self,n,estrategia):
    #     if estrategia == 'Topdown':
            
    #     else:
            








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

















