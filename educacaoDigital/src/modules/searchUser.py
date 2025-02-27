def viewUser(user):
    if not user:
        print("Não há usuários cadastrados.")
        return
    
    print("\n===== Usuários =====")
    for register in user:
        print(f"ID: {register['id']}")
        print(f"Nome: {register['nome']}")
        print(f"Idade: {register['idade']}")
        print(f"Email: {register['email']}")
        print("-" * 20)

def searchUser(user):
    if not user:
        print("Não há usuários cadastrados.")
        return
    
    nameUser = input("Digite o nome de um usuário  para buscar: ").lower()
    users = [r for r in user if nameUser in r['nome'].lower()]
    
    if users:
        print(f"\nUsuários {len(users)} encontrados:")
        for register in users:
            print(f"ID: {register['id']}")
            print(f"Nome: {register['nome']}")
            print(f"Idade: {register['idade']}")
            print(f"Email: {register['email']}")
            print("-" * 20)
    else:
        print("Nenhum usuário encontrado.")
