import pytest
from medication_management.inventario import Inventario
from medication_management.medicamento import Medicamento

def test_aggiunta_medicamento():
    inventario = Inventario()
    medicamento = Medicamento("Aspirina", 100, 4.50, "mg")
    inventario.agregar_medicamento(medicamento)
    assert len(inventario.medicamentos) == 1
    assert inventario.medicamentos[0] == medicamento

def test_aggiunta_medicamento_esistente():
    inventario = Inventario()
    medicamento1 = Medicamento("Aspirina", 100, 4.50, "mg")
    medicamento2 = Medicamento("Aspirina", 50, 4.50, "mg")
    inventario.agregar_medicamento(medicamento1)
    inventario.agregar_medicamento(medicamento2)
    assert len(inventario.medicamentos) == 1
    assert inventario.medicamentos[0].cantidad == 150

def test_eliminazione_medicamento():
    inventario = Inventario()
    medicamento = Medicamento("Aspirina", 100, 4.50, "mg")
    inventario.agregar_medicamento(medicamento)
    inventario.eliminare_medicamento("Aspirina")  
    assert len(inventario.medicamentos) == 0


def test_ottenere_inventario():
    inventario = Inventario()
    medicamento1 = Medicamento("Aspirina", 100, 4.50, "mg")
    medicamento2 = Medicamento("Paracetamolo", 200, 3.00, "mg")
    inventario.agregar_medicamento(medicamento1)
    inventario.agregar_medicamento(medicamento2)
    inventario_data = inventario.ottenere_inventario()  
    assert len(inventario_data) == 2
    assert inventario_data[0] == ("Aspirina", 100, "mg")
    assert inventario_data[1] == ("Paracetamolo", 200, "mg")

