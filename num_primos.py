num=int(input('Digite o número: '));
divi=0;

for i in range(1,num+1):
    print(i, end=" - ");    
    if num % i==0:
        divi+=1;
        
if divi==2:
    print('\nEsse número é primo!');
else:
    print('\nEsse número não é primo');
