"""Faça um programa que cadastre o estado civil de uma pessoa, entretanto, o programa deve continuar perguntando enquanto o valor informado for diferente de "solteiro" ou "casado"."""


while True:
  estado_civil = input('Digite seu estado civil: ')
  if estado_civil.lower() == 'solteiro' or estado_civil.lower() == 'Casado':
    break 
