import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    """ maksukortti.py testaukset"""

    def setUp(self):
        """ Jokaiseen testiin alustetaan korttil 10.00 eurolla"""
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        """ kortti on olemassa testeille """
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa(self):
        """ kortti luodaan oikein """
        self.assertEqual(str(self.maksukortti),
                         "Kortilla on rahaa 10.00 euroa")

    def test_lataa_rahaa(self):
        """ kortille ladataan oikea summa """
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(str(self.maksukortti),
                         "Kortilla on rahaa 15.00 euroa")

    def test_lataa_rahaa_neg(self):
        """ varmistetaan ettei neg. rahoja voi lisata """
        with self.assertRaises(ValueError):
            self.maksukortti.lataa_rahaa(-500)

    def test_ota_rahaa_saldo_vahenee_oiein(self):
        """ kortilta vahenee oikea summa """
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_ota_rahaa_saldo_ei_neg(self):
        """ kortin saldo ei voi menna negatiiviseksi """
        self.maksukortti.ota_rahaa(2000)
        self.assertNotEqual(str(self.maksukortti),
                            "Kortilla on rahaa -10.00 euroa")

    def test_ota_rahaa_true(self):
        """ ota_rahaa palauttaa True, jos otto onnistuu """
        self.assertTrue(self.maksukortti.ota_rahaa(500))

    def test_ota_rahaa_false(self):
        """ ota_rahaa palauttaa False, jos otto ei onnistu"""
        self.assertFalse(self.maksukortti.ota_rahaa(2000))
