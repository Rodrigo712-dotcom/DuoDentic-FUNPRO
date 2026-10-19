
namespace DuoDenticFUNPRO.Services
{
    public class Validaciones
    {
        public static bool ValidarTexto(string texto)
        {
            return !string.IsNullOrWhiteSpace(texto);
        }

        public static bool ValidarCodigo(string codigo)
        {
            if (string.IsNullOrWhiteSpace(codigo))
            {
                return false;
            }

            codigo = codigo.Trim();

            return codigo.StartsWith(
                "EXP",
                StringComparison.OrdinalIgnoreCase)
                && codigo.Length > 3;
        }
    }
}
