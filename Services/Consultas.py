"""
consultas.py - Busqueda, ordenamiento y listado.

Los algoritmos estan escritos a mano (sin sorted()/index()) para evidenciar
la logica pedida en el curso (Tema 3: insercion, busqueda y ordenamiento).
"""
from Modelos import Expediente as expediente


def busqueda_secuencial(almacen, codigo):
    """Recorre de 0 a n-1. Devuelve la posicion o -1. Costo O(n)."""
    for i in range(expediente.total(almacen)):
        if almacen["codigo"][i] == codigo:
            return i
    return -1


def esta_ordenado(almacen):
    """True si los codigos estan en orden ascendente."""
    for i in range(1, expediente.total(almacen)):
        if almacen["codigo"][i - 1] > almacen["codigo"][i]:
            return False
    return True

