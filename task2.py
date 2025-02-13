import timeit
import matplotlib.pyplot as plt
from functools import lru_cache
from sortedcontainers import SortedDict

# Реалізація обчислення чисел Фібоначчі з LRU-кешем
@lru_cache(maxsize=None)
def fibonacci_lru(n):
    if n < 2:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)

# Реалізація Splay Tree
class SplayTree:
    def __init__(self):
        self.tree = SortedDict()
    
    def insert(self, key, value):
        self.tree[key] = value
    
    def find(self, key):
        return self.tree.get(key, None)

def fibonacci_splay(n, tree):
    if n < 2:
        return n
    if (result := tree.find(n)) is not None:
        return result
    result = fibonacci_splay(n - 1, tree) + fibonacci_splay(n - 2, tree)
    tree.insert(n, result)
    return result

# Параметри тестування
fib_values = list(range(0, 951, 50))
num_repeats = 5

lru_times = []
splay_times = []

for n in fib_values:
    tree = SplayTree()
    
    lru_time = timeit.timeit(lambda: fibonacci_lru(n), number=num_repeats) / num_repeats
    splay_time = timeit.timeit(lambda: fibonacci_splay(n, tree), number=num_repeats) / num_repeats
    
    lru_times.append(lru_time)
    splay_times.append(splay_time)

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(fib_values, lru_times, marker='o', label='LRU Cache')
plt.plot(fib_values, splay_times, marker='x', label='Splay Tree')
plt.xlabel('Число Фібоначчі (n)')
plt.ylabel('Середній час виконання (секунди)')
plt.title('Порівняння часу виконання для LRU Cache та Splay Tree')
plt.legend()
plt.grid()
plt.show()

# Виведення таблиці результатів
print(f"{'n':<10}{'LRU Cache Time (s)':<20}{'Splay Tree Time (s)'}")
print("-" * 50)
for i in range(len(fib_values)):
    print(f"{fib_values[i]:<10}{lru_times[i]:<20.8f}{splay_times[i]:.8f}")
