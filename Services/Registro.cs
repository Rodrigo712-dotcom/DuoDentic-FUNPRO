
using System;
using System.Collections.Generic;
using System.Linq;

public class Registro
{
    private static readonly List<Paciente> pacientes = new();

    public static void RegistrarPaciente()
    {
        Console.WriteLine("\n=== REGISTRO DE PACIENTES ===");

        Console.Write("Nombre: ");
        string nombre = Console.ReadLine() ?? "";

        Console.Write("Apellido: ");
        string apellido = Console.ReadLine() ?? "";

        Console.Write("DNI (8 dígitos): ");
        string dni = Console.ReadLine() ?? "";

        Console.Write("Edad: ");
        string edadTexto = Console.ReadLine() ?? "";

        Console.Write("Teléfono (9 dígitos): ");
        string telefono = Console.ReadLine() ?? "";

        Console.Write("Dirección: ");
        string direccion = Console.ReadLine() ?? "";

        if (string.IsNullOrWhiteSpace(nombre) ||
            string.IsNullOrWhiteSpace(apellido) ||
            dni.Length != 8 ||
            !dni.All(char.IsDigit) ||
            !int.TryParse(edadTexto, out int edad) ||
            edad <= 0 ||
            telefono.Length != 9 ||
            !telefono.All(char.IsDigit))
        {
            Console.WriteLine("Datos inválidos. Intente nuevamente.");
            return;
        }

        if (pacientes.Any(p => p.Dni == dni))
        {
            Console.WriteLine("El DNI ya está registrado.");
            return;
        }

        Paciente paciente = new Paciente
        {
            Id = pacientes.Count + 1,
            Nombre = nombre.Trim(),
            Apellido = apellido.Trim(),
            Dni = dni,
            Edad = edad,
            Telefono = telefono,
            Direccion = direccion.Trim()
        };

        pacientes.Add(paciente);
        Console.WriteLine("\nPaciente registrado correctamente.");
    }

    public static void ListarPacientes()
    {
        Console.WriteLine("\n=== PACIENTES REGISTRADOS ===");

        foreach (var paciente in pacientes)
        {
            Console.WriteLine(
                $"{paciente.Id} - {paciente.Nombre} " +
                $"{paciente.Apellido} - DNI: {paciente.Dni}");
        }
    }
}

public class Paciente
{
    public int Id { get; set; }
    public string Nombre { get; set; } = "";
    public string Apellido { get; set; } = "";
    public string Dni { get; set; } = "";
    public int Edad { get; set; }
    public string Telefono { get; set; } = "";
    public string Direccion { get; set; } = "";
}
