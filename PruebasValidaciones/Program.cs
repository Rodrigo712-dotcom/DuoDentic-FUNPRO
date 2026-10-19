using DuoDenticFUNPRO.Services;
using DuoDenticFUNPRO.Models;
using System.Collections.Generic;

Console.WriteLine("=== PRUEBAS DE VALIDACIONES ===");

Console.WriteLine("\n--- ValidarTexto ---");
Console.WriteLine(
    Validaciones.ValidarTexto("Solicitud de tratamiento"));
Console.WriteLine(
    Validaciones.ValidarTexto(""));
Console.WriteLine(
    Validaciones.ValidarTexto("   "));

Console.WriteLine("\n--- ValidarCodigo ---");
Console.WriteLine(Validaciones.ValidarCodigo("EXP001"));
Console.WriteLine(Validaciones.ValidarCodigo("EXP"));
Console.WriteLine(Validaciones.ValidarCodigo("ABC001"));

Console.WriteLine("\n--- CodigoExiste ---");
var expedientePrueba = new Expediente
{
    Codigo = "EXP001",
    TipoSolicitud = "Consulta",
    Descripcion = "Prueba ficticia",
    Estado = "Pendiente"
};

var expedientesPrueba = new List<Expediente>
{
    expedientePrueba
};

Console.WriteLine(
    Validaciones.CodigoExiste("EXP001", expedientesPrueba));
Console.WriteLine(
    Validaciones.CodigoExiste("EXP002", expedientesPrueba));
Console.WriteLine(
    Validaciones.CodigoExiste("exp001", expedientesPrueba));

Console.WriteLine("\n--- ValidarExpediente ---");

var expedienteValido = new Expediente
{
    Codigo = "EXP100",
    TipoSolicitud = "Tratamiento",
    Descripcion = "Evaluación odontológica",
    Estado = "Pendiente"
};

Console.WriteLine(
    Validaciones.ValidarExpediente(
        expedienteValido,
        expedientesPrueba));

var expedienteSinTipo = new Expediente
{
    Codigo = "EXP101",
    TipoSolicitud = "",
    Descripcion = "Evaluación odontológica",
    Estado = "Pendiente"
};

Console.WriteLine(
    Validaciones.ValidarExpediente(
        expedienteSinTipo,
        expedientesPrueba));

var expedienteDuplicado = new Expediente
{
    Codigo = "EXP001",
    TipoSolicitud = "Consulta",
    Descripcion = "Otro registro ficticio",
    Estado = "Pendiente"
};

Console.WriteLine(
    Validaciones.ValidarExpediente(
        expedienteDuplicado,
        expedientesPrueba));

Console.WriteLine("\n=== FIN DE LAS PRUEBAS ===");