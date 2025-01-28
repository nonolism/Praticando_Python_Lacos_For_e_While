def main():
    for segundo in range(10, 0, -1):
        if segundo % 2 == 0:
            print(f'Faltam apenas {segundo} segundos - Não perca essa oportunidade!')
        if segundo % 2 != 0:
            print(f'A contagem continua: {segundo} segundos restantes.')
    
    print('Aproveite a promoção agora!')
    
if __name__ == "__main__":
    main()