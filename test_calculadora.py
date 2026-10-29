import pytest
from calculadora import sumar, restar, multiplicar, dividir

# --- Casos Base ---
def test_sumar_positivos():
    assert sumar(2, 3) == 5

def test_sumar_negativos():
    assert sumar(-2, -3) == -5

def test_dividir_exactamente():
    assert dividir(10, 2) == 5

def test_dividir_decimal():
    assert dividir(7, 2) == 3.5

def test_dividir_entre_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)

# --- Actividad Complementaria ---
def test_restar_positivos():
    assert restar(10, 5) == 5

def test_restar_negativos():
    assert restar(-5, -5) == 0

def test_multiplicar_con_negativos():
    assert multiplicar(4, -3) == -12

def test_dividir_cero_entre_numero():
    assert dividir(0, 5) == 0

def test_dividir_entradas_no_numericas():
    with pytest.raises(TypeError):
        dividir("diez", 2)