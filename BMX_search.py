def search(string, substring):
    """
    Алгоритм Бойер-Мур-Хорспул для поиска подстроки в строке.
    Параметры:
        string (str): исходная строка
        substring (str): искомая подстрока
    Возвращаемое значение:
        result (bool): наличие подстроки в строке
    """
    string_len = len(string)
    substring_len = len(substring)
    if substring_len > string_len:
        return False

    # формируем таблицу смещения
    offset_table = {}
    for i in range(256):
        offset_table[chr(i)] = substring_len

    # добавляем кириллицу
    for i in range(1025, 1106):
        offset_table[chr(i)] = substring_len

    for i in range(substring_len - 1):
        offset_table[substring[i]] = substring_len - i - 1
    i = substring_len - 1
    j = i
    k = i
    while j >= 0 and i <= string_len - 1:
        j = substring_len - 1
        k = i
        while j >= 0 and string[k] == substring[j]:
            k -= 1
            j -= 1
        i += offset_table[string[i]]
    if k >= string_len - substring_len:
        return False
    else:
        return True
