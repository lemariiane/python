#primeiro e último nome
nome=str(input("Digite o nome completo: ")).strip(); #strip para tirar os espaços antes e depois
n = nome.split(); #pega uma sequência de nomes e separa cada um deles em uma lista

print(f"Seu primeiro nome é: {n[0]}");
print(f"Seu último nome é: {n[-1]}");
