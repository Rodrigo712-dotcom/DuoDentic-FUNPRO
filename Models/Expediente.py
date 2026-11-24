"""
Expediente.py - Modelo y almacenamiento de expedientes.
"""

CAMPOS = ["codigo", "tipo", "descripcion", "estado", "fecha"]

ESTADO_INICIAL = "Pendiente"

ESTADOS_VALIDOS = [
    "Pendiente",
    "En proceso",
    "Finalizado"
]


def crear_almacen():
    """Crea los arreglos paralelos para almacenar expedientes."""
    almacen = {}

    for campo in CAMPOS:
        almacen[campo] = []

    return almacen


def total(almacen):
    """Devuelve la cantidad de expedientes registrados."""
    return len(almacen["codigo"])


def agregar(almacen, codigo, tipo, descripcion, estado, fecha):
    """Agrega un expediente a todos los arreglos."""
    almacen["codigo"].append(codigo)
    almacen["tipo"].append(tipo)
    almacen["descripcion"].append(descripcion)
    almacen["estado"].append(estado)
    almacen["fecha"].append(fecha)


def obtener(almacen, indice):
    """Devuelve todos los datos de un expediente."""
    return tuple(almacen[campo][indice] for campo in CAMPOS)
