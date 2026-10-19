namespace DuoDenticFUNPRO.Models
{
    public class Expediente
    {
        public string Codigo { get; set; } = "";
        public string TipoSolicitud { get; set; } = "";
        public string Descripcion { get; set; } = "";
        public string Estado { get; set; } = "Pendiente";
        public DateTime FechaRegistro { get; set; } = DateTime.Now;
    }
}
