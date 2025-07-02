def somma_lista(nums):
    total = 0
    for i in range(len(nums)):
        total += nums[i]
    return total


def trova_pari(nums):
    risultati = []
    for num in nums:
        if num % 2 == 0:
            risultati.append(num)
        else:
            continue
    return risultati

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def conta_parole(file_path):
    file = open(file_path, 'r')
    contenuto = file.read()
    parole = contenuto.split()
    file.close()
    return len(parole)

import threading

class Contatore:
    def __init__(self):
        self.valore = 0

    def incrementa(self):
        for _ in range(100000):
            self.valore += 1

contatore = Contatore()

thread1 = threading.Thread(target=contatore.incrementa)
thread2 = threading.Thread(target=contatore.incrementa)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(contatore.valore)