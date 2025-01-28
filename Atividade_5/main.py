def exibir_projetos(projetos:list):
    for projeto in projetos:
        if projeto:
            print(projeto)
        else:
            print('Projeto ausente')

def main():
    projetos = ['website', 'jogo', 'análise de dados', None, 'aplicativo móvel']
    exibir_projetos(projetos)
    
if __name__ == '__main__':
    main()