import json
import os

def loadUser():
    if os.path.exists('user.json'):
        try:
            with open('user.json', 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo. Criando um novo banco de usuários.")
            return []
    else:
        return []

def saveUser(user):
    with open('server.json', 'w', encoding='utf-8') as arquivo:
        json.dump(user, arquivo, indent=4, ensure_ascii=False)
    print("Usuário salvo com sucesso!")