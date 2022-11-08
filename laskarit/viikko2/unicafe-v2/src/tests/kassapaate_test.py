"""
better version maybe?
But i still dont like forcing testing on edullinen and maukas, which is asked :b
"""

import unittest
from kassapaate import Kassapaate, KateinenMaksutapa, KorttiMaksutapa, Lounas
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    """ kassapaatte.py testaukset """

    def assert_kassapaate(self, rahaa, e, m):
        """ 
        Apumetodi muille testeille
        e = edulliset lounaat kassapaatteessa
        m = maukkaat lounaat
        """
        self.assertEqual(self.kassapaate.kassassa_rahaa, rahaa)
        self.assertEqual(self.kassapaate.edulliset, e)
        self.assertEqual(self.kassapaate.maukkaat, m)

    def setUp(self):
        """ 
        Kassapaate: rahaa 1000_00, myytyja annoksia 0 edullista, 0 maukasta 
        Edullisen ja maukkaan aterian hinta: 240, 400
        """
        self.kassapaate = Kassapaate(1000_00)
        self.lounaat = [l
                        for l in Lounas]  # kay lapi lounaat ja pistaa listaan

    def test_kassapaate_luotu_oikein(self):
        """ aloitusraha 1000 euroa """
        self.assert_kassapaate(1000_00, 0, 0)

    def test_kassapaate_neg_rahat(self):
        """ varmistetaan ettei neg. rahoja voi lisata """
        with self.assertRaises(ValueError):
            self.kassapaate.kassassa_rahaa = -10_000_000

    def test_kateisosto_edullinen(self):
        """ kateis_ostos edullinen 10e """
        lounas = self.lounaat[0]  # edullinen
        vaihtoraha = self.kassapaate.osta_lounas(lounas,
                                                 KateinenMaksutapa(10_00))
        self.assertEqual(vaihtoraha, 10_00 - lounas.value)
        self.assert_kassapaate(1000_00 + lounas.value, 1, 0)

    def test_kateisosto_maukas(self):
        """ kateis_ostos maukas 10e """
        lounas = self.lounaat[1]  # maukas
        vaihtoraha = self.kassapaate.osta_lounas(lounas,
                                                 KateinenMaksutapa(10_00))
        self.assertEqual(vaihtoraha, 10_00 - lounas.value)
        self.assert_kassapaate(1000_00 + lounas.value, 0, 1)

    def test_kateisosto_ei_tarpeeksi(self):
        """ asiakas antaa vain 2 euroa """
        for lounas in self.lounaat:
            kateinen = KateinenMaksutapa(2_00)
            self.kassapaate.osta_lounas(lounas, kateinen)
            # Maksu ei onnistu, niin rahan ei pitaisi muuttua
            self.assertEqual(kateinen.kortti.saldo, 2_00)
            # Kassan rahamaara ei pitaisi muuttua
            self.assert_kassapaate(1000_00, 0, 0)

    def test_korttiostos_on_rahaa_edullinen(self):
        """ lisataan kortti, jonka saldo on 10e """
        kortti = Maksukortti(10_00)
        lounas = self.lounaat[0]  # edullinen
        self.kassapaate.osta_lounas(lounas, KorttiMaksutapa(kortti))
        self.assert_kassapaate(1000_00 + lounas.value, 1, 0)

    def test_korttiostos_on_rahaa_maukas(self):
        """ lisataan kortti, jonka saldo on 10e """
        kortti = Maksukortti(10_00)
        lounas = self.lounaat[1]  # maukas
        self.kassapaate.osta_lounas(lounas, KorttiMaksutapa(kortti))
        self.assert_kassapaate(1000_00 + lounas.value, 0, 1)

    def test_korttiostos_ei_rahaa(self):
        """ lisataan kortti, jonka saldo on 1e, oston ei pitaisi onnistua """
        kortti = Maksukortti(10)
        for lounas in self.lounaat:
            self.kassapaate.osta_lounas(lounas, KorttiMaksutapa(kortti))
            self.assertEqual(kortti.saldo, 10)
            self.assert_kassapaate(1000_00, 0, 0)

    def test_kortin_lataus(self):
        """ lisataan 100e korttiin """
        kassan_raha = 1000_00
        lisays = 100_00
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, lisays)
        self.assertEqual(kortti.saldo, 1000 + lisays)
        self.assert_kassapaate(kassan_raha + lisays, 0, 0)
        kassan_raha += lisays

    def test_kortin_lataus_neg(self):
        """ negatiivinen lisays """
        kortti = Maksukortti(1000)
        summa = -10
        with self.assertRaises(ValueError):
            self.kassapaate.lataa_rahaa_kortille(kortti, summa)
        # kortin ja kassan saldo ei muutu
        self.assertEqual(kortti.saldo, 1000)
        self.assert_kassapaate(1000_00, 0, 0)
