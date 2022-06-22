from main import somar, dividir, subtrair, multiplicar

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