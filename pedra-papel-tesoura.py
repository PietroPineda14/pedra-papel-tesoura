import random

linha = '---------------------------------------------'

print()
print(linha)
print(' Bem-vindo ao jogo, Pedra, Papel ou Tesoura!')
print(' Te apresento seu adversário, o Ted!!')

# Menu de escolha do usuário
print(linha)
print('                     MENU')
print(linha)
print(' [1] Pedra')
print(' [2] Papel')
print(' [3] Tesoura')
print(linha)
escolha = input(' Qual sua escolha? ')

if escolha == '1':
    escolha = 'Pedra'
elif escolha == '2':
    escolha = 'Papel'
elif escolha == '3':
    escolha = 'Tesoura'
else:
    print(' Sua escolha é inválida.')
    escolha = input(' Escolha novamente: ')
    if escolha == '1':
        escolha = 'Pedra'
    elif escolha == '2':
        escolha = 'Papel'
    elif escolha == '3':
        escolha = 'Tesoura'

print(linha)
print()
print(linha)
print('                  PREPARE-SE!')
print(linha)
print(' 3..   2..   1..   JÁ!')
print()

# Opções disponíveis para o computador
opcoes = ['Pedra', 'Papel', 'Tesoura']
# Escolhe uma opção aleatória
computador = random.choice(opcoes)

print(linha)
print('                  RESULTADO')
print(linha)
print(f' Escolha do Ted: {computador}')
print(f' Sua escolha: {escolha}')
if escolha == 'Pedra' and computador == 'Tesoura':
    print(' O vencedor é você!')
elif escolha == 'Papel' and computador == 'Pedra':
    print(' O vencedor é você!')
elif escolha == 'Tesoura' and computador == 'Papel':
    print(' O vencedor é você!')
elif escolha == computador:
    print(' O jogo deu empate!')
else:
    print(' O vencedor é o Ted!')
print(linha)
print()