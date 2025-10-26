# Aluguel de carros
d=int(input("Quantos dias que o carro ficou alugado? ")); #d de dias alugados
km=float(input("Quantos km percorridos? ")); #km de quantos km foram percorridos
a=(km*0.15)+(d*60); #a de preço do aluguel

print(f"O preço para o aluguel, em que cada dia vale R$60 e cada km vale R$0.15, é de R${a}");
