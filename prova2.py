def pari(n):
    print(f"pari({n})")
    if n == 0:
        return True
    else:
        return dispari(n - 1)

def dispari(n):
    print(f"dispari({n})")
    if n == 0:
        return False
    else:
        return pari(n - 1)

# Eseguiamo con un numero
print("Risultato:", pari(5))