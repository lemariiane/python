
tipo_conta=input('BInforme seu tipo de conta Pessoal(P) ou Empresarial(E) [P/E]: ').strip();#strip() para ignorar os espaços em branco

while tipo_conta not in('P','p','E','e'):
        tipo_conta=input('Dados inválidos! Digite "P" ou "E": ');

print(f'Conta {tipo_conta} cadastrada com sucesso!');
