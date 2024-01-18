import random

def jogar_pedra_papel_tesoura(jogada_usuario):
    opcoes = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}

    if jogada_usuario not in opcoes:
        return 'Escolha inválida: Por favor, escolha entre 1, 2 ou 3'

    jogada_computador = random.randint(1, 3)

    print(f'Você escolheu {opcoes[jogada_usuario]}.')
    print(f'O computador escolheu {opcoes[jogada_computador]}.')

    if jogada_usuario == jogada_computador:
        return 'Empate'
    elif (
        (jogada_usuario == 1 and jogada_computador == 3) or
        (jogada_usuario == 2 and jogada_computador == 1) or
        (jogada_usuario == 3 and jogada_computador == 2)
    ):
        return 'Você venceu'
    else:
        return 'Você perdeu'

try:
    entrada_usuario = int(input('Escolha 1 para Pedra, 2 para Papel ou 3 para Tesoura: '))
    resultado = jogar_pedra_papel_tesoura(entrada_usuario)
    print(resultado)
except ValueError:
    print('Entrada inválida. Por favor, insira um número inteiro.')
