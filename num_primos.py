num=int(input('Digite o número: '));
divi=0;

for i in range(1,num+1):
    print(i, end=" - ");
    i+=1;
    if num % i==0:
        divi+=1;
        
if divi==2:
    print('Esse número é primo!');
else:
    print('Esse número não é primo');
