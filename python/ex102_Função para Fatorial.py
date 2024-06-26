"""Crie um programa que tenha uma função fatorial() que receba
dois parâmetros: o primeiro que indique o número a calcular
e outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de
cálculo do fatorial."""


# Função fatorial
def fatorial(num, show=False):
    """
    Calcula o fatorial de um número
    :param num: o número a ser calculado
    :param show: mostrar ou não na tela
    :return: o valor do fatorial de um número
    """
    fat = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        fat *= c
    return fat


print(fatorial(5))
