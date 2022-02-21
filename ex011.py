L = float(input('Qual a largura da parede? '))
H = float(input('Qual a altura da parede? '))
Tamanho = L * H
Tinta = Tamanho / 2
print ('A sua parede tem {}m de largura e {}m de altura, que totaliza {}m². Você precisa de {} Litros de tinta para pintar ela completamente'.format(L,H,Tamanho,Tinta))