
# Recebe o valor n e imprime n linas e n colunas 
def leitor(n):
    aux = 1
    while aux <= n :
        for num in range(aux) :
            print(num+1, end="")
        print()
        aux +=1
# Recebe 3 parametros recebe a soma dos 3 paramentros 
def soma3(n1,n2,n3):
    return n1+n2+n3

def comparador(valor):
    result =''
    if (valor > 0):
        result = 'P'
    elif (valor <= 0):
        result = 'N'
    return result

#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto 
#sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
def somaImposto(taxaImposto, custo):
    custoFinal = custo + custo * (taxaImposto/100)
    return custoFinal

# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. 
# A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. 
# Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. 
# Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. 
# Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
def converteHora(hora, intervalo):
    horaAlterada = 0
    if(intervalo == 'P' or intervalo == 'p' ):
        #transforma hora
        horaAlterada = hora - 12
    else:
        horaAlterada = hora
    return horaAlterada 
def horaAlterada(hora, min, intervalo):
    if(intervalo == 'P' or intervalo == 'p' ):
        intervalo = 'PM'
    else:
        intervalo = 'AM'
    print('{0}:{1} - {2}'.format(hora,min, intervalo))

while True:
    hora = int(input('digite a hora :'))
    min = int(input('Digite os minutos :'))
    intervalo = input('A para intervamo da manha P para tarde : ')
    horaAlterada(converteHora(hora,intervalo), min , intervalo)

#n2 = int(input('digite o valor a imprimir '))
#-1
# n3 = int(input('digite o valor a imprimir '))
#leitor(n)
#print(soma3(n1,n2,n3))
#print(comparador(n1))
#print(somaImposto(n1,n2))
