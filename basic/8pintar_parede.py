# Pintar paredes
l=float(input("Digite a largura: ")); #l de largura
at=float(input("Digite a altura: ")); #at de altura
area=l*at;

print(f"Sua parede tem a dimensão {l:.2f}X{at:.2f} e sua área é de {area:.2f}m²");
print(f"Para pintar essa parede, você precisará de {area/2}L de tinta");
