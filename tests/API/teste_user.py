import requests


url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}


def teste_incluir_usuario():
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '2846522'

    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('C:\\Users\\lhvil\\PycharmProjects\\134inicial\\vendors\\json\\user1.json')
    )

    corpo_do_resultado_obtido = resultado_obtido.json()

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == codigo_esperado
    assert corpo_do_resultado_obtido['type'] == tipo_esperado
    assert corpo_do_resultado_obtido['message'] == mensagem_esperada


def teste_login():
    username = 'juca'
    password = 'bala'

    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = 'logged in user session'

    resultado_obtido = requests.get(
        url=f'{url}/login?username={username}&password={password}',
        headers=headers,
    )

    corpo_do_resultado_obtido = resultado_obtido.json()

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == codigo_esperado
    assert corpo_do_resultado_obtido['type'] == tipo_esperado
    assert mensagem_esperada.find(corpo_do_resultado_obtido['message'])

    mensagem_extraida = corpo_do_resultado_obtido.get('message')
    print(f'O token: {mensagem_extraida}')
