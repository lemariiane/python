#Multa de velocidade
km=float(input("Qual a sua velocidade? "));

if km<80: #80km/hr é o limite de velocidade
    print("Pode seguir!!! Sua velocidade está dentro do permitido!");
else:
    print(f"Multado, você ultrapassou o limite de velocidade e recebeu uma multa de R${(km-80)*7}"); #7 reais para cada km acima do permitido

print("Tenha um bom dia! Dirija com segurança!!");
