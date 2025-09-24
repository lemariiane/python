pal = input('Digite algo: ');
print ('O tipo é', type(pal));
print ('Só tem espaços?',pal.isspace());
print ('É um número?', pal.isnumeric());
print ('Tem letra?', pal.isalpha());
print ('Tem número e letra?', pal.isalnum());
print ('Está em maiúsculo?', pal.isupper());
print ('Está em minúsculo?', pal.islower());
print ('Está capitalizada?', pal.istitle());