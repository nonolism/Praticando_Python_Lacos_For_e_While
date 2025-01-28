def main():
    usuario = ''
    senha = ''
    
    while (len(usuario) < 5 or len(senha) < 8):
        usuario = input('Digite seu nome de usuário: ')
        senha = input('Digite sua senha: ')
        if len(usuario) < 5:
            print('O nome de usuário deve ter pelo menos 5 caracteres')
            pass
        if len(senha) < 8:
            print('A senha deve ter pelo menos 8 caracteres.')
            pass
    
    print('Cadastro realizado com sucesso!')
    
if __name__ == "__main__":
    main()