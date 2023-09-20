class Node:
    """
    Вспомогательный класс для построения дерева, представляющий узел бора.
    Атрибуты:
    goto - словарь, содержащий дочерние узлы;
    out - список паттернов, заканчивающихся в данном узле;
    fail - ссылка на узел, который является наиболее длинной суффиксной ссылкой данного узла.
    """
    def __init__(self):
        self.goto = {}
        self.out = []
        self.fail = None


def create_ac_tree(substring):
    """
    Функция создает бор - дерево подстрок. В нашем случае, одной подстроки.
    Для подстроки происходит проход по узлам бора, начиная с корневого узла, и создание новых узлов при необходимости.
    В список out последнего узла добавляется подстрока.
    Функция возвращает корневой узел бора.
    """
    root = Node()
    node = root
    for symbol in substring:
        node = node.goto.setdefault(symbol, Node())
    node.out.append(substring)
    return root


def create_ac_statemachine(substring):
    """
    Функция создает конечный автомат Ахо-Корасика.
    Фактически создает бор и инициализирует fail-функции всех узлов, обходя дерево в ширину.
    """
    root = create_ac_tree(substring)
    nodes = [node for node in root.goto.values()]
    for node in nodes:
        node.fail = root
    while nodes:
        current_node = nodes.pop()
        for key, child_node in current_node.goto.items():
            nodes.append(child_node)
    return root


def aho_corasick_search(string, substring):
    """
    Алгоритм Ахо-Корасик для поиска подстроки в строке.
    Параметры:
        string (str): исходная строка
        substring (str): искомая подстрока
    Возвращаемое значение:
        result (bool): наличие подстроки в строке
    """
    root = create_ac_statemachine(substring)
    node = root
    for i in range(len(string)):
        while node and string[i] not in node.goto:
            node = node.fail
        node = node.goto[string[i]] if node else root
        if node.out:
            return True
    return False
