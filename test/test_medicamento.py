import pytest
from medication_management.medicamento import Medicamento

def test_medicamento_inizializzazione_valida():
    medicamento = Medicamento("Aspirina", 100, 4.50, "mg")
    assert medicamento.nombre == "Aspirina"
    assert medicamento.cantidad == 100
    assert medicamento.precio == 4.50
    assert medicamento.unitad == "mg"

def test_medicamento_inizializzazione_nome_non_valido():
    with pytest.raises(ValueError):
        Medicamento("", 100, 4.50, "mg")

def test_medicamento_inizializzazione_quantita_non_valida():
    with pytest.raises(ValueError):
        Medicamento("Aspirina", -10, 4.50, "mg")

def test_medicamento_inizializzazione_prezzo_non_valido():
    with pytest.raises(ValueError):
        Medicamento("Aspirina", 100, 0, "mg")

def test_medicamento_inizializzazione_unita_non_valida():
    with pytest.raises(ValueError):
        Medicamento("Aspirina", 100, 4.50, "")
