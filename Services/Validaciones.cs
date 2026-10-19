using System;
using System.Collections.Generic;
using System.Linq;
using DuoDenticFUNPRO.Models;

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

            if (codigo != codigo.Trim())
            {
                return false;
            }

            return codigo.StartsWith(
                       "EXP",
                       StringComparison.OrdinalIgnoreCase)
                   && codigo.Length > 3;
        }

        public static bool CodigoExiste(
            string codigo,
            IEnumerable<Expediente> expedientes)
        {
            if (string.IsNullOrWhiteSpace(codigo) ||
                expedientes == null)
            {
                return false;
            }

            return expedientes.Any(expediente =>
                expediente != null &&
                string.Equals(
                    expediente.Codigo?.Trim(),
                    codigo.Trim(),
                    StringComparison.OrdinalIgnoreCase));
        }

        public static bool ValidarExpediente(
            Expediente expediente,
            IEnumerable<Expediente> expedientes)
        {
            if (expediente == null || expedientes == null)
            {
                return false;
            }

            if (!ValidarCodigo(expediente.Codigo))
            {
                return false;
            }

            if (!ValidarTexto(expediente.TipoSolicitud) ||
                !ValidarTexto(expediente.Descripcion))
            {
                return false;
            }

            if (CodigoExiste(expediente.Codigo, expedientes))
            {
                return false;
            }

            return true;
        }
    }
}