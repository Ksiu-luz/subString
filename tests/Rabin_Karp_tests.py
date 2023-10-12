import unittest
from subString import Rabin_Karp_search


class Tests(unittest.TestCase):
    def test_simple_true(self):
        self.assertEqual(Rabin_Karp_search.search('логика', 'гик'), True)

    def test_simple_false(self):
        self.assertEqual(Rabin_Karp_search.search('Обеспечение', 'печень'), False)

    def test_one_symbol(self):
        self.assertEqual(Rabin_Karp_search.search('F', 'F'), True)

    def test_no_symbols_in_str(self):
        self.assertEqual(Rabin_Karp_search.search('', 'F'), False)

    def test_long_text(self):
        self.assertEqual(Rabin_Karp_search.search('Прошло уже пять сезонов, а Адриан так и не понял, '
                                                             'что Маринетт - это леди баг', 'Дебил'), False)

    def test_simple_true_md5(self):
        self.assertEqual(Rabin_Karp_search.search('логика', 'гик', Rabin_Karp_search.hash_md5), True)

    def test_simple_false_md5(self):
        self.assertEqual(Rabin_Karp_search.search('Обеспечение', 'печень',
                                                  Rabin_Karp_search.hash_md5), False)

    def test_one_symbol_md5(self):
        self.assertEqual(Rabin_Karp_search.search('F', 'F', Rabin_Karp_search.hash_md5), True)

    def test_no_symbols_in_str_md5(self):
        self.assertEqual(Rabin_Karp_search.search('', 'F', Rabin_Karp_search.hash_md5), False)

    def test_long_text_md5(self):
        self.assertEqual(Rabin_Karp_search.search('Прошло уже пять сезонов, а Адриан так и не понял, '
                                                             'что Маринетт - это леди баг', 'Дебил',
                                                  Rabin_Karp_search.hash_md5), False)

    def test_simple_true_sha1(self):
        self.assertEqual(Rabin_Karp_search.search('логика', 'гик', Rabin_Karp_search.hash_sha1), True)

    def test_simple_false_sha1(self):
        self.assertEqual(Rabin_Karp_search.search('Обеспечение', 'печень',
                                                  Rabin_Karp_search.hash_sha1), False)

    def test_one_symbol_sha1(self):
        self.assertEqual(Rabin_Karp_search.search('F', 'F', Rabin_Karp_search.hash_sha1), True)

    def test_no_symbols_in_str_sha1(self):
        self.assertEqual(Rabin_Karp_search.search('', 'F', Rabin_Karp_search.hash_sha1), False)

    def test_long_text_sha1(self):
        self.assertEqual(Rabin_Karp_search.search('Прошло уже пять сезонов, а Адриан так и не понял, '
                                                             'что Маринетт - это леди баг', 'Дебил',
                                                  Rabin_Karp_search.hash_sha1), False)


if __name__ == '__main__':
    unittest.main()
