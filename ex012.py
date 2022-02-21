valor = float(input('digite o valor do produto para proceder o desconto: '))
desconto = float(input('Digite o valor em percentual do desconto: '))
total = valor-(valor*desconto)/100
print('O valor de {}, com desconto de {}, totaliza {}'.format(valor,desconto,total))