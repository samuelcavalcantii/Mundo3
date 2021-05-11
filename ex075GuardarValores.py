#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.

#B) Em que posição foi digitado o primeiro valor 3.

#C) Quais foram os números pares.
num = int(input('Digite um valor: ')),\
      int(input('Digite um valor: ')),\
      int(input('Digite um valor: ')),\
      int(input('Digite um valor: '))
print(num)
if 9 in num:
    print(f'O valor nove aparece {num.count(9)}')
else:
    print('Número nove não foi digitado')
if 3 in num:
    print(f'O número três (3) aparece ({num.index(3)+1}ª posição')
else:
    print('Número três (3) não foi digitado.')
print('Números pares encontrados: ', end =' ')
for n in num:
    if n % 2 == 0:
        print(f'{n}',end=' ')

