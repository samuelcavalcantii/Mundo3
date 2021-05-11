#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
from time import sleep
num = randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10)
print(f'Os números sorteados foram {num}')
print(f'O número máximo foi {max(num)}\nO mínimo foi {min(num)}')