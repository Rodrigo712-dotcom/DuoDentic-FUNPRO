
namespace DuoDentic_FUNPRO.Models
{
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
}
