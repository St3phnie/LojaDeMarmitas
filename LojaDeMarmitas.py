print('-------Bem vindo a loja de Marmitas da Stephanie Marrocos ------')
print('----------------------------Cardápio----------------------------')
print('----------------------------------------------------------------')
print('---|  Tamanho  |  Bife Acebolado(BA) |  Filé de Frango(FF)  |---')
print('---|     P     |      R$ 16.00       |        R$ 15.00      |---')
print('---|     M     |      R$ 18.00       |        R$ 17.00      |---')
print('---|     G     |      R$ 22.00       |        R$ 21.00      |---')
print('----------------------------------------------------------------')

# Tabela de preços
precos = {
    'BA': {'P': 16, 'M': 18, 'G': 22},
    'FF': {'P': 15, 'M': 17, 'G': 21}
}

# Dicionário para nomes completos dos produtos
nomes = {
    'BA': 'Bife Acebolado',
    'FF': 'Filé de Frango'
}

# Iniciar valor total
valorTotal = 0

while True:
    # Escolher sabor
    sabor = input('Selecione o sabor desejado (BA/FF):').upper()
    if sabor not in precos:
        print('Sabor inválido. Tente novamente.')
        continue

    # Escolher tamanho
    tamanho = input('Selecione o tamanho (P/M/G):').upper()
    if tamanho not in precos[sabor]:
        print('Tamanho inválido. Tente novamente.')
        continue

    # Calcular o preço do pedido atual usando modelo aninhado
    if sabor == 'BA':
        if tamanho == 'P':
            preco = precos['BA']['P']
        elif tamanho == 'M':
            preco = precos['BA']['M']
        elif tamanho == 'G':
            preco = precos['BA']['G']
    elif sabor == 'FF':
        if tamanho == 'P':
            preco = precos['FF']['P']
        elif tamanho == 'M':
            preco = precos['FF']['M']
        elif tamanho == 'G':
            preco = precos['FF']['G']

    # Exibir o pedido atual e o valor
    nome_sabor = nomes[sabor]
    print(f'Pedido: {nome_sabor} - Tamanho: {tamanho} | Preço: R$ {preco:.2f}')

    valorTotal += preco  # Adiciona valor ao pedido total

    # Perguntar se deseja pedir algo a mais
    algoMais = input('Deseja pedir algo mais? (S/N):').upper()
    if algoMais != 'S':
        break

# Mostrar valor total do pedido
print(f'O valor total a ser pago é: R$ {valorTotal:.2f}')
