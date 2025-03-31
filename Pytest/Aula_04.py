import pytest

#Funções
def soma(a, b):
    return a + b

def subtracao(a,b):
    return a - b

def divisao(a,b):

    if b == 0:
        raise ValueError("Impossível realizar a operação")
    return a/b

def multiplicacao(a,b):
    return a * b

#Testes unitários
def test_soma_positivo():
    assert soma(2, 3) == 5

def test_soma_negativo():
    assert soma(-1, -2) == -3

def test_subtacao():
    assert subtracao(1,2) == -1

def test_divisao():
    assert divisao(10,5) == 2

def test_multiplicacao():
    assert multiplicacao(4,5) == 20

