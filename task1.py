import random
import time
from lru import LRUCache

def range_sum_no_cache(array, L, R):
    return sum(array[L:R+1])

def update_no_cache(array, index, value):
    array[index] = value

def range_sum_with_cache(array, L, R, cache):
    cached_value = cache.get((L, R))
    if cached_value is not None:
        return cached_value
    result = sum(array[L:R+1])
    cache.put((L, R), result)
    return result

def update_with_cache(array, index, value, cache):
    array[index] = value
    keys_to_remove = [key for key in list(cache.cache.keys()) if key[0] <= index <= key[1]]
    for key in keys_to_remove:
        cache.cache.pop(key, None)

# Генерація вхідних даних
N = 100000
Q = 50000
array = [random.randint(1, 1000) for _ in range(N)]
queries = []
for _ in range(Q):
    if random.random() < 0.7:
        L, R = sorted(random.sample(range(N), 2))
        queries.append(('Range', L, R))
    else:
        index = random.randint(0, N-1)
        value = random.randint(1, 1000)
        queries.append(('Update', index, value))

# Виконання запитів без кешу
start_time = time.time()
for query in queries:
    if query[0] == 'Range':
        range_sum_no_cache(array, query[1], query[2])
    else:
        update_no_cache(array, query[1], query[2])
time_no_cache = time.time() - start_time

# Виконання запитів з кешем
cache = LRUCache(1000)
start_time = time.time()
for query in queries:
    if query[0] == 'Range':
        range_sum_with_cache(array, query[1], query[2], cache)
    else:
        update_with_cache(array, query[1], query[2], cache)
time_with_cache = time.time() - start_time

# Вивід результатів
print(f'Час виконання без кешування: {time_no_cache:.2f} секунд')
print(f'Час виконання з LRU-кешем: {time_with_cache:.2f} секунд')
