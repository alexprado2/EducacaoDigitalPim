from modules import jsonManager,menuRegisterUsers,registerUser,searchUser,deleteUser

def main():
    print("Bem-vindo ao Gerenciador de Usuários!")
    user = jsonManager.loadUser()
    
    while True:
        opcao = menuRegisterUsers.loadMenu()
        
        if opcao == '1':
            registerUser.addUser(user)
        elif opcao == '2':
            searchUser.viewUser(user)
        elif opcao == '3':
            searchUser.searchUser(user)
        elif opcao == '4':
            deleteUser.userDelete(user)
        elif opcao == '5':
            print("Obrigado por usar o cadastro de usuários. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()