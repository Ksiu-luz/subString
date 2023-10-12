import time
import tracemalloc
import matplotlib.pyplot as plt
import Aho_Corasick_search
import Bruteforce_search
import KMP_search
import Rabin_Karp_search


def get_data(method):
    """
        Возвращает массив времени от длины строки
        Параметры:
            method (method): метод поиска подстроки в строке
        Возвращаемое значение:
            [x, y] ([]): x - массив длин строк,
                         y - массив времени
    """
    x, y = [], []
    for i in range(10, 100000, 10000):
        k = 0
        summ = 0
        for j in range(1, i, 10000):
            start = time.time()
            method('a' * i, 'a' * j + 'b')
            end = time.time()
            summ += ((end - start) * 10 ** 3)
            k += 1
        x.append(i)
        y.append(summ / k)

    return [x, y]


def get_memory(method):
    x, y = [], []
    for i in range(10, 10000, 1000):
        k = 0
        summ = 0
        for j in range(1, i, 1000):
            tracemalloc.start()
            method('a' * i, 'a' * j + 'b')
            summ += tracemalloc.get_traced_memory()[1]
            k += 1
        x.append(i)
        y.append(summ / k)

    return [x, y]


def get_graph(method):
    x, y = get_data(method.search)
    # График времени
    plt.subplot(211)
    plt.plot(x, y)
    plt.xlabel('Длина строки')
    plt.ylabel('Время, мс')
    # График памяти
    plt.subplot(212)
    plt.plot(x, y)
    plt.xlabel('Длина строки')
    plt.ylabel('Память')

    plt.show()


def graphs():
    k = 1
    for module in [Bruteforce_search, Aho_Corasick_search, Rabin_Karp_search, KMP_search]:
        # График времени
        x, y = get_data(module.search)
        plt.subplot(5, 2, k)
        plt.plot(x, y)
        plt.xlabel('Длина строки')
        plt.ylabel('Время, мс')
        # График памяти
        x, y = get_memory(module.search)
        plt.subplot(5, 2, k+1)
        plt.plot(x, y)
        plt.xlabel('Длина строки')
        plt.ylabel('Память')
        k += 2
    plt.show()
