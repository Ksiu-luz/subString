import unittest
from subString import Aho_Corasick_search


class Tests(unittest.TestCase):
    def test_simple_true(self):
        self.assertEqual(Aho_Corasick_search.search('логика', 'гик'), True)

    def test_simple_false(self):
        self.assertEqual(Aho_Corasick_search.search('Обеспечение', 'печень'), False)

    def test_one_symbol(self):
        self.assertEqual(Aho_Corasick_search.search('F', 'F'), True)

    def test_no_symbols_in_str(self):
        self.assertEqual(Aho_Corasick_search.search('', 'F'), False)

    def test_long_text(self):
        self.assertEqual(Aho_Corasick_search.search('Прошло уже пять сезонов, а Адриан так и не понял, '
                                                                 'что Маринетт - это леди баг', 'Дебил'), False)


if __name__ == '__main__':
    unittest.main()
