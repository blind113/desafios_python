#print('teste')

#Desafio 13
# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
# sexo = input('Insira o seu sexo (H) ou (M) :')
# altura = float(input('Insira seu altura : '))
# if sexo == 'H' or sexo == 'h':
#     print('Peso ideal é :' , (72.7*altura) - 58)
# elif sexo == 'M' or sexo == 'm':
#     print('Peso ideal é :' ,(62.1*altura) - 44.7)
# else :
#     print('Parece que voce errou no sexo ')
    
#Desafio 14
# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
# peso = float(input('Peso do peixe: '))
# if peso > 50:
#     excesso = peso - 50 
#     multa = excesso * 4
#     print('Multado tem que pagar :', multa, ' Passou do limite por ', excesso, 'KG')
# else :
#     excesso = 0
#     multa = 0 
#     print('Mando bem, sem multa ')

#Desafio 15 
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.
# valor = float(input('Quando você recebe por hora R$:'))
# horas = float(input('Quantas horas você trabalha por mês :'))

# salario_bruto = valor * horas
# ir = salario_bruto * 0.11
# inss = salario_bruto * 0.08
# sindicato = salario_bruto * 0.05

# print('+ Salário Bruto : R$', salario_bruto)
# print('- IR (11%) : R$',ir)
# print('- INSS (8%) : R$', inss)
# print('- Sindicato ( 5%) : R$',sindicato)
# print('Total descontos : ', (ir+inss+sindicato) )
# print('= Salário Liquido : R$', (salario_bruto - (ir+inss+sindicato)))

#Desafio 16
# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
# metros_q = float(input('Quantos metros quadrados pretende pintar :'))
# if metros_q <= 54 :
#     print('Voce tem que comprar uma lata por 80 reias')
# else:
#     latas = round(metros_q/54)
#     print('Voce precisa de ', latas, 'latas Valor a pagar :', latas*80)

#Desafio 17
# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 
# ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
# cobertura_lata = 6*18
# cobertura_galao = 6*3.6
# valor_lata = 80
# valor_galao = 25
# metros_pintura = float(input('Quantos metros voce vai pintar'))

# #Gasto em latas 
# if metros_pintura <= cobertura_lata:
#     print('Voce precisa somente uma lata e vai pagar R$', valor_lata)
# else:
#     latas = round(metros_pintura/cobertura_lata)
#     print('Voce vai precisar de ', latas, 'Latas e vai pagar R$', latas*valor_lata)

# if metros_pintura <= cobertura_galao:
#     print('Voce precisa uma galao e vai pagar R$', valor_galao)
# else:
#     galao = round(metros_pintura/cobertura_galao)
#     print('Voce precisa de', galao, 'galoes e vai pagar R$', galao*valor_galao)


#Desafio 18 
# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).