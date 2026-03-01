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
    
print('Sua Mão: ')
for valor, naipe in mao_jogador:
    nome_valor = traducao_valores.get(valor, valor)
    print(f'{nome_valor} de {naipe}')

print(f'Mão da Maquina: {len(mao_maquina)} cartas')

print(f'Cartas restantes no baralho: {len(meu_baralho)}')
