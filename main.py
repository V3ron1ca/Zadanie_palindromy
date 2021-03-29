def palindromy(x):
    x = x.lower()
    if x == x[::-1]:
        return True
    return False
slowo = "Potop"
funkcja = palindromy(slowo)
if (funkcja):
    print("Tak")
else:
    print("Nie")
