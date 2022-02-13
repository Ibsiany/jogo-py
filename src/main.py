from .loteria import loteria


def main():
    sequencia = input('Informe uma sequência de 6 digitos separados por - \n')

    lista = sequencia.split('-')

    jogo = loteria()

    if len(lista) == 6:
        jogo.loteriaJogo(lista)
    else:
        print('Sequência inválida!')
