def encontrar_livro(livros:list, livro_buscado:str):
    for livro in livros:
        if livro == livro_buscado:
            print(f'Livro encontrado: {livro}')
            break

def main():
    livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]
    livro_buscado = 'O Hobbit'
    encontrar_livro(livros,livro_buscado)

if __name__ == '__main__':
    main()