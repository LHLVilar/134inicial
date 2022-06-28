# bibliotecas
import pytest
import requests
from tests.utils.file_manager import ler_csv


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
    pet_id = '2958522'  # Tem que ser string porque vai no endereço url
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


def teste_excluir_pet():
    # Entradas/Resultado Esperado
    pet_id = '2958522'
    status_code_esperado = 200
    type_esperado = 'unknown'
    message_esperada = '2958522'

    # Executar/Resultado Obtido
    resultado_obtido = requests.delete(
        url=url + '/' + pet_id,
        headers=headers
    )
    # Validar
    corpo_do_resultado_obtido = resultado_obtido.json()
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido["code"] == status_code_esperado
    assert corpo_do_resultado_obtido["type"] == type_esperado
    assert corpo_do_resultado_obtido["message"] == message_esperada


@pytest.mark.parametrize('pet_id, category_id, category_name, pet_name, tags_id, tags_name, status', ler_csv(
    'C:\\Users\\lhvil\\PycharmProjects\\134inicial\\vendors\\csv\\massa_incluir_pet.csv'))
def teste_incluir_pet_massa(pet_id, category_id, category_name, pet_name, tags_id, tags_name, status):
    # Dados de entrada vem do arquivo massa_incluir_pet
    # Os dados de entrada são os resultados esperados pois é a inclusão dos dados
    # e o código 200 confirma que deu certo
    status_code_esperado = 200

    # Json dinâmico
    corpo_json = '{'
    corpo_json += f'"id": {pet_id},'
    corpo_json += '"category": {'
    corpo_json += f'"id": {category_id},'
    corpo_json += f'"name": "{category_name}"'
    corpo_json += '},'
    corpo_json += f'"name": "{pet_name}",'
    corpo_json += '"photoUrls": ['
    corpo_json += '"string"'
    corpo_json += '],'
    corpo_json += '"tags": ['
    corpo_json += '{'
    corpo_json += f'"id": {tags_id},'
    corpo_json += f'"name": "{tags_name}"'
    corpo_json += '}'
    corpo_json += '],'
    corpo_json += f'"status": "{status}"'
    corpo_json += '}'

    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=corpo_json
    )

    corpo_do_resultado_obtido = resultado_obtido.json()
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == int(pet_id)
    assert corpo_do_resultado_obtido['name'] == pet_name
    assert corpo_do_resultado_obtido['category']['name'] == category_name
    assert corpo_do_resultado_obtido['tags'][0]['name'] == tags_name

