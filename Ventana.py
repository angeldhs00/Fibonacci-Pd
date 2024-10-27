# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:13:25 2024

Interfaz gráfica para visualizar los términos de fibonacci.

@author: Angel de Hoyos Sainz
"""
import tkinter as tk 
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
        raiz_width = 600
        raiz_height = 450
        cent_x = int((self.master.winfo_screenwidth() - raiz_width)/2) 
        cent_y = int((self.master.winfo_screenheight() - raiz_height)/2)
        self.master.geometry(f"{raiz_width}x{raiz_height}+{cent_x}+{cent_y}")
        
        # disposición de la ventana
        self.master.columnconfigure(0, weight = 6)
        self.master.columnconfigure(1, weight = 4)
        
        self.master.rowconfigure(0, weight = 2)
        self.master.rowconfigure(1, weight = 4)
        self.master.rowconfigure(2, weight = 4)
        
        # Se crean los widgets
        self.widgets()
        
    
    
    def widgets(self):
        """
        Crea los widgets de la ventana y establece sus funcionalidades.

        Returns
        -------
        None.

        """
        
        self.img_port = ImageTk.PhotoImage(Image.open("portada.jpeg"))
        lb_img_port = tk.Label(self.master, image=self.img_port)
        lb_img_port.grid(row=0, column=0,columnspan=2, sticky='nsew')
        





# Ventana raiz ################################################################
if __name__ == '__main__':
    raiz = tk.Tk()
    
    # titulo de la ventana
    raiz.title('Sucesión de Fibonacci!!')
    
    # ventana no reescalable
    raiz.resizable(False,False)
    
    img_icon= ImageTk.PhotoImage(Image.open("fibonacci.png"))
    raiz.iconphoto(False,img_icon,img_icon)
    
    # se crean todos los widgets de la ventana con sus funciones
    ventana = VentanaFib(raiz)
    
    # mantener la ventana abierta
    raiz.mainloop()

















