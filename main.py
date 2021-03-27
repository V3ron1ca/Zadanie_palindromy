def palindromy(x):
    """
    tworzymy funkcje "palindoromy",
    wpisujemy zmienną l oznaczającą długość podanego słowa
    tworzymy pętle rozczytującą wyraz od początku a potem od końca
    jeśli słowo czytane od początku nie jest takie samo jak czytane od końca to wyskakuje return false
    jeśli jest takie samo to return true
    zmienna slowo przechowuje dany wyraz który nastepnie wprowadzony jest do funkcji
    jesli podany wyraz zgadza sie z założeniem funkcji wyskakuje "Tak"
    natomiast jak wyraz nie jest rozpoznany jako palindrom to dostajemy informacje "Nie"
    :param x:
    :return:
    """
    l = len(x)
    for p in range (l-1):
        if x[p] != x[l-1-p]:
            return False
    return True
slowo = "potop"
funkcja = palindromy(slowo)
if (funkcja):
    print("Tak")
else:
    print("Nie")