from typing import Callable
from timeit import timeit

from hometask03_search_alg import kmp_search, boyer_moore_search, rabin_karp_search


def read_file(filename):
    with open(filename, 'r', encoding='cp1251') as f:
        return f.read()

def benchmark(func: Callable, text_: str, pattern_: str):
    setup_code = f'from __main__ import {func.__name__}'
    statement = f'{func.__name__}(text, pattern)'
    return timeit(stmt=statement, setup=setup_code, globals={'text': text_, 'pattern': pattern_}, number=10)

def main():
    # Робимо пошук у першій статті
    print('Стаття:  ВИКОРИСТАННЯ АЛГОРИТМІВ У БІБЛІОТЕКАХ МОВ ПРОГРАМУВАННЯ')
    results = []
    real_pattern = 'шуканого'
    fake_pattern = 'відродження історичного спадку'
    text = read_file('стаття 1.txt')
    
    #print(boyer_moore_search(text,real_pattern))
    #print(boyer_moore_search(text,fake_pattern))

    for pattern in (real_pattern, fake_pattern):
        time = benchmark(boyer_moore_search, text, pattern)
        results.append((boyer_moore_search.__name__, pattern, time))

        time = benchmark(kmp_search, text, pattern)
        results.append((kmp_search.__name__, pattern, time))

        time = benchmark(rabin_karp_search, text, pattern)
        results.append((rabin_karp_search.__name__, pattern, time))

    print()
    title = f"{'Алгоритм':^20} | {'Строка пошуку':^40} | {'Час виконання, сек':^20}"
    print(title)
    print('-'*len(title))
    for result in results:
        print(f'{result[0]:^20} | {result[1]:<40} | {result[2]:^20}')

    # Робимо пошук у другій статті
    print()
    print('Стаття:  Методи та структури даних для реалізації бази даних рекомендаційної системи соціальної мережі')
    results = []
    real_pattern = 'порівняння часу'
    fake_pattern = 'марс вийшов на постійний '
    text = read_file('стаття 2.txt')
    
    #print(text)
    #print(boyer_moore_search(text,real_pattern))
    #print(boyer_moore_search(text,fake_pattern))

    for pattern in (real_pattern, fake_pattern):
        time = benchmark(boyer_moore_search, text, pattern)
        results.append((boyer_moore_search.__name__, pattern, time))

        time = benchmark(kmp_search, text, pattern)
        results.append((kmp_search.__name__, pattern, time))

        time = benchmark(rabin_karp_search, text, pattern)
        results.append((rabin_karp_search.__name__, pattern, time))

    print()
    title = f"{'Алгоритм':^20} | {'Строка пошуку':^40} | {'Час виконання, сек':^20}"
    print(title)
    print('-'*len(title))
    for result in results:
        print(f'{result[0]:^20} | {result[1]:<40} | {result[2]:^20}')


if __name__ == '__main__':
    main()