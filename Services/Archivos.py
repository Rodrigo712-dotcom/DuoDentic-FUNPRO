"""
archivos.py - Persistencia en archivo de texto (.txt).

Formato: una linea por expediente, campos separados por '|':
    codigo|tipo|descripcion|estado|fecha
Se eligio TXT (y no binario) porque es legible, facil de revisar
y suficiente para el volumen del prototipo (Tema 5).
"""
from Models import Expediente as expediente
from Services import Validaciones as val

RUTA_POR_DEFECTO = "expedientes.txt"


def guardar(almacen, ruta=RUTA_POR_DEFECTO):
    """Escribe todos los expedientes. Devuelve (ok, mensaje)."""
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            for i in range(expediente.total(almacen)):
                linea = val.SEPARADOR.join(expediente.obtener(almacen, i))
                archivo.write(linea + "\n")
        return True, f"{expediente.total(almacen)} expediente(s) guardado(s) en '{ruta}'."
    except OSError as error:
        return False, f"No se pudo guardar: {error}"


def cargar(almacen, ruta=RUTA_POR_DEFECTO):
    """Lee el archivo y llena el almacen. Omite lineas danadas o duplicadas.
    Devuelve (cargados, omitidos)."""
    cargados = 0
    omitidos = 0
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea == "":
                    continue
                partes = linea.split(val.SEPARADOR)          # cadena -> campos
                if len(partes) != len(expediente.CAMPOS):
                    omitidos += 1
                    continue
                codigo, tipo, desc, estado, fecha = partes
                codigo_ok, _ = val.validar_codigo(codigo)
                estado_ok, _ = val.validar_estado(estado)
                if (not codigo_ok or not estado_ok
                        or val.codigo_duplicado(almacen, codigo)):
                    omitidos += 1
                    continue
                expediente.agregar(almacen, codigo, tipo, desc, estado, fecha)
                cargados += 1
    except FileNotFoundError:
        pass   # primera ejecucion: aun no existe el archivo
    return cargados, omitidos
