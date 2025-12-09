# #Analisando frase com a letra 'A'

frase= str(input("Digite a frase contendo a letra 'a': ")).upper().strip();#strip para tirar os espaços antes e depois

print(f"A sua frase tem {frase.count("A")} letra's a's.");
print(f"A letra 'a' aparece pela primeira vez no índice {frase.find("A")+1}");
print(f"A última letra 'a' apareceu na posição {frase.rfind("A")+1}"); #tem a questão dos espaçoes entre as palavras 
