

lista1 = [2, 5, 4, 8, 9, 11, 10, 12]


def kivalasztas_tetele(lista_kivalasztas):
    talalat = False
    index = 0
    while not talalat:
        if lista_kivalasztas[index] % 3 == 0:
            talalat = True
        index = index + 1

    print('A hárommal osztható szám indexe a listában: ', index-1)








kivalasztas_tetele(lista1)


