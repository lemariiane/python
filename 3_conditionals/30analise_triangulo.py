#analisando o triângulo. Formam ou não um triângulo?
lado1=float(input("Digite o primeiro lado: "));
lado2=float(input("Digite o segundo lado: "));
lado3=float(input("Digite o terceiro lado: "));

if lado1+lado2>lado3 and lado1+lado3>lado2 and lado3+lado2>lado1: #soma de quaisquer dos dois lados tem que ser maior que o terceiro
     print("Esses lados FORMAM um triângulo!");
else:
     print("Essas medidas NÃO formam um triângulo!");
