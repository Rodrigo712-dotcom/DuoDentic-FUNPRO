"""
Program.py - Sistema Administrativo Duo Dentic.
Integra registro, busqueda, ordenamiento y archivos.
"""

from Models import Expediente
from Services import Registro
from Services import Consultas
from Services import Archivos
from Services import Validaciones


def mostrar_menu():
    print("\n=======================================")
    print("    SISTEMA ADMINISTRATIVO DUO DENTIC")
    print("=======================================")
    print("1. Registrar expediente")
    print("2. Buscar expediente")
    print("3. Listar expedientes")
    print("4. Ordenar expedientes")
    print("5. Almacenar expedientes")
    print("0. Salir")
    print("=======================================")


def buscar_expediente(almacen):
    print("\n--- BUSCAR EXPEDIENTE ---")

    codigo = input("Ingrese el codigo: ")
    codigo = Validaciones.normalizar_codigo(codigo)

    indice, metodo = Consultas.buscar(almacen, codigo)

    print(f"\nMetodo utilizado: Busqueda {metodo}")

    if indice == -1:
        print("Expediente no encontrado.")
        return

    cod, tipo, descripcion, estado, fecha = (
        Expediente.obtener(almacen, indice)
    )

    print("\nEXPEDIENTE ENCONTRADO")
    print("-----------------------------------")
    print("Codigo:", cod)
    print("Tipo:", tipo)
    print("Descripcion:", descripcion)
    print("Estado:", estado)
    print("Fecha:", fecha)
    print("-----------------------------------")


def ejecutar():
    almacen = Expediente.crear_almacen()

    # Recuperar expedientes guardados anteriormente.
    cargados, omitidos = Archivos.cargar(almacen)

    print("\nSistema Administrativo Duo Dentic")
    print("Expedientes recuperados:", cargados)

    if omitidos > 0:
        print("Registros omitidos:", omitidos)

    opcion = ""

    while opcion != "0":

        print("\nExpedientes registrados:", Expediente.total(almacen))
        mostrar_menu()

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":

            Registro.registrar_interactivo(almacen)

        elif opcion == "2":

            buscar_expediente(almacen)

        elif opcion == "3":

            Consultas.listar(almacen)

        elif opcion == "4":

            Consultas.ordenar_por_codigo(almacen)
            print("Expedientes ordenados correctamente.")

        elif opcion == "5":

            ok, mensaje = Archivos.guardar(almacen)
            print(mensaje)

        elif opcion == "0":

            ok, mensaje = Archivos.guardar(almacen)
            print(mensaje)
            print("Saliendo del sistema...")

        else:

            print("Opcion invalida. Intente nuevamente.")


if __name__ == "__main__":
    ejecutar()
