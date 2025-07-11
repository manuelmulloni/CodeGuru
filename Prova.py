import time
import random

def conta_parole_da_input(percorso):
    file = open(percorso, 'r')  # RISCHIO: input non validato + risorsa non protetta
    contenuto = file.read()
    parole = contenuto.split()
    file.close()
    return len(parole)

def unsafe_eval(user_input):
    # Potenziale vulnerabilità: CodeGuru dovrebbe segnalarla
    return eval(user_input)

def duplicate_logic_2(numbers):
    squared = []
    for n in numbers:
        if n > 0:
            squared.append(n * n)
    return squared




# Funzione con pratica non ottimale: uso non sicuro di eval()
def unsafe_eval(user_input):
    # Potenziale vulnerabilità: CodeGuru dovrebbe segnalarla
    return eval(user_input)

# Funzione con sleep e uso inutile di loop (inefficiente)
def slow_loop():
    total = 0
    for i in range(100000):
        time.sleep(0.00001)  # Introduce lentezza senza utilità
        total += i
    return total

# Funzione ben scritta (nessuna raccomandazione qui)
def calculate_average(values):
    if not values:
        return 0
    return sum(values) / len(values)

# Funzione volutamente difficile da analizzare per CodeGuru
def tricky_logic(data):
    result = []
    i = 0
    while i < len(data):
        if data[i] % 2 == 0:
            j = i
            while j < len(data) and data[j] % 2 == 0:
                j += 1
            result.append((i, j))
            i = j
        else:
            i += 1
    return result

# Codice duplicato (CodeGuru potrebbe segnalarlo)
def duplicate_logic_1(numbers):
    squared = []
    for n in numbers:
        if n > 0:
            squared.append(n * n)
    return squared

def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n - 1)

def A(n):
    if n <= 0:
        return "A"
    return B(n - 1)

def B(n):
    if n <= 0:
        return "B"
    return C(n - 1)

def C(n):
    if n <= 0:
        return "C"
    return A(n - 1)

def is_positive(n):
    return not is_negative(n)

def is_negative(n):
    return not is_zero(n) and not is_positive(n - 1)

def is_zero(n):
    return n == 0

if __name__ == "__main__":
    print("is_even(4):", is_even(4))
    print("A(5):", A(5))
    print("is_positive(2):", is_positive(2))