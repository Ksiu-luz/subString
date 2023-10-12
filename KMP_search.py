def search(string, substring):
    """
    Алгоритм Кнут-Моррис-Пратт поиска подстроки в строке.
    Параметры:
        string (str): исходная строка
        substring (str): искомая подстрока
    Возвращаемое значение:
        result (bool): наличие подстроки в строке
    """
    def prefix(sub):
        """
        Возвращает массив длин префиксов подстроки для алгоритма Кнут-Моррис-Пратт.
        Параметры:
            sub (str): подстрока
        Возвращаемое значение:
            result (list): массив длин префиксов
        """
        len_sub = len(sub)
        result = [0] * len_sub
        for n in range(len_sub - 1):
            m = result[n]
            while m > 0 and sub[n] != sub[m]:
                m = result[m-1]
            if sub[n+1] == sub[m]:
                m += 1
            result[n+1] = m
        return result

    pref = prefix(substring)
    j = 0
    for i in range(len(string)):
        while j > 0 and substring[j] != string[i]:
            j = pref[j-1]
        if substring[j] == string[i]:
            j += 1
        if j == len(substring):
            return True
    return False
