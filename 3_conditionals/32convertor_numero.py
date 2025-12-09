#conversor de números
num=int(input("Digite um número inteiro: "));#num de número

print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''');

opcao=int(input('Sua opção: '));

if opcao==1:
    print(f"{num} convertido em BINÁRIO é {bin(num)[2:]}"); #Se não tivesse os '[2:]', no terminal apareceria: '0o55'
elif opcao==2:
    print(f"{num} convertido em OCTAL é {oct(num)}[2:]"); #'[2:]' é para pular as duas primeiras possições e aparecer só da 2 a diante (só números)
elif opcao==3:
    print(f"{num} convertido em HEXADECIMAL é {hex(num)[2:]}");
else:
    print("Digite uma opção válida!");
