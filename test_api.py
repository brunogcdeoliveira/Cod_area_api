import unittest

from main import busca_ddd_uf, busca_uf


class TestApi(unittest.TestCase):
    def test_busca_ddd_uf(self):
        assert busca_ddd_uf("RS") == [
            {'regiao': 'Porto Alegre', 'ddd': 51},
            {'regiao': 'Pelotas', 'ddd': 53},
            {'regiao': 'Caxias do Sul', 'ddd': 54},
            {'regiao': 'Santa Maria', 'ddd': 55}
        ]
        # OUTRA FORMA
        # self.assertEqual(
        #     busca_ddd_uf("RS"),
        #     [
        #         {'regiao': 'Porto Alegre', 'ddd': 51},
        #         {'regiao': 'Pelotas', 'ddd': 53},
        #         {'regiao': 'Caxias do Sul', 'ddd': 54},
        #         {'regiao': 'Santa Maria', 'ddd': 55}
        #     ]
        # )

    def test_busca_ddd(self):
        assert busca_ddd_uf("RS") == [
            {'regiao': 'Porto Alegre', 'ddd': 51},
            {'regiao': 'Pelotas', 'ddd': 53},
            {'regiao': 'Caxias do Sul', 'ddd': 54},
            {'regiao': 'Santa Maria', 'ddd': 55}
        ]

    def test_busca_uf(self):
        assert busca_uf(51) == {
            "ddd_recebido": 51,
            "uf": "RS",
            "regiao": "Porto Alegre"
        }