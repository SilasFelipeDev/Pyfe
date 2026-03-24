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

def turno_jogador():
    print('----------SUA VEZ--------------')
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
        carta = meu_baralho.pop()
    elif escolha == 2:
        carta = mesa.pop()

    mao_jogador.append(carta)
    print('----------SUA MÃO--------------')
    for i, carta in enumerate(mao_jogador):
        print(f'[{i}] {formatar_carta(carta)}')

    while True:
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
        carta = meu_baralho.pop()
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

print(f'Cartas restantes no baralho: {len(meu_baralho)}')

while True:
    turno_jogador()
    turno_maquina()