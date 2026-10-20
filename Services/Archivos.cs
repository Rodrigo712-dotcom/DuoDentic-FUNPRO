
using System;
using System.Collections.Generic;
using System.IO;
using DuoDenticFUNPRO.Models;

namespace DuoDenticFUNPRO.Services
{
    public class Archivos
    {
        public void GuardarExpedientes(List<Expediente> expedientes)
        {
            Console.WriteLine("Modulo de guardado de expedientes");
            string ruta = "expedientes.txt";

            try
            {
                List<string> lineas = new List<string>();

                foreach (Expediente expediente in expedientes)
                {
                    string linea =
                        $"{expediente.Codigo}|" +
                        $"{expediente.TipoSolicitud}|" +
                        $"{expediente.Descripcion}|" +
                        $"{expediente.Estado}|" +
                        $"{expediente.FechaRegistro:yyyy-MM-dd HH:mm:ss}";

                    lineas.Add(linea);
                }

                File.WriteAllLines(ruta, lineas);

                Console.WriteLine("Expedientes guardados correctamente.");
                Console.WriteLine("Archivo: " + Path.GetFullPath(ruta));
                Console.WriteLine("Cantidad guardada: " + lineas.Count);
            }
            catch (IOException ex)
            {
                Console.WriteLine("Error al guardar el archivo: " + ex.Message);
            }
            catch (UnauthorizedAccessException ex)
            {
                Console.WriteLine("No hay permisos para guardar el archivo: " + ex.Message);
            }
        }
    }
}
