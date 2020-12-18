import unittest
import requests

class SuitTest(unittest.TestCase):
    """Test if CRUD's working
    Warning: keep in mind that once you've run this script, the majority of tests will fail and you will need to delete the file feiras.db
    """
    def test_getting(self):
        """
        Makes a request and then verify if all is working fine
        """
        request = requests.get("http://127.0.0.1:5000/api/1.0.0/get", json={"distrito": "ARTUR ALVIM", "regiao05": "Leste", "nomeFeira": "JARDIM COIMBRA", "bairro": "JD COIMBRA"})
        self.assertEqual(request.status_code, 200)
        self.assertTrue(request.ok)
        self.assertEqual(request.json(), {'areaPonderacao': 3550308005146, 'bairro': 'JD COIMBRA', 'codigoDistrito': 5, 'codigoSubprefeitura': 21, 'distrito': 'ARTUR ALVIM', 'id': 24, 'latitude': -23531381, 'logradouro': 'RUA PITAGORAS', 'longitude': -46479045, 'nomeFeira': 'JARDIM COIMBRA', 'numero': '579.000000', 'referencia': 'RUA CLAUDIO BARTOLOMEU', 'regiao05': 'Leste', 'regiao08': 'Leste 1', 'registro': '3082-1', 'setorCensitario': 355030805000045, 'subprefeitura': 'PENHA'})
    def test_posting(self):
        """
        Test by creating and then see whether it was created or not
        """
        post = requests.post("http://127.0.0.1:5000/api/1.0.0/post", json={"id": 1637, "longitude": -2736377, "latitude": -9283910, "setorCensitario": 82937393729, "areaPonderacao": 62937383, "codigoDistrito": 87, "distrito": "UJC Columbia", "codigoSubprefeitura": 820, "subprefeitura": "kom", "regiao05": "nepal", "regiao08": "diamante", "nomeFeira": "komintern", "registro": 7200, "logradouro": 7292639737, "numero": "829-65", "bairro": "Parantes", "referencia": "aparecida"})
        self.assertTrue(post.ok)
        self.assertEqual(post.json(), {"message": "ok"})
        self.assertEqual(post.status_code, 200)
    def test_patching(self):
        """
        Updates a resource and see whether it was updated
        """
        right_patch = requests.patch("http://127.0.0.1:5000/api/1.0.0/update", json={"longitude": 223378, "latitude": 72293738, "setorCensitario": 62738383, "areaPonderacao": "628727w7", "codigoDistrito": 8, "distrito": "SP", "codigoSubprefeitura": 0, "subprefeitura": "uklaine", "regiao05": "foo", "regiao08": "bar", "nomeFeira": "déia", "logradouro": 6273, "numero": 8, "bairro": "Átila", "referencia": "TV aberta", "id": 24, "registro": "3082-1"})
        wrong_patch = requests.patch("http://127.0.0.1:5000/api/1.0.0/update", json={"longitude": 223378, "latitude": 72293738, "setorCensitario": 62738383, "areaPonderacao": "628727w7", "codigoDistrito": 8, "distrito": "SP", "codigoSubprefeitura": 0, "subprefeitura": "uklaine", "regiao05": "foo", "regiao08": "bar", "nomeFeira": "déia", "logradouro": 6273, "numero": 8, "bairro": "Átila", "referencia": "TV aberta", "id": 24, "registro": "3082-41"})
        self.assertEqual(right_patch.json(), {"message": "ok"})
        self.assertEqual(wrong_patch.json(), {"message": "error"})
        self.assertEqual(wrong_patch.status_code, 400)
        self.assertTrue(right_patch.ok)
        self.assertFalse(wrong_patch.ok)
        get = requests.get("http://127.0.0.1:5000/api/1.0.0/get", json={"distrito": "SP", "regiao05": "foo", "nomeFeira": "déia", "bairro": "Átila"})
        self.assertEqual(get.json(), {'areaPonderacao': '628727w7', 'bairro': 'Átila', 'codigoDistrito': 8, 'codigoSubprefeitura': 0, 'distrito': 'SP', 'id': 24, 'latitude': 72293738, 'logradouro': '6273', 'longitude': 223378, 'nomeFeira': 'déia', 'numero': '8', 'referencia': 'TV aberta', 'regiao05': 'foo', 'regiao08': 'bar', 'registro': '3082-1', 'setorCensitario': 62738383, 'subprefeitura': 'uklaine'})
        self.assertTrue(get.ok)
    def test_deleting(self):
        """
        Delete a resource and makes a request to make grant that it was deleted
        """
        get = requests.get("http://127.0.0.1:5000/api/1.0.0/get", json={"distrito": "PIRITUBA", "regiao05": "Norte", "nomeFeira": "JARDIM SANTA MONICA", "bairro": "JARDIM SANTA MONICA"})
        self.assertTrue(get.ok)
        delete = requests.delete("http://127.0.0.1:5000/api/1.0.0/delete", json={"id": 872, "bairro": "JARDIM SANTA MONICA"})
        self.assertTrue(delete.ok)
        get = requests.get("http://127.0.0.1:5000/api/1.0.0/get", json={"distrito": "PIRITUBA", "regiao05": "Norte", "nomeFeira": "JARDIM SANTA MONICA", "bairro": "JARDIM SANTA MONICA"})
        self.assertFalse(get.ok)

if __name__ == '__main__':
    unittest.main()
