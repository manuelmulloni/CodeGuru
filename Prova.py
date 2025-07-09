import time
import random

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

def duplicate_logic_2(numbers):
    squared = []
    for n in numbers:
        if n > 0:
            squared.append(n * n)
    return squared

# Chiamate di esempio
if __name__ == "__main__":
    print(unsafe_eval("2 + 2"))
    print(slow_loop())
    print(calculate_average([1, 2, 3]))
    print(tricky_logic([2, 4, 6, 1, 2, 2, 3]))
    print(duplicate_logic_1([1, -1, 2]))
    print(duplicate_logic_2([3, -2, 4]))
