#Gerenciador de pagamento
preco=float(input("Digite o preço da compra (R$): "));

print('''CONDIÇÕES DE PAGAMENTO
    [1] à vista dinheiro/cheque/pix 
    [2] à vista cartão
    [3] 2X no cartão
    [4] 3X ou mais no cartão''');

opcao=int(input("Qual opção? "));

if opcao==1:
    print(f"Sua compra irá custar R${preco-(preco*0.1):.2f} no final! Com 10% de desconto."); #10% de desconto
elif opcao==2:
    print(f"Sua compra irá custar R${preco-(preco*0.05):.2f} no final! Com 5% de desconto."); #5% de desconto
elif opcao==3:
    print(f"Sua compra foi parcelada em 2X de {preco/2:.2f}.");
    print(f"Sua compra irá custar R${preco} no final!"); #preco normal
elif opcao==4:
    parcela=int(input("Quantas parcelas? "));
    print(f"Sua compra foi parcelada em {parcela}X de R${(preco+(preco*0.2))/parcela:.2f} com juros!");
    print(f"Sua compra irá custar R${preco+(preco*0.2):.2f} no final."); #20% de juros
else:
    print("OPÇÃO INVÁLIDA de pagamento! Tente novamente!");
