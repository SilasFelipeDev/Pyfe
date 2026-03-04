import random

def criar_baralho():
    naipes = ['ouro', 'paus', 'copas', 'espada']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    baralho = [(valor, naipe) for naipe in naipes for valor in valores]
    
    return baralho

meu_baralho = criar_baralho()
print(f'Total de cartas: {len(meu_baralho)}')

traducao_valores = {
    'A': 'Ás',
    'J': 'Valete',
    'Q': 'Dama',
    'K': 'Rei',
}

random.shuffle(meu_baralho)

mao_jogador = [meu_baralho.pop() for _ in range(9)]
mao_maquina = [meu_baralho.pop() for _ in range(9)] 
    
print('----------SUA MÃO--------------')
for valor, naipe in mao_jogador:
    nome_valor = traducao_valores.get(valor, valor)
    print(f'{nome_valor} de {naipe}')
print('-------------------------------')

print(f'Mão da Maquina: {len(mao_maquina)} cartas')
print('-------------------------------')

mesa = []
mesa.append(meu_baralho.pop())

topo = mesa[-1]
print(f'Carta na mesa: {topo[0]} de {topo[1]}')

print(f'Cartas restantes no baralho: {len(meu_baralho)}')

def turno_jogador():
    print('----------SUA VEZ--------------')
    print(f'Carta na mesa: {mesa[-1]}')

    escolha = input('1 - Comprar do Baralho \n2 - Comprar da mesa\nEscolha: ')

    if escolha == '1':
        carta = meu_baralho.pop()
    else:
        carta = mesa.pop()

    mao_jogador.append(carta)
    print('----------SUA MÃO--------------')
    for i, carta in enumerate(mao_jogador):
        print(i, carta)
    
    descarte = int(input('Escolha o numero da carta para descartar: '))
    carta_descartada = mao_jogador.pop(descarte)
    mesa.append(carta_descartada)
    print(f'Carta na mesa: {mesa[-1]}')

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

while True:
    turno_jogador()
    turno_maquina()