namespace DuoDenticFUNPRO.services
{
    public class Validaciones
    {
        public static bool ValidarTexto(string texto)
        {
            return !string.IsNullOrWhiteSpace(texto);
        }
    }
}
