print('welcome to the womens clothing store "ROZANE" ')
def pergunta():
    return int(input('which one do you want? '))
def linhas():
    print('-----------------------')
valor = []
oi = ()
Blouses = {}
Shorts = {}
Pants = {}
Dresses = {}
escolha = {}
Total = Blouses, Shorts, Pants, Dresses
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
    if escolha == 1:
        print('''
        [1] Blouse of Mickey. This blouse was sewn and worn by Waldisney's beautiful wife, because of its significant value, it's costing $300
        [2] Zebra print blouse. Because this blouse is a little simpler, the value is $20
        [3] Blouse with snowflakes. This blouse is great for christmas and thanksgiving, its fabric is comfortable and reasonably warm, its value is for $60''')

        linhas()
        resposta = pergunta()
        linhas()
        if resposta == 1:
            Blouses['blusas'] = 'Blouse of Mickey'
            valor.append(300)
        if resposta == 2:
            Blouses['blusas'] = 'Zebra print blouse'
            valor.append(20)
        if resposta == 3:
            Blouses['blusas'] = 'Blouse with snowflakes'
            valor.append(60)
    elif escolha == 2:
        print('''
        [1] Basic black shorts. It is costing $10
        [2] Short jeans tumbler. as this is in fashion it will cost a little more. It is costing $50
        [3] Short saia. It is costing $35''')
        linhas()
        barbie = pergunta()
        if barbie == 1:
            Shorts['short'] = 'Basic black shorts'
            valor.append(10)
        if barbie == 2:
            Shorts['short'] = 'Short tumbler'
            valor.append(50)
        if barbie == 3:
            Shorts['short'] = 'Short saia'
            valor.append(35)
    elif escolha == 3:
        print('''
        [1] pant jeans. It is costing $30
        [2] pant legging. It is costing $20''')
        linhas()
        opção = pergunta()
        if opção == 1:
            Pants['calças'] = 'pant jeans'
            valor.append(30)
        if opção == 2:
            Pants['calças'] = 'pant legging'
            valor.append(20)
    elif escolha == 4:
        print('''
        [1] Prom dress. It is costing $1050
        [2] baggy dress. It is costing $25
        [3] Long dress. It is costing $40''')
        linhas()
        popcorn = pergunta()
        if popcorn == 1:
            Dresses['vestidos'] = 'Prom dress'
            valor.append(1050)
        if popcorn == 2:
            Dresses['vestidos'] = 'baggy dress'
            valor.append(25)
        if popcorn == 3:
            Dresses['vestidos'] = 'Long dress'
            valor.append(40)
    elif escolha == 5:
        break
print(f'goodbyee! The value of this purchase was {valor}')