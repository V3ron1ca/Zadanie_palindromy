def palindromy(x):
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