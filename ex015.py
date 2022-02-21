kminicial = float(input('Insira a km inicial: '))
kmatual = float(input('insira a km atual: '))
dias = int(input('Quantos dias ficou alugado? '))
kmpercorrido = kmatual - kminicial
rkm = kmpercorrido * 0.15
rdias = dias * 60
total = rkm+rdias

print ('O total de km percorrido foi: {}. A quantidade de dias utilizado foi: {}, que resultou no valor de R$: {}'.format(kmpercorrido,dias,total))

