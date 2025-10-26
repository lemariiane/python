#analisando nomes
nm=str(input("Digite o nome completo: ")).strip(); #strip para tirar os espaços antes e depois

print("Analisando seu nome");
print(f"Seu nome em maiúsculo: {nm.upper()}");
print(f"Seu nome em minúsculo {nm.lower()}");
print(f"Seu nome tem {len(nm)-nm.count(' ')} letras");#quantidade de letras - os espaços entre eles
print(f"Seu primeiro nome têm {nm.find(' ')}");
