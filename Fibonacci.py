# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 17:18:07 2024

Cálculo de los terminos de la sucesión de Fibonacci, basada en
estrategias de programación dinámica.

@author: Angel de Hoyos Sainz
"""



# [None] * (4+1)
def fibonacciTopDown(n: int, Fn: list)-> int:
    """
    Cálculo del termino n de la sucesión de Fibonacci mediante el método 
    Top-Down.

    Parameters
    ----------
    n : int
        Número del término de la sucesión de Fibonacci que se desea calcular.
        
    Fn: lista de longitud n donde se irán colocando los valores de la sucesión
        de Fibonacci.

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
    # Realizamos dos llamadas recursivas si el termino Fn no esta calculado
    else:
        if Fn[n] == None:
            Fn[n] = fibonacciTopDown(n-1,Fn) + fibonacciTopDown(n-2,Fn)
        return Fn[n]
      
def fibonacciBottomUp(n: int)-> int:
    """
    Cálculo del termino n de la sucesión de Fibonacci mediante el método 
    Bottom-Up.
    
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
    
    # se introduce un número negativo
    if n < 0:
        return -1
    # casos sencillos cuando n=0 o n=1
    if n == 0 or n == 1:
        return n
    # inicializo las variables para los valore an-1 y an-2
    a = 0
    b = 1
    # calculo de términos sin necesidad de una lista con n elementos
    for i in range(0,n):
        c = a + b
        a = b
        b = c
        
    return c
        




















