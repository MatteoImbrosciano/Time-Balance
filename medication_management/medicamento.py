from dataclasses import dataclass

@dataclass
class Medicamento:
    nombre: str
    cantidad: float
    precio: float
    unitad: str  
    
    def __post_init__(self):
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if self.cantidad <= 0:
            raise ValueError("La cantidad debe ser un valor numérico positivo.")
        if self.precio <= 0:
            raise ValueError("El precio debe ser un valor numérico positivo.")
        if not isinstance(self.unitad, str) or not self.unitad.strip():
            raise ValueError("La unidad debe ser una cadena no vacía.")
    