lista = []
mulheres = []
media = []
acima_da_media = []
contador = 0
while True:
    nome = input('qual o seu nome: ')
    sexo = input('qual é o seu sexo?? m/f: ')
    idade = int(input('quantos anos vc tem: '))
    pessoas = input(' alguem mais?? sim ou não: ')
    if sexo == 'f':
        mulheres.append(nome[contador])
    if pessoas == 'não':
        break
cadastros = []

lista.append(nome)
lista.append(sexo)
lista.append(idade)
print(lista)
print(f'a quantidade de pessoas cadastradas é: {cadastros}')
print(f' a media de idade foi: {media}')
print(f'as mulheres cadastradas foram: {mulheres}')
print(f'as pessoas com idade acima da media foram: {acima_da_media}')
#print(nome.len)