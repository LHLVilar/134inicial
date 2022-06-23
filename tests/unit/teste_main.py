import parametrize as parametrize
import pytest

from main import somar, dividir, subtrair, multiplicar

def ler_csv(arquivo_csv):
    dados_csv = []
    try:
        with open(arquivo_csv, newline='') as massa:
            import csv
            campos = csv.reader(massa, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {arquivo_csv}')
    except Exception as fail:
        print(f'Falha não prevista: {fail}')

lista_de_valores = [
    (8, 7, 15),
    (20, 30, 50),
    (25, 0, 25),
    (-5, 12, 7),
    (6, -3, 3)
]

def teste_somar_leitura_de_lista(numero_a, numero_b, resultado_esperado):
    resultado_obtido = somar(numero_a, numero_b)
    assert resultado_obtido == resultado_esperado

@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', ler_csv('C:\\Users\\lhvil\\PycharmProjects\\134inicial\\vendors\\csv\\massa_teste_somar_positivo.csv'))
def teste_somar_leitura_de_csv(numero_a, numero_b, resultado_esperado):
    resultado_obtido = somar(int(numero_a), int(numero_b))
    assert resultado_obtido == int(resultado_esperado)

def testar_somar():
    numero_a = 10
    numero_b = 5
    resultado_esperado = 15
    resultado_obtido = somar(numero_a, numero_b)
    assert resultado_obtido == resultado_esperado

def testar_dividir_positivo():
    numero_a = 10
    numero_b = 5
    resultado_esperado = 2
    resultado_obtido = dividir(numero_a, numero_b)
    assert resultado_obtido == resultado_esperado

def testar_dividir_negativo():
    numero_a = 10
    numero_b = 0
    resultado_esperado = 2
    resultado_obtido = dividir(numero_a, numero_b)
    assert resultado_obtido == resultado_esperado

def testar_subtrair():
    numero_a = 10
    numero_b = 5
    resultado_esperado = 5
    resultado_obtido = subtrair(numero_a, numero_b)
    assert resultado_obtido == resultado_esperado

def testar_multiplicar():
    numero_a = 10
    numero_b = 5
    resultado_esperado = 50
    resultado_obtido = multiplicar(numero_a, numero_b)
    assert resultado_obtido == resultado_esperado