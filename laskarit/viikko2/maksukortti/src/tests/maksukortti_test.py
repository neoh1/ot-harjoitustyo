import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.card = Maksukortti(1000)

    def test_konstruktori_asettaa_saldon_oikein(self):
        # card with 10 euros == 1000 cents
        self.assertEqual(str(self.card), "Kortilla on rahaa 10.00 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.card.syo_edullisesti()
        self.assertEqual(str(self.card), "Kortilla on rahaa 7.50 euroa")

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.card.syo_maukkaasti()
        self.assertEqual(str(self.card), "Kortilla on rahaa 6.00 euroa")

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.syo_edullisesti()
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.syo_maukkaasti()
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

    def test_syo_edullisest_tasaraha(self):
        kortti = Maksukortti(250)
        kortti.syo_edullisesti()
        self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")

    def test_syo_maukkaasti_tasaraha(self):
        kortti = Maksukortti(400)
        kortti.syo_maukkaasti()
        self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.card.lataa_rahaa(2500)
        self.assertEqual(str(self.card), "Kortilla on rahaa 35.00 euroa")

    def test_kortille_ei_ladata_neg_summa(self):
        self.card.lataa_rahaa(-1000)
        self.assertEqual(str(self.card), "Kortilla on rahaa 10.00 euroa")

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.card.lataa_rahaa(20000)
        self.assertEqual(str(self.card), "Kortilla on rahaa 150.00 euroa")


