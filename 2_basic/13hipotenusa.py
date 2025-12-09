# Hipotenusa
from math import sqrt;

ang1=float(input("Digite o ângulo adjacente: ")); #ang1 de ângulo 1
ang2=float(input("Digite o ângulo oposto: ")); #ang2 de ângulo 2

h=(ang1**2)+(ang2**2); #h de hipotenusa

print(f"A hipotenuza desse triângulo é {sqrt(h)}");
