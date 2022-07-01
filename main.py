
from random import randint
computador = randint(0, 5) # Faz o computador "Pensar"
print('-=-' * 20)
print("Pense em um Numero de 0 a 5. Tente adivinhar... ")
print('-=-'* 20)
jogador = int(input('em que nomero eu estou Pensando ? ')) # jogador tente adivinhar
if jogador == computador:
    print("Parabens ! voce ganhou eu pensei {} e voce tembem pensou no {} ?".format(computador,jogador))
else:
    print("Ganhei ! voce errou eu pensei no {} e nao no {} ! ".format(computador,jogador))
print("-*-" *10) 
print("FIM ")
print("-*-" * 10)
