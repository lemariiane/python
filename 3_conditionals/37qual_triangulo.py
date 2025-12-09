#Analisando triângulos. Qual triângulo esses segmentos formam?
lado1=int(input("Digite o primeiro lado: "));
lado2=int(input("Digite o segundo lado: "));
lado3=int(input("Digite o terceiro lado: "));

if lado1+lado2>lado3 and lado1+lado3>lado2 and lado3+lado2>lado1:
    print("O triângulo foi formado!");

    if lado1==lado2==lado3:
        print("Esses segmentos formam um triângulo EQUILÁTERO!");
    elif lado1!=lado2!=lado3:
        print("Esses segmentos formam um triângulo ESCALENO!");
    else:
        print("Esses segmentos formam um triângulo ISÓSCELES!");

else:
    print("Esses segmentos NÃO formam um triângulo!");
