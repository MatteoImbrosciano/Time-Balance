from datetime import datetime
from dataclasses import dataclass, field
from typing import List
from .medicamento import Medicamento
import locale

@dataclass
class Ticket:
    cliente: str = None
    fecha: datetime = None
    medicamentos: List[Medicamento] = field(default_factory=list)
    totale: float = None

    def cargar_ticket_desde_txt(self, file_path: str):
        """Metodo principale per caricare i dati del ticket da un file di testo."""
        locale.setlocale(locale.LC_TIME, 'it_IT.UTF-8')  
        lines = self._leggi_file(file_path)
        self._parsa_dati_generali(lines)  # Analizza i dati generali (cliente, data, totale)
        medicamentos = self._estrai_medicamenti(lines)  # Estrae i medicinali
        self._aggiorna_medicamentos(medicamentos)  # Aggiorna lo stato interno dei medicinali

    def _leggi_file(self, file_path: str) -> List[str]:
        """Legge un file di testo e restituisce una lista di righe."""
        with open(file_path, "r", encoding="utf-8") as file:
            return file.readlines()

    def _parsa_dati_generali(self, lines: List[str]):
        """Analizza i dati generali del ticket: cliente, data e totale."""
        for line in lines:
            line = line.strip()
            if line.startswith("Cliente:"):
                self.cliente = self._parsa_cliente(line)
            elif line.startswith("Data:"):
                self.fecha = self._parsa_data(line)
            elif line.startswith("Totale:"):
                self.totale = self._parsa_totale(line)

    def _estrai_medicamenti(self, lines: List[str]) -> List[Medicamento]:
        """Estrae i farmaci dalle righe fornite e restituisce una lista di Medicamento."""
        medicamentos = []
        for line in lines:
            line = line.strip()
            if "|" in line and not line.startswith("Articolo"):
                medicamento = self._parsa_medicamento(line)
                if medicamento:
                    medicamentos.append(medicamento)
        return medicamentos

    def _aggiorna_medicamentos(self, medicamentos: List[Medicamento]):
        """Aggiorna la lista interna dei medicinali con quelli forniti."""
        self.medicamentos.clear()
        self.medicamentos.extend(medicamentos)

    @staticmethod
    def _parsa_cliente(line: str) -> str:
        """Estrae il cliente dalla riga."""
        return line.split(":", 1)[1].strip()

    @staticmethod
    def _parsa_data(line: str) -> datetime:
        """Estrae e converte la data dalla riga."""
        data_testo = line.split(":", 1)[1].strip()
        return datetime.strptime(data_testo, "%d %B %Y")

    @staticmethod
    def _parsa_totale(line: str) -> float:
        """Estrae e converte il totale dalla riga."""
        return float(line.split(":", 1)[1].strip().replace("€", "").replace(",", "."))

    @staticmethod
    def _parsa_medicamento(line: str) -> Medicamento:
        """Parsifica una riga e restituisce un oggetto Medicamento."""
        parts = line.split("|")
        if len(parts) == 4:
            nombre = parts[0].strip()
            cantidad_info = parts[1].strip().split()
            cantidad = float(cantidad_info[0])
            unitad = cantidad_info[1] if len(cantidad_info) > 1 else ''
            precio = float(parts[3].strip().replace("€", "").replace(",", "."))
            return Medicamento(nombre, cantidad, precio, unitad)
        return None
