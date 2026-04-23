import random

traducoes = {
    'A': 'Ás',
    'J': 'Valete',
    'Q': 'Dama',
    'K': 'Rei',
}

def criar_baralho():
    naipes = ['ouro', 'paus', 'copas', 'espada']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    baralho = [(valor, naipe) for naipe in naipes for valor in valores]
    
    return baralho

def traduzir_valor(valor):
    return traducoes.get(valor, valor)

def formatar_carta(carta): 
    valor, naipe = carta
    nome_valor = traduzir_valor(valor)
    return f'{nome_valor} de {naipe}'

def comprar_do_baralho():
    global meu_baralho, mesa

    if len(meu_baralho) == 0:
        print('O Baralho acabou! Embaralhando cartas da mesa ...')

        ultima_carta_mesa = mesa.pop()
        meu_baralho = mesa[:]
        random.shuffle(meu_baralho)
        mesa = [ultima_carta_mesa]

        #estudar melhor essa parte
        if len(meu_baralho) == 0:
            print('Não há mais cartas disponíveis!')
            return None
    return meu_baralho.pop()

def reorganizar_mao():
    print('\n--------REORGANIZAR MÃO---------')

    while True:
        print('Sua mão atual:')
        for i, carta in enumerate(mao_jogador):
            print(f'[{i}] {formatar_carta(carta)}')

        print('\nOrganize sua mão digitando dois números (ex 0 -> 3) ou [s] para sair:')
        entrada = input('> ').strip().lower()

        if entrada == 's':
            break

        try:
            partes = entrada.split()

            if len(partes) != 2:
                print('Digite exatamente dois números separados por espaço!')
                continue
            
            i, j = int(partes[0]), int(partes[1])

            if not (0 <= i < len(mao_jogador)) or not (0 <= j < len(mao_jogador)):
                print(f'Índices devem estar entre 0 e {len(mao_jogador) - 1}!')
                continue

            if i == j: 
                print('Escolha dois índices diferentes!')
                continue

            mao_jogador[i], mao_jogador[j] = mao_jogador[j], mao_jogador[i]
            print(f'Trocado: [{i}] <=> [{j}]\n')

        except ValueError:
            print('Digite apenas números válidos!')

def turno_jogador():
    print('----------SUA VEZ--------------')
    print(f'Cartas restantes no baralho: {len(meu_baralho)}')
    print(f'Carta na mesa: {formatar_carta(mesa[-1])}')

    while True:
        try:
            escolha = int(input('1 - Comprar do Baralho \n2 - Comprar da mesa\nEscolha: '))
            
            if escolha not in [1, 2]:
                print('Digite apenas [1] ou [2]!')
                continue
            break
        except ValueError:
            print('Você precisa digitar um NÚMERO válido!')

    if escolha == 1:
        carta = comprar_do_baralho()
    elif escolha == 2:
        carta = mesa.pop()

    mao_jogador.append(carta)
    print('----------SUA MÃO--------------')
    for i, carta in enumerate(mao_jogador):
        print(f'[{i}] {formatar_carta(carta)}')

    while True:
        while True:
            print('\n Deseja reorganizar suas cartas? [s/n]')
            reorganizar = input('> ').strip().lower()

            if reorganizar == 's':
                reorganizar_mao()
                break
            elif reorganizar == 'n':
                break
            else: 
                print('Digite apenas [s] ou [n]!')

        try:
            descarte = int(input('Escolha o numero da carta para descartar: '))

            if not 0 <= descarte < len(mao_jogador):
                print('!!!DIGITE UM ÍNDICE CORRETO!!!')
                continue
            break
        except ValueError:
            print('DIGITE UM NÚMERO VÁLIDO')

    carta_descartada = mao_jogador.pop(descarte)
    mesa.append(carta_descartada)
    print(f'Carta na mesa: {formatar_carta(mesa[-1])}')

def turno_maquina():
    print('--------VEZ DA MÁQUINA---------')
    if random.choice([True, False]) and mesa:
        carta = mesa.pop()
        print('Máquina Comprou da Mesa')
    else:
        carta = comprar_do_baralho()
        print('Máquina comprou do Baralho')

    mao_maquina.append(carta)

    descarte = random.randint(0, len(mao_maquina)-1)
    carta_descartada = mao_maquina.pop(descarte)

    mesa.append(carta_descartada)
    print('Máquina Descartou uma carta.')

meu_baralho = criar_baralho()
print(f'Total de cartas: {len(meu_baralho)}')
random.shuffle(meu_baralho)

mao_jogador = [meu_baralho.pop() for _ in range(9)]
mao_maquina = [meu_baralho.pop() for _ in range(9)] 
    
print('----------SUA MÃO--------------')
for i, carta in enumerate(mao_jogador):
    print(f'[{i}] {formatar_carta(carta)}')
print('-------------------------------')

print(f'Mão da Maquina: {len(mao_maquina)} cartas')
print('-------------------------------')

mesa = []
mesa.append(meu_baralho.pop())

print(f'Carta na mesa: {formatar_carta(mesa[-1])}')

while True:
    turno_jogador()
    turno_maquina()