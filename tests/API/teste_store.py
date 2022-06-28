import requests


url = 'https://petstore.swagger.io/v2/store/order'
headers = {'Content-Type': 'application/json'}


def teste_vender_pet():
    status_code_esperado = 200
    pedido_id_esperado = 250205
    pet_id_esperado = 2958522
    status_pedido_esperado = 'placed'

    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('C:\\Users\\lhvil\\PycharmProjects\\134inicial\\vendors\\json\\store1.json')
    )

    corpo_do_resultado_obtido = resultado_obtido.json()

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pedido_id_esperado
    assert corpo_do_resultado_obtido['petId'] == pet_id_esperado
    assert corpo_do_resultado_obtido['status'] == status_pedido_esperado
