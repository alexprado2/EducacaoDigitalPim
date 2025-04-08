import json
import os
from datetime import datetime

class SystemBooks:
    def __init__(self, file_json='books.json'):
        self.file_json = file_json
        self.books = self.load_books()
    
    def load_books(self):  #Carrega os livros do file JSON.
        if os.path.exists(self.file_json):
            try:
                with open(self.file_json, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Erro ao ler o arquivo JSON. Criando um novo banco de dados.")
                return []
        return []
    
    def save_books(self): # Salva os livros no arquivo JSON.
        with open(self.file_json, 'w', encoding='utf-8') as file:
            json.dump(self.books, file, indent=4, ensure_ascii=False)
        print("Dados salvos com sucesso!")
    
    def generate_id(self): # Gera um novo ID para um livro.
        if not self.books:
            return 1
        return max(book['id'] for book in self.books) + 1
    
    def add_books(self, title, author, year_publication, gender, description=None): # Adiciona um novo livro ao sistema.
        new_book = {
            'id': self.generate_id(),
            'title': title,
            'author': author,
            'year_publication': year_publication,
            'gender': gender,
            'description': description,
            'registration_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.books.append(new_book)
        self.save_books()
        return new_book
    
    def list_books(self): # Lista todos os livros cadastrados.
        if not self.books:
            print("Não há books cadastrados.")
            return []
        return self.books
    
    def books_by_id(self, id_book): # Busca um livro pelo ID.
        for book in self.books:
            if book['id'] == id_book:
                return book
        return None
    
    def books_by_title(self, search): # Busca livros pelo título.
        return [book for book in self.books if search.lower() in book['title'].lower()]
    
    def books_by_author(self, search): # Busca livros pelo autor.
        return [book for book in self.books if search.lower() in book['author'].lower()]
    
    def update_book(self, id_book, **updated): # Atualiza um livro existente.
        book = self.books_by_id(id_book)
        if not book:
            print(f"Livro com ID {id_book} não encontrado.")
            return None
        
        # Atualiza apenas os campos fornecidos
        for campo, valor in updated.items():
            if campo in book and valor is not None:
                book[campo] = valor
        
        book['update_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save_books()
        return book
    
    def remove_book(self, id_book): # Remove um livro pelo ID.
        book = self.books_by_id(id_book)
        if not book:
            print(f"Livro com ID {id_book} não encontrado.")
            return False
        
        self.books.remove(book)
        self.save_books()
        print(f"Livro '{book['title']}' removido com sucesso!")
        return True


def menu(): # Exibe o menu de opções do sistema.
    print("\n===== SISTEMA DE GERENCIAMENTO DE LIVROS =====")
    print("1. Adicionar livro")
    print("2. Listar todos os livros")
    print("3. Buscar livro por ID")
    print("4. Buscar livro por título")
    print("5. Buscar livro por autor")
    print("6. Atualizar livro")
    print("7. Remover livro")
    print("0. Sair")
    print("==============================================")
    return input("Escolha uma opção: ")


def display_books(book): # Exibe os detalhes de um livro de forma formatada.
    print("\n--- Detalhes do livro ---")
    print(f"ID: {book['id']}")
    print(f"Título: {book['title']}")
    print(f"Autor: {book['author']}")
    print(f"Ano de Publicação: {book['year_publication']}")
    print(f"Gênero: {book['gender']}")
    if book.get('description'):
        print(f"Descrição: {book['description']}")
    print(f"Data de Cadastro: {book.get('registration_date', 'N/A')}")
    if book.get('update_date'):
        print(f"Última Atualização: {book['update_date']}")
    print("-------------------------")


def main():
    system = SystemBooks()
    
    while True:
        opc = menu()
        
        if opc == '1':  # Adicionar livro
            print("\n--- Adicionar Novo Livro ---")
            title = input("Título: ")
            author = input("Autor: ")
            
            while True:
                try:
                    year = int(input("Ano de Publicação: "))
                    break
                except ValueError:
                    print("Por favor, digite um ano válido.")
            
            gender = input("Gênero: ")
            description = input("Descrição: (opcional, pressione Enter para pular): ")
            
            description = description if description else None
            new_book = system.add_books(title, author, year, gender, description)
            print(f"\nLivro '{new_book['title']}' adicionado com sucesso! ID: {new_book['id']}")
        
        elif opc == '2':  # Listar todos os livros
            print("\n--- Lista de livros ---")
            books = system.list_books()
            for book in books:
                print(f"ID: {book['id']} | Título: {book['title']} | Autor: {book['author']} | Ano: {book['year_publication']}")
        
        elif opc == '3':  # Buscar livro por ID
            try:
                id_book = int(input("\nDigite o ID do livro: "))
                book = system.books_by_id(id_book)
                if book:
                    display_books(book)
                else:
                    print(f"Livro com ID {id_book} não encontrado.")
            except ValueError:
                print("ID inválido. Por favor, digite um número.")
        
        elif opc == '4':  # Buscar livro por título
            search = input("\nDigite o título ou parte do título: ")
            books = system.books_by_title(search)
            if books:
                print(f"\nEncontrados {len(books)} livro(s):")
                for book in books:
                    print(f"ID: {book['id']} | Título: {book['title']} | Autor: {book['author']}")
            else:
                print(f"Nenhum livro encontrado com o título contendo '{search}'.")
        
        elif opc == '5':  # Buscar livro por autor
            search = input("\nDigite o nome do autor ou parte do nome: ")
            books = system.books_by_author(search)
            if books:
                print(f"\nEncontrados {len(books)} book(s):")
                for book in books:
                    print(f"ID: {book['id']} | Título: {book['title']} | Autor: {book['author']}")
            else:
                print(f"Nenhum livro encontrado com autor contendo '{search}'.")
        
        elif opc == '6':  # Atualizar livro
            try:
                id_book = int(input("\nDigite o ID do livro a ser atualizado: "))
                book = system.books_by_id(id_book)
                
                if not book:
                    print(f"Livro com ID {id_book} não encontrado.")
                    continue
                
                print("\n--- Atualizar livro ---")
                print("(Deixe em branco para manter o valor atual)")
                
                display_books(book)
                
                updated = {}
                
                new_title = input(f"Novo título [{book['title']}]: ")
                if new_title:
                    updated['title'] = new_title
                
                new_author = input(f"Novo autor [{book['author']}]: ")
                if new_author:
                    updated['author'] = new_author
                
                new_year = input(f"Novo ano de publicação [{book['year_publication']}]: ")
                if new_year:
                    try:
                        updated['year_publication'] = int(new_year)
                    except ValueError:
                        print("Ano inválido. Este campo não será atualizado.")
                
                new_gender = input(f"Novo gênero [{book['gender']}]: ")
                if new_gender:
                    updated['gender'] = new_gender
                
                new_description = input(f"Nova descrição [{book.get('description', 'N/A')}]: ")
                if new_description:
                    updated['description'] = new_description
                
                if updated:
                    book_atualizado = system.update_book(id_book, **updated)
                    print("Livro atualizado com sucesso!")
                    display_books(book_atualizado)
                else:
                    print("Nenhuma alteração realizada.")
            
            except ValueError:
                print("ID inválido. Por favor, digite um número.")
        
        elif opc == '7':  # Remover livro
            try:
                id_book = int(input("\nDigite o ID do livro a ser removido: "))
                book = system.books_by_id(id_book)
                
                if book:
                    confirmacao = input(f"Tem certeza que deseja remover o livro '{book['title']}'? (s/n): ")
                    if confirmacao.lower() == 's':
                        system.remove_book(id_book)
                else:
                    print(f"Livro com ID {id_book} não encontrado.")
            
            except ValueError:
                print("ID inválido. Por favor, digite um número.")
        
        elif opc == '0':  # Sair
            print("\nSaindo do sistema. Até logo!")
            break
        
        else:
            print("\nOpção inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    main()