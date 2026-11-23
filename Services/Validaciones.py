"""
validaciones.py - Validacion de datos de entrada (cadenas de caracteres).

Todas las funciones devuelven una tupla (es_valido, mensaje).
"""
from expediente import ESTADOS_VALIDOS

PREFIJO = "EXP"
LARGO_CODIGO = 6          # EXP + 3 digitos -> EXP001
SEPARADOR = "|"           # separador del archivo TXT, no se permite en textos
MAX_DESCRIPCION = 200


def normalizar_codigo(codigo):
    """Quita espacios sobrantes y pasa a mayusculas: ' exp001 ' -> 'EXP001'."""
    return codigo.strip().upper()


def validar_codigo(codigo):
    """Formato EXP + 3 digitos (ej. EXP001)."""
    if codigo == "":
        return False, "El codigo no puede estar vacio."
    if len(codigo) != LARGO_CODIGO:
        return False, "El codigo debe tener 6 caracteres (ej. EXP001)."
    if not codigo.startswith(PREFIJO):
        return False, "El codigo debe empezar con 'EXP'."
    if not codigo[3:].isdigit():
        return False, "Despues de 'EXP' deben ir 3 digitos."
    return True, "Codigo valido."


def codigo_duplicado(almacen, codigo):
    """True si el codigo ya esta registrado (recorrido secuencial)."""
    for existente in almacen["codigo"]:
        if existente == codigo:
            return True
    return False


def validar_texto(texto, nombre_campo, maximo=MAX_DESCRIPCION):
    """Texto no vacio, sin el separador '|' y con largo maximo."""
    limpio = texto.strip()
    if limpio == "":
        return False, f"{nombre_campo} no puede estar vacio."
    if SEPARADOR in limpio:
        return False, f"{nombre_campo} no puede contener el caracter '{SEPARADOR}'."
    if len(limpio) > maximo:
        return False, f"{nombre_campo} excede {maximo} caracteres."
    return True, "Texto valido."


def validar_estado(estado):
    """El estado debe pertenecer a la lista de estados permitidos."""
    if estado in ESTADOS_VALIDOS:
        return True, "Estado valido."
    return False, "Estado invalido. Use: " + ", ".join(ESTADOS_VALIDOS)
