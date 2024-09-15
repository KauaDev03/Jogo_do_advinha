tentativas = 1
numeroSecreto = 7
print('Bem-vindo ao jogo do advinha!')
print('Você possui 3 tentativas')
while tentativas <= 3:
    print(f'{tentativas}º tentativa(s)')
    escolha = int(input('Digite um número entre 1 e 10: '))
    if escolha >=1 and escolha <=10:
        if escolha == numeroSecreto:
            if tentativas == 1:
                print(f'\033[32mVocê acertou o número secreto na {tentativas}º tentativa\033[m')
                break
            else:
                print(f'\033[32mVocê acertou o número secreto na {tentativas}º tentativas\033[m')
                break
        else:
            tentativas+=1
            print('--------------------------------')
    else:
        print('Número Inválido!')

if tentativas > 3:
    print('\033[31mGame over! Acabaram suas tentativas.\033[m')
    print(f'O número secreto é {numeroSecreto}')
