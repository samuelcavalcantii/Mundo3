'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
cont = 'zero','um', 'dois', 'três', 'quatro','cinco','seis','sete','oito','nove','dez', 'onze','doze','treze','quatorze','quinze', 'dezesseis','dezessete','dezoito','dezenove','vinte'

while True:
    numero = int(input('Digite um número de 0 - 20: '))

    if 0<= numero <= 20:
        print(f'Você digitou o número {cont[numero]}')
        resp = ' '
        while resp not in 'SN':
            resp = str(input('Voce quer continuar?')).upper()
        if resp == 'N':
            break
    else:
        numero = int(input('Digite um número de 0 - 20: '))
print('FIM')




