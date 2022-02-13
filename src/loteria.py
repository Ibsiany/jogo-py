import random


class loteria:
    def loteriaJogo(self, sequencia):

        numeros_sorteado = []

        for valor in sequencia:
            numeros_sorteado.append(random.randint(0, 99))

        validado = []

        indice = 0

        for valor_sequencia in sequencia:
            if valor_sequencia == numeros_sorteado[indice]:
                validado.append(valor)

        indice += 1

        if (len(validado) == 4):
            print('Você ganhou 400 mil reais.')
        elif (len(validado) == 5):
            print('Você ganhou 500 mil reais.')
        elif (len(validado) == 6):
            print('Você ganhou 1 milhão de reais.')
        else:
            print('Infelizmente você não fanhou nada :/')

        print(f'O número sorteado foi {numeros_sorteado}')
