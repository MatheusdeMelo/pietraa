#inicio da loja, informar a loja e criar variaveis
#fazer tudo em inglês
print('welcome to the womens clothing store "ROZANE" ')
#criar uma função de rotina para que não precise ficar escrevendo linha
def linhas():
    print('-----------------------')
#colocar as variaveis, não vou fazer todas elas em inglês se não eu posso me confundir
valor = 0
opção = 0
Blouses = 0
Shorts = 0
Pants = 0
Dresses = 0
escolha = 0
#para dá o resultado final da compra, eu vou ter que somar os pedidos
Total = Blouses, Shorts, Pants, Dresses
#criar um laço para repetir os comandos, colocar os nomes das roupas
while escolha != 5:
    linhas()
    print('Todays clothes are: ')
    linhas()
    print('''
    1-Blouse
    2-Shorts
    3-Pants
    4-Dresses
    5-Exit''')
    linhas()
    escolha = int(input('What do you want: '))
    linhas()
    # fazer os if's (se) para cada roupa
    if escolha == 1:
        print('''
        [1] Blouse of Mickey. This blouse was sewn and worn by Waldisney's beautiful wife, because of its significant value, it's costing $300
        [2] Zebra print blouse. Because this blouse is a little simpler, the value is $20
        [3] Blouse with snowflakes. This blouse is great for christmas and thanksgiving, its fabric is comfortable and reasonably warm, its value is for $60''')
        linhas()
        opção = int(input('which one do you want? '))
        linhas()
        if opção == 1:
            blusas = 'Blouse of Mickey'
            valor += 300
        if opção == 2:
            blusas = 'Zebra print blouse'
            valor += 20
        if opção == 3:
            blusas = 'Blouse with snowflakes'
            valor += 60
    elif escolha == 2:
        print('''
        [1] Basic black shorts. It is costing $10
        [2] Short jeans tumbler. as this is in fashion it will cost a little more. It is costing $50
        [3] Short saia. It is costing $35''')
        linhas()
        opção = int(input('which one do you want? '))
        linhas()
        if opção == 1:
            shorts = 'Basic black shorts'
            valor += 10
        if opção == 2:
            shorts = 'Short tumbler'
            valor += 50
        if opção == 3:
            shorts = 'Short saia'
            valor += 35
    elif escolha == 3:
        print('''
        [1] pant jeans. It is costing $30
        [2] pant legging. It is costing $20''')
        linhas()
        opção = int(input('which one do you want? '))
        linhas()
        if opção == 1:
            calças = 'pant jeans'
            valor += 30
        if opção == 2:
            calças = 'pant legging'
            valor += 20
    elif escolha == 4:
        print('''
        [1] Prom dress. It is costing $1050
        [2] baggy dress. It is costing $25
        [3] Long dress. It is costing $40''')
        linhas()
        opção = int(input('which one do you want? '))
        linhas()
        if opção == 1:
            vestidos = 'Prom dress'
            valor += 1050
        if opção == 2:
            vestidos = 'baggy dress'
            valor += 25
        if opção == 3:
            vestidos = 'Long dress'
            valor += 40
    elif escolha == 5:
        #quebrar o laço
        break
#terminar o jogo e eu acho que vou colocar uma linha para ficar mais bonito
print(f'goodbyee! The value of this purchase was {valor}')
linhas()
#decidi colocar troco kkkkk
troco = int(input('Do you will need how much change?? '))
linhas()
print(f'You paid: {valor}, your change was: {troco}')