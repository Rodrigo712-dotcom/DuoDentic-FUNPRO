from datetime import datetime

from Models import Expediente as expediente
from Services import Validaciones as val


def registrar_expediente(almacen, codigo, tipo, descripcion):
    """Valida los datos y, si todo es correcto, agrega el expediente."""
    codigo = val.normalizar_codigo(codigo)
    tipo = tipo.strip()
    descripcion = descripcion.strip()

    ok, msg = val.validar_codigo(codigo)
    if not ok:
        return False, msg
    if val.codigo_duplicado(almacen, codigo):
        return False, f"El codigo {codigo} ya existe."
    ok, msg = val.validar_texto(tipo, "El tipo de solicitud", 50)
    if not ok:
        return False, msg
    ok, msg = val.validar_texto(descripcion, "La descripcion")
    if not ok:
        return False, msg

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
    expediente.agregar(almacen, codigo, tipo, descripcion,
                       expediente.ESTADO_INICIAL, fecha)
    return True, "Expediente registrado correctamente."


def cambiar_estado(almacen, indice, nuevo_estado):
    """Actualiza el estado del expediente en la posicion `indice`."""
    ok, msg = val.validar_estado(nuevo_estado)
    if not ok:
        return False, msg
    almacen["estado"][indice] = nuevo_estado
    return True, "Estado actualizado."


def registrar_interactivo(almacen):
    """Pide los datos por consola; repite si hay error hasta que el usuario cancele."""
    print("\n--- REGISTRAR EXPEDIENTE ---")
    while True:
        codigo = input("Codigo (ej. EXP001): ")
        tipo = input("Tipo de solicitud: ")
        descripcion = input("Descripcion: ")
        ok, mensaje = registrar_expediente(almacen, codigo, tipo, descripcion)
        print(("[OK] " if ok else "[ERROR] ") + mensaje)
        if ok:
            return
        reintentar = input("Reintentar? (s/n): ").strip().lower()
        if reintentar != "s":
            return