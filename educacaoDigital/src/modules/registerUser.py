from modules import jsonManager

def addUser(user):
    name = input("Nome: ")
    age = input("Idade: ")
    email = input("Email: ")
    
    newRegister = {
        "id": len(user) + 1,
        "nome": name,
        "idade": age,
        "email": email
    }
    
    user.append(newRegister)
    jsonManager.saveUser(user)
    print(f"Usuário {name} adicionado com sucesso!")


