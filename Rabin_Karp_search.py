import hashlib


def rabin_karp_search(string, substring, hash_func=hash):
    """
    Алгоритм Рабин-Карп поиска подстроки в строке с использованием произвольных типов хэширования.
    Параметры:
        string (str): исходная строка
        substring (str): искомая подстрока
    Возвращаемое значение:
        result (bool): наличие подстроки в строке
    """
    n = len(string)
    m = len(substring)

    substring_hash = hash_func(substring)
    for i in range(n - m + 1):
        spam = string[i:i + m]
        hs = hash_func(spam)
        if hs == substring_hash:
            if spam == substring:
                return True
    return False


def hash_md5(string):
    return hashlib.md5(string.encode()).hexdigest()


def hash_sha1(string):
    return hashlib.sha1(string.encode()).hexdigest()
