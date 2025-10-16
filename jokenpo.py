import random;
from time import sleep;
print("JOGO DE PEDRA, PAPEL E TESOURA")
print("-"*30);
print('''Escolha uma jogada: 
      [1] PEDRA
      [2] PAPEL
      [3] TESOURA''');

jogador=int(input("Qual opção você escolhe jogar? "));#jogador escolhe qual joga
opcoes={1: "Pedra", 2:"Papel", 3:"Tesoura"};#dicionário de opções

if jogador not in opcoes:
    print("Esse número de jogada NÃO É VÁLIDO! Tente novamente.");
else:
    print("JO")
    sleep(0.6)
    print("KEN")
    sleep(0.6)
    print("PO")
    sleep(1)
    computador=random.choice([1,2,3]);#computador escolhe uma opção aleatória

    print("_"*30);
    print(f"Você jogou {opcoes[jogador]}");#se o jogador escolher 1: vai aparecer 'pedra', pois está de acordo com o dicionário de opções
    print(f"O computador jogou {opcoes[computador]}");
    print("¨"*30);

    if jogador==computador:
        print("EMPATE!!!");
    elif jogador==1 and computador==3 or jogador==2 and computador==1 or jogador==3 and computador==2: #pedra(1) ganha da tesoura(3) / papel(2) ganha da pedra(1)/ tesoura(3) ganha papel(2)/ 
        print("PARABÉNS, VOCÊ GANHOU!!!");
    else:
        print("Infelizmente, VOCÊ PERDEU!!!");
