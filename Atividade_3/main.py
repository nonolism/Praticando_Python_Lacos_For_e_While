def exibir_mensagem(mensagem:str, quantidade:int):
    while quantidade > 0:
        print(mensagem)
        quantidade -= 1

def main():
    exibir_mensagem('Bem-vindo ao Buscante!', 5)
    
if __name__ == '__main__':
    main()