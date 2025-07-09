# 1. Somma di una lista con un ciclo inefficiente
def somma_lista(nums):
    total = 0
    for i in range(len(nums)):
        total += nums[i]  # Inefficienza: usare sum(nums)
    return total


# 2. Ricerca dei numeri pari con controllo ridondante
def trova_pari(nums):
    risultati = []
    for num in nums:
        if num % 2 == 0:
            risultati.append(num)
        else:
            continue  # Ridondante: può essere rimosso
    return risultati


# 3. Calcolo ricorsivo di Fibonacci con ricorsione duplicata
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Ripetizione non ottimizzata


# 4. Conteggio parole in un file senza contesto with
def conta_parole(file_path):
    file = open(file_path, 'r')  # Possibile perdita di risorsa: usare 'with'
    contenuto = file.read()
    parole = contenuto.split()
    file.close()
    return len(parole)


# 5. Incremento concorrente senza lock (race condition)
import threading

class Contatore:
    def __init__(self):
        self.valore = 0

    def incrementa(self):
        for _ in range(100000):
            self.valore += 1  # Accesso non thread-safe

contatore = Contatore()

thread1 = threading.Thread(target=contatore.incrementa)
thread2 = threading.Thread(target=contatore.incrementa)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Valore finale (non deterministico):", contatore.valore)


# 6. Mutua ricorsione tra pari e dispari
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

print("Risultato:", pari(5))
def conta_parole_da_input(percorso):
    file = open(percorso, 'r')  # RISCHIO: input non validato + risorsa non protetta
    contenuto = file.read()
    parole = contenuto.split()
    file.close()
    return len(parole)