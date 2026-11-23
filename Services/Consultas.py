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


def busqueda_binaria(almacen, codigo):
    """Requiere arreglo ordenado. Devuelve la posicion o -1. Costo O(log n)."""
    inferior = 0
    superior = expediente.total(almacen) - 1
    while inferior <= superior:
        medio = (inferior + superior) // 2
        actual = almacen["codigo"][medio]
        if actual == codigo:
            return medio
        if actual < codigo:
            inferior = medio + 1
        else:
            superior = medio - 1
    return -1


def buscar(almacen, codigo):
    """Elige el algoritmo: binaria si esta ordenado, secuencial si no.
    Devuelve (indice, nombre_del_metodo)."""
    if esta_ordenado(almacen):
        return busqueda_binaria(almacen, codigo), "binaria"
    return busqueda_secuencial(almacen, codigo), "secuencial"


def ordenar_por_codigo(almacen):
    """Ordenamiento por insercion sobre TODOS los arreglos paralelos,
    para que cada expediente conserve sus datos. Costo O(n^2)."""
    n = expediente.total(almacen)
    for i in range(1, n):
        clave = expediente.obtener(almacen, i)   # tupla completa del expediente
        j = i - 1
        while j >= 0 and almacen["codigo"][j] > clave[0]:
            for campo in expediente.CAMPOS:      # desplazar todos los campos
                almacen[campo][j + 1] = almacen[campo][j]
            j -= 1
        for pos in range(len(expediente.CAMPOS)):
            almacen[expediente.CAMPOS[pos]][j + 1] = clave[pos]
