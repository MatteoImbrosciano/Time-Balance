from datetime import datetime
from dataclasses import dataclass, field
from typing import List
from .medicamento import Medicamento
import locale
from typing import Optional

@dataclass
class Ticket:
    cliente: str = None
    fecha: datetime = None
    medicamentos: List[Medicamento] = field(default_factory=list)
    totale: float = None

    def cargar_ticket_desde_txt(self, file_path: str):
        locale.setlocale(locale.LC_TIME, 'it_IT.UTF-8')  
        lines = self._leggi_file(file_path)
        self._parsa_dati_generali(lines)  
        medicamentos = self._estrai_medicamenti(lines)  
        self._aggiorna_medicamentos(medicamentos)  

    def _leggi_file(self, file_path: str) -> List[str]:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.readlines()

    def _parsa_dati_generali(self, lines: List[str]):
        for line in lines:
            line = line.strip()
            if line.startswith("Cliente:"):
                self.cliente = self._parsa_cliente(line)
            elif line.startswith("Data:"):
                self.fecha = self._parsa_data(line)
            elif line.startswith("Totale:"):
                self.totale = self._parsa_totale(line)

    def _estrai_medicamenti(self, lines: List[str]) -> List[Medicamento]:
        medicamentos = []
        for line in lines:
            line = line.strip()
            if "|" in line and not line.startswith("Articolo"):
                medicamento = self._parsa_medicamento(line)
                if medicamento:
                    medicamentos.append(medicamento)
        return medicamentos

    def _aggiorna_medicamentos(self, medicamentos: List[Medicamento]):
        self.medicamentos.clear()
        self.medicamentos.extend(medicamentos)

    @staticmethod
    def _parsa_cliente(line: str) -> str:
        return line.split(":", 1)[1].strip()

    @staticmethod
    def _parsa_data(line: str) -> datetime:
        data_testo = line.split(":", 1)[1].strip()
        return datetime.strptime(data_testo, "%d %B %Y")

    @staticmethod
    def _parsa_totale(line: str) -> float:
        return float(line.split(":", 1)[1].strip().replace("€", "").replace(",", "."))

    @staticmethod
    def _parsa_medicamento(line: str) -> Optional[Medicamento]:

        try:
            parts = line.split("|")
            if len(parts) != 4:
                raise ValueError(f"Formato errato della riga: {line}")
        
            nombre = parts[0].strip()
            if not nombre:
                raise ValueError(f"Nome del medicinale mancante nella riga: {line}")
        
            cantidad_info = parts[1].strip().split()
            if len(cantidad_info) != 2:
                raise ValueError(f"Informazioni sulla quantità malformate nella riga: {line}")
        
            cantidad = float(cantidad_info[0])
            unitad = cantidad_info[1]
            precio = float(parts[3].strip().replace("€", "").replace(",", "."))
        
            return Medicamento(nombre, cantidad, precio, unitad)
        except ValueError as e:
            print(f"Errore nel parsificare la riga: {e}")
            return None
