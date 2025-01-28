def main():
    livro = 5
    while livro > 0:
        print(f'Venda realizada! Estoque restante: {livro}')
        livro -= 1
    print('Estoque esgotado')
    
if __name__ == "__main__":
    main()