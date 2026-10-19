using DuoDenticFUNPRO.Services;

Console.WriteLine(
    Validaciones.ValidarTexto("Solicitud de tratamiento"));

Console.WriteLine(
    Validaciones.ValidarTexto(""));

Console.WriteLine(
    Validaciones.ValidarTexto("   "));

Console.WriteLine(Validaciones.ValidarCodigo("EXP001"));
Console.WriteLine(Validaciones.ValidarCodigo("EXP"));
Console.WriteLine(Validaciones.ValidarCodigo("ABC001"));