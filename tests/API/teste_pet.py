# bibliotecas
import pytest
import requests

# variável pública (maneira de otimizar o trbalho, pois serão utilizadas em vários lugares)
url = "https://petstore.swagger.io/v2/pet"
headers = {"Content-Type": "application/json"}

# definições (defs)
def teste_incluir_pet():
    # Entradas/Resultado Esperado
    status_code_esperado = 200
    pet_id_esperado = 2958522
    pet_nome_esperado = "Nina"
    pet_nome_categoria_esperado = "cachorro"
    pet_tag_esperado = "vacinado"

    # Executa/Resultado Obtido
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open("C:\\Users\\lhvil\\PycharmProjects\\134inicial\\vendors\\json\\pet1.json")
    )

    # Valida
    corpo_do_resultado_obtido = resultado_obtido.json()
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido["id"] == pet_id_esperado
    assert corpo_do_resultado_obtido["name"] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_tag_esperado


def teste_consultar_pet():
    # Entrada
    pet_id = '2958522' # Tem que ser string porque vai no endereço url
    # Resultados Esperados
    status_code_esperado = 200
    pet_id_esperado = 2958522
    pet_nome_esperado = "Nina"
    pet_nome_categoria_esperado = "cachorro"
    pet_tag_esperado = "vacinado"

    # Executa
    resultado_obtido = requests.get(
        url=url + '/' + pet_id,
        headers=headers
    )

    # Valida
    corpo_do_resultado_obtido = resultado_obtido.json()
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido["id"] == pet_id_esperado
    assert corpo_do_resultado_obtido["name"] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_tag_esperado

def teste_alterar_pet():
    # Entradas/Resultado Esperado
    status_code_esperado = 200
    pet_id_esperado = 2958522
    pet_nome_esperado = "Nina"
    pet_nome_categoria_esperado = "cachorro"
    pet_tag_esperado = "vacinado"
    pet_status_esperado = 'pending'

    # Executa/Resultado Obtido
    resultado_obtido = requests.put(
        url=url,
        headers=headers,
        data=open("C:\\Users\\lhvil\\PycharmProjects\\134inicial\\vendors\\json\\pet2.json")
    )

    # Valida
    corpo_do_resultado_obtido = resultado_obtido.json()
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido["id"] == pet_id_esperado
    assert corpo_do_resultado_obtido["name"] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_tag_esperado
    assert corpo_do_resultado_obtido["status"] == pet_status_esperado
