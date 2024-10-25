# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 17:18:07 2024

Calculo de los terminos de la sucesión de Fibonacci, basada en la
estrategia de programación dinámica Top-Down

@author: Angel de Hoyos Sainz
"""
import numpy as np

# np.empty(3)* np.nan

def fibonacciTopDown(n: int, Fn: list)-> int:
    """
    Cálculo del termino n de la sucesión de Fibonacci mediante el método 
    Top-Down.

    Parameters
    ----------
    n : int
        Número del término de la sucesión de Fibonacci que se desea calcular.

    Returns
    -------
    int
        Valor del término n-esimo de la sucesión de Fibonacci. Se
        retorna -1 si el número de término introducido es negativo.
    """
    # se introduce un número no natural
    if n < 0:
        return -1
    # casos sencillos cuando n=0 o n=1, guardamos el valor
    if n == 0 or n == 1:
        Fn[n] = n
        return n
    # Caso no calculado uno de los dos
    else:
        if Fn[n] == None:
            Fn[n] = fibonacciTopDown(n-1,Fn) + fibonacciTopDown(n-2,Fn)
        return Fn[n]
        
    




















