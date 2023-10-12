def search(string, substring):
    """
    Алгоритм полного перебора строки для поиска подстроки.
    Параметры:
        string (str): исходная строка
        substring (str): искомая подстрока
    Возвращаемое значение:
        result (bool): наличие подстроки в строке
    """
    substr_len = len(substring)
    n = len(string) - substr_len + 1
    for i in range(n):
        if string[i: i + substr_len] == substring:
            return True
    return False

