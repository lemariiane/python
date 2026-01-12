#analizando uma matriz
matriz=[]
soma_par=soma_coluna=maior_linha=0

for l in range (0,3):
    linha=[]
    for c in range (0,3):
        num=int(input(f'Digite o valor [{l}],[{c}]: '))
        if num %2==0:
            soma_par=soma_par+num
        linha.append(num)
        if l==2:
            soma_coluna=soma_coluna+num
        if c==1:
            if maior_linha<num:
                maior_linha=num
        
    matriz.append(linha)
    


for linha in matriz:
    print(linha)

print(f'A soma dos valores pares é {soma_par}')
print(f'A soma dos valores da terceira coluna é {soma_coluna}')
print(f'O maior valor da segunda linha é {maior_linha}')
