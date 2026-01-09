nome_pessoa=[]
pessoas=[]
nome_maior=[]
nome_menor=[]
maior_peso=menor_peso=0

while True:
    nome=str(input('Digite o nome: '))
    nome_pessoa.append(nome)

    peso=float(input('Digite o peso: '))
    nome_pessoa.append(peso)
    
    pessoas.append(nome_pessoa[:])
    nome_pessoa.clear()

    cont=str(input('Deseja adicionar outra pessoa? [S/N]')).strip().upper()
    while cont not in ('S','N'):
        cont=str(input('DADO INVÁLIDO! Digite apenas "S" OU "N": ')).strip().upper()

    if len(pessoas)==1:
        maior_peso=peso
        menor_peso=peso
    
    if peso > maior_peso:
        maior_peso = peso
        nome_maior = [nome] 
    elif peso == maior_peso:
        nome_maior.append(nome) 

    if peso < menor_peso:
        menor_peso = peso
        nome_menor = [nome] 
    elif peso == menor_peso:
        nome_menor.append(nome)

    if cont=='N':
        break

print(f'Você cadastrou {len(pessoas)} pessoa(s)!')
print(f'O maior peso foi de {maior_peso}KG. Peso de {nome_maior}')
print(f'O menor peso foi de {menor_peso}KG. Peso de {nome_menor}')
