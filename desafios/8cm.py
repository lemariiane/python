m = float(input('Digite o comprimento em metros: '));

cm = m * 100;
mm= m* 1000;

print ('Metro:',m,'m');
print ('Centimetro: {:.0f} cm'.format(cm));
print ('Milimetro: {:.0f} mm'.format(mm));