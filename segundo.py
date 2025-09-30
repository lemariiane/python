import math; #importando bibliotecas
from math import sqrt; # raiz quadrade 
# #python.org
import random #pegar elemento aleatório

# import emoji

# # Usando a função emojize para adicionar um emoji
# print(emoji.emojize("Python é :snake: e eu amo :pizza:!"))

# raiz quadrada
# num = math.sqrt(49);

# soma
# print (num);

# n1= int(input("Digite um número: "))
# n2= int(input("Digite outro número: "))

# print(f"A soma entre {n1} e {n2} é igual á {n1+n2}")

# sucessor e antecessor
# n= int(input("Digite um número: "))

# print(f"Seu antecessor é {n-1} e seu sucessor é {n+1}")

# triplo do número e raiz quadrada
# n = int(input("Digite um número: "))

# print(f"Seu dobro é {n*2}\nSeu triplo é {n*3}\nSua raiz quadrada é {n**(1/2)}")


# média de notas
# n1= float(input("Digite a primeira nota:"))
# n2=float(input("Digite a segunda nota:"))

# print (f"O valor da média entre {n1} e {n2} é {(n1+n2)/2:.2f}")

# tabuada
# n= int(input("Digite o número da tabuada desejada:"))
# for i in range(11):
#     print(f"{n} X {i} = {n*i}")


# Conversor de moedas
# r = float(input("Digite o valor em reais(R$): "))
# d= 5.40
# print(f"Com R${r:.2f} você consegue comprar U${r/d:.2f}")

# Pintar paredes
# l=float(input("Digite a largura: "));
# at=float(input("Digite a altura: "));
# area=l*at;

# print(f"Sua parede tem a dimensão {l:.2f}X{at:.2f} e sua área é de {area:.2f}m²");
# print(f"Para pintar essa parede, você precisará de {area/2}L de tinta");

# Desconto para um produto
# p= float(input("Digite o preço do produto : "));
# d= (p*5)/100;
# print (f"O produto com 5% de desconto ficou R${p-d}");

# Aumento de 15% no salário
# s=float(input("Digite o salário: "));
# aum=(s*15)/100;
# print(f"O salário com o aumento de 15% ficou R${s+aum}");

# # Conversor de °C para °F
# tempc=float(input("Digite a temperatura em °C: "));
# print(f"O valor {tempc}C°, em Fahrenheit fica {(tempc*1.8)+32}");

# Aluguel de carros
# d=int(input("Quantos dias que o carro ficou alugado? ")); 
# km=float(input("Quantos km percorridos? "));
# a=(km*0.15)+(d*60);
# print(f"O preço para o aluguel, em que cada dia vale R$60 e cada km vale R$0.15, é de R${a}");

# Hipotenusa
# ang1=float(input("Digite o ângulo adjacente: ")); #ang1== ãngulo 1
# ang2=float(input("Digite o ângulo oposto: "));
# h=(ang1**2)+(ang2**2);
# print(f"A hipotenuza desse triângulo é {sqrt(h)}");

# seno cosseno tangente
# ang1=float(input("Digite o ângulo desejado: ")); #ang1 é de 'ângulo 1'

# print(f"O valor do seno é {math.sin(ang1)}");
# print(f"O valor do cosseno é {math.cos(ang1)}");
# print(f"O valor da tangente é {math.tang(ang1)}");

# sortteio entre 4 pessoas
nm1=str(input("Digite o primeiro nome: ")); #nm é de 'nome' 1
nm2=str(input("Digite o segundo nome: "));
nm3=str(input("Digite o terceiro nome: "));
nm4=str(input("Digite o quarto nome: "));

lista=[nm1,nm2,nm3,nm4];
escolhido=random.choice(lista);

print (f"O nome escolhido foi {escolhido}");