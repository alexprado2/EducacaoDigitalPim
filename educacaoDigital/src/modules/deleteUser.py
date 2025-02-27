from modules import searchUser,jsonManager

def userDelete(user):
    if not user:
        print("Não há usuário cadastrados.")
        return
    
    searchUser.viewUser(user)
    try:
        idUserDelete = int(input("Digite o ID do usuário a ser excluído: "))
        
        id = [id for id, list in enumerate(user) if list['id'] == idUserDelete]
        
        if id:
            register = user.pop(id[0])
            jsonManager.saveUser(user)
            print(f"Usuário {register['nome']} excluído com sucesso!")
        else:
            print(f"Usuário com ID {idUserDelete} não encontrado.")
            
    except ValueError:
        print("ID inválido. Digite um número.")