using DuoDenticFUNPRO.Models;
List<Expediente> expedientes = new List<Expediente>();

Expediente prueba = new Expediente();

prueba.Codigo = "EXP001";
prueba.TipoSolicitud = "Solicitud administrativa";
prueba.Descripcion = "Solicitud de registro de paciente";
prueba.Estado = "Pendiente";

expedientes.Add(prueba);

string opcion;
do
{
    Console.WriteLine("Expedientes registrados: " + expedientes.Count);
MostrarMenu();
Console.WriteLine();
Console.Write("Seleccione una opción: ");
opcion = Console.ReadLine() ?? "";

switch (opcion)
{
    case "1":
        Console.WriteLine("Modulo de registro de expedientes en desarrollo...");
        break;
    case "2":
        Console.WriteLine("Modulo de búsqueda de expedientes en desarrollo...");
        break;
    case "3":
        Console.WriteLine("Modulo de listado de expedientes en desarrollo...");
        break;
    case "4":
        Console.WriteLine("Modulo de ordenamiento de expedientes en desarrollo...");
        break;
    case "5":
        Console.WriteLine("Modulo de almacenamiento de expedientes en desarrollo...");
        break;
    case "0":
        Console.WriteLine("Saliendo del sistema...");
        break;
    default:
        Console.WriteLine("Opción inválida. Por favor, seleccione una opción válida.");
        break;
}
}while (opcion != "0");
static void MostrarMenu()
{
    Console.WriteLine("=======================================");
    Console.WriteLine("    SISTEMA ADMINISTRATIVO DUO DENTIC");
    Console.WriteLine("=======================================");
    Console.WriteLine();
    Console.WriteLine("1. Registrar expediente");
    Console.WriteLine("2. Buscar expediente");
    Console.WriteLine("3. Listar expedientes");
    Console.WriteLine("4. Ordenar expedientes");
    Console.WriteLine("5. Almacenar expedientes");
    Console.WriteLine("0. Salir");
}
