while True:
    print('Os conteudos da aula de hoje são: ')
    print('''
    1- print
    2- while
    3- variavel
    4- função
    5- listas, tuplas e dicionarios
    6- sair''')
    pergunta = int(input(' qual desses vc quer estudar hj?? '))
    print('----------------------------------------------------------')
    if pergunta == 1:
        print('R: O print é uma função que serve para vc imprimir algo ')
        print('--------------------------------------------------------')
    elif pergunta == 2:
        print('R: O while é uma estrutura de repetição que serve como um lupe, para usalo é só escrever: "while True".')
        print('--------------------------------------------------------')
    elif pergunta == 3:
        print('R: uma variavel serve para vc guardar algo dentro, para usala é só colocar: variavel(qualquer palavra) =, esse simbulo(=) serve para receber algo')
        print('--------------------------------------------------------')
    elif pergunta == 4:
        print('R: as funções são qualquer palavras que fecham ou abrem um paratenses. por exemplo: função() ')
        print('--------------------------------------------------------')
    elif pergunta == 5:
        print('R: As tuplas são usadas com esse simbulo (), elas são imutaveis. Listas são usadas com esse simbulo [], elas diferentimente das tuplas são mutaveis. já os dicionarios são usados com esse simbulo {}, elas são mutaveis tbm')
        print('--------------------------------------------------------')
    else:
        print('Vc saiu, obriigada por jogar')
        break