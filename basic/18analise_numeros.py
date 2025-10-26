#analisando números
n=int(input("Informe o número para ánalise: ")); #n de número

u= n // 1 % 10; #u de unidade
d= n//10 % 10; #d de decimal
c= n//100 % 10; #c de centena
m= n//1000 % 10; #m de milhar

print(f"A unidade: {u}");
print(f"A dezena: {d}");
print(f"A centena: {c}");
print(f"O milhar: {m}");
