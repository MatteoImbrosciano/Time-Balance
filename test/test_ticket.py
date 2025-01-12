import pytest
from medication_management.ticket import Ticket
from medication_management.medicamento import Medicamento

def test_cargar_ticket_desde_txt(tmp_path):

    ticket_content = """Pharmacy Receipt - Farmacia Italia  
Cliente: Matteo Imbrosciano  
Data: 15 Febbraio 2024

Articolo              | Quantità (mg/ml) | Unità | Importo (Euro)
----------------------------------------------------------------
Sintrom               | 1 mg            |   1   |    €7.50
Elidel                | 10 mg/g         |   1   |   €12.30
Protopic              | 0.3 mg          |   1   |    €9.80
Decloban              | 500 mic         |   1   |    €7.10
Dolquine              | 200 mg          |   1   |   €10.60
Hemovas               | 400 mg          |   1   |    €8.40

----------------------------------------------------------------
Totale: €55.70
"""
    ticket_path = tmp_path / "ticket.txt"
    ticket_path.write_text(ticket_content, encoding="utf-8")

    ticket = Ticket()
    ticket.cargar_ticket_desde_txt(str(ticket_path))

    assert ticket.cliente == "Matteo Imbrosciano"
    
    assert ticket.fecha.strftime("%d %B %Y").capitalize() == "15 Febbraio 2024".capitalize()
    
    assert ticket.totale == 55.70
    assert len(ticket.medicamentos) == 6

    medicamento1 = ticket.medicamentos[0]
    assert medicamento1.nombre == "Sintrom"
    assert medicamento1.cantidad == 1
    assert medicamento1.unitad == "mg"
    assert medicamento1.precio == 7.50

    medicamento2 = ticket.medicamentos[1]
    assert medicamento2.nombre == "Elidel"
    assert medicamento2.cantidad == 10
    assert medicamento2.unitad == "mg/g"
    assert medicamento2.precio == 12.30
