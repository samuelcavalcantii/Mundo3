lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
print(lanche[1])#posiçã na tupla
print(lanche[-2])#posição a partir do fim da tupla. ex. Pudim = -1; ´Pizza = -2
print(lanche[1:3])#Fateamento da tupla. Vai do objeto 1 até o 3, desconsiderando o último
print(lanche[2:])#posições a partir da segunda posição até o fim
print(lanche)#tupla inteira
##tuplas são imutáveis
#lanche[1] = refrigerante
#print(lanche[1])# vai dar erro porque tuplas são imutáveis. Não dá pra adicionar novos objetos.
'''for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print(len(lanche)) #número de elementos na tupla'''

'''for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}') #mostra a posição do elemento na variáel lanche'''
'''for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}') #a variável cont sozinha mostra a posição do elemento'''

'''for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}') #tem o mesmo efeito do anterior'''

print(sorted(lanche)) #colocar em ordem alfabética em uma lista []
a = 2,3,4
b = 5, 8, 1, 2
c = a + b #soma as tuplas, números
print(c.count(5)) #quantas vezes aparece o número 5
print(c.index(8)) #Qual a posição do 8
pessoa = 'Samuel', 30, 'M', 99 #posso adicionar de tipos diferentes
print(pessoa)