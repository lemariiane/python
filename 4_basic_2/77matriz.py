#Gerando uma matriz 3X3
matriz = []

for l in range(0, 3):
    linha = [] 
    for c in range(0, 3):
        num = int(input(f'Digite o valor para [{l}, {c}]: '))
        linha.append(num) 
    matriz.append(linha) 
    
print("-" * 30)
for linha in matriz:
    print(linha)
print('Volte sempre!')
