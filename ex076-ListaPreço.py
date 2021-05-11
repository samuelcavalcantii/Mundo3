#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
listagem = 'Lápis', 1.75,'Caderno', 15.90,'Folha A4', 40.00,'Lapiseira', 10.90, 'Estojo', 25
print(listagem)
print(len(listagem)) #QUANTIDADE DE ITENS NA TUPLA
print('-'*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-'*40)
for item in range (0, len(listagem)): #para saber a posição na lista
   if item % 2 ==0: #Volta a posição par na lista
       print(f'{listagem[item]:.<30}', end= ' ') #volta o item na lista de acordo com a posição
   else:
       print(f'R${listagem[item]:.2f}')