from dataclasses import dataclass, field
from typing import List
from .medicamento import Medicamento

@dataclass
class Inventario:
    medicamentos: List[Medicamento] = field(default_factory=list)

    def agregar_medicamento(self, medicamento: Medicamento):
        if not isinstance(medicamento, Medicamento):
            raise TypeError("L'oggetto deve essere un'istanza della classe Medicamento.")
        for med in self.medicamentos:
            if med.nombre == medicamento.nombre:
                med.cantidad += medicamento.cantidad
                return
        self.medicamentos.append(medicamento)

    def eliminare_medicamento(self, nome: str):
        self.medicamentos = [
            med for med in self.medicamentos if med.nombre != nome.strip()
        ]

    def ottenere_inventario(self):
        """Restituisce una lista dei medicinali nell'inventario."""
        return [(med.nombre, med.cantidad, med.unitad) for med in self.medicamentos]

    def __str__(self):
        if not self.medicamentos:
            return "L'inventario è vuoto."
        return "\n".join(str(med) for med in self.medicamentos)
