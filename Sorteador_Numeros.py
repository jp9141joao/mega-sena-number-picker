import random
import time
import os

os.system('cls')
Qntd = int(input('Quantos jogos deseja sortear\nR: '))

Ganhos = 0
Quinas = 0
Quadras = 0
Triplas = 0

Vencedor = str(input('Digite o numero do jogo vencedor com espaços\nExp: "10 20 30 40 50 60"\nR: '))
Vencedor = Vencedor.split()
Vencedor = [int(numero) for numero in Vencedor]
Vencedor = sorted(Vencedor)


if len(Vencedor) != 6:
    print('Jogo vencedor invalido!')

for i in range(6):
    Cont = 0
    for j in range(6):
        if Vencedor[i] == Vencedor[j]:
            Cont += 1
        
    if Cont == 2:
        print('Jogo vencedor invalido!')
        break

Sequencia = []    

for i in range(Qntd):
    Layout = f'{(i+1):05d}) '
    Jogo = []
    Acertos = 0

    while True:
        for i in range(6): 
            while True:
                Numb = random.randint(1,60)
                if Numb not in Jogo:
                    Jogo.append(Numb)
                    break
        
        Ordem = sorted(Jogo)

        if Jogo not in Sequencia:
            Sequencia.append(Jogo)
            break
    
    for i in range(6):
        if Ordem[i] in Vencedor:
            Acertos += 1

    if Acertos == 3:
        Triplas += 1
    elif Acertos == 4:
        Quadras += 1
    elif Acertos == 5:
        Quinas += 1
    
    if Ordem == Vencedor:
        Ganhos += 1
    
    if Acertos >= 3:
        for i in range(6):
            Layout += f' {Ordem[i]:02d}'

        Layout += f' | Acertos: {Acertos}'
        
        print(Layout)



print(f'\nNumero de jogos ganhos: {Ganhos}\nNumero de quinas {Quinas}\nNumero de quadras: {Quadras}\nNumero de Triplas: {Triplas}')