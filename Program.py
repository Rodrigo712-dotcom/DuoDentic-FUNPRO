from DuoDenticFUNPRO.Models import Expediente

expedientes = []

prueba = Expediente()

prueba.Codigo = "EXP001"
prueba.TipoSolicitud = "Solicitud administrativa"
prueba.Descripcion = "Solicitud de registro de paciente"
prueba.Estado = "Pendiente"

expedientes.append(prueba)

opcion = ""

while opcion != "0":
    print("Expedientes registrados:", len(expedientes))

    MostrarMenu()

    print()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Modulo de registro de expedientes en desarrollo...")

    elif opcion == "2":
        print("Modulo de búsqueda de expedientes en desarrollo...")

    elif opcion == "3":
        print("Modulo de listado de expedientes en desarrollo...")

    elif opcion == "4":
        print("Modulo de ordenamiento de expedientes en desarrollo...")

    elif opcion == "5":
        print("Modulo de almacenamiento de expedientes en desarrollo...")

    elif opcion == "0":
        print("Saliendo del sistema...")

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


def MostrarMenu():
    print("=======================================")
    print("    SISTEMA ADMINISTRATIVO DUO DENTIC")
    print("=======================================")
    print()
    print("1. Registrar expediente")
    print("2. Buscar expediente")
    print("3. Listar expedientes")
    print("4. Ordenar expedientes")
    print("5. Almacenar expedientes")
    print("0. Salir")
