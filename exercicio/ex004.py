# Implemente um programa que leia um valor em metros e mostre seu valor em centímetros e em milímetros.

metros = float(input('Digite a quantidade em metros: '))
print('Quantidade em metros: {} \n Quantidade em centimetros: {} \n Quantidade em milimetros: {}'.format(metros,metros*100,metros*1000))
print('dm: {}, dam: {:.1f}, hm: {}, km:{}'.format(metros*10, metros*0.1, metros*0.01, metros*0.001))