#Essa frase continua a mesma ao contrário? é um palindromo?

frase=str(input("Digite a frase: ")).strip().upper().split();#NÃO COLOCAR ACENTO

invertida=''.join(frase);
frase_final=''.join(frase);

print(f"A frase {frase_final} invertida é {invertida}");

if frase_final== invertida[::-1]:
    print("Essa frase é um palíndromo!");
else:
    print("Essa frase NÂO é um palíndromo!");
