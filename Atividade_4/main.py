def soma(receitas):
    total = 0
    for receita in receitas:
        total = total + receita
        
    print(f'A soma total das receitas é: {total}')

def main():
    valores = [10, 20, 30, 40, 50]
    soma(valores)
    
    
if __name__ == '__main__':
    main()