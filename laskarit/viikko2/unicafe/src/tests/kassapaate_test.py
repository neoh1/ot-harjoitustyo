"""
Test kassapaate
"""

import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti
class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassa = Kassapaate()
        self.card = Maksukortti(1000)

    def test_kassapaate_loaded(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_syo_edullinen_kateisella_tarpeeksi_rahaa(self):
        payment = self.kassa.syo_edullisesti_kateisella(250)
        # correct return 10
        self.assertEqual(payment, 10)
        # lunch sold inc by one
        self.assertEqual(self.kassa.edulliset, 1)
        # kassa increases by 240
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)

    def test_syo_edullinen_kateisella_liian_vahan(self):
        payment = self.kassa.syo_edullisesti_kateisella(200)
        # get money back
        self.assertEqual(payment, 200)
        # lunch sold inc by 0
        self.assertEqual(self.kassa.edulliset, 0)
        # kassa increases by 0
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_syo_maukas_kateisella_tarpeeksi_rahaa(self):
        payment = self.kassa.syo_maukkaasti_kateisella(410)
        # correct return 10
        self.assertEqual(payment, 10)
        # lunch sold inc by one
        self.assertEqual(self.kassa.maukkaat, 1)
        # kassa increases by 400
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    def test_syo_maukas_kateisella_liian_vahan(self):
        payment = self.kassa.syo_maukkaasti_kateisella(390)
        # correct return 390
        self.assertEqual(payment, 390)
        # lunch sold inc by 0
        self.assertEqual(self.kassa.maukkaat, 0)
        # kassa increases by 0
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_syo_kortilla_on_rahaa(self):
        edullinen_true = self.kassa.syo_edullisesti_kortilla(self.card)
        maukas_true = self.kassa.syo_maukkaasti_kortilla(self.card)
        self.assertEqual(edullinen_true, True)
        self.assertEqual(maukas_true, True)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.maukkaat, 1)
        # money in cashier not increased
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_syo_kortilla_ei_rahaa(self):
        kortti = Maksukortti(10) # not enough money
        edullinen_false = self.kassa.syo_edullisesti_kortilla(kortti)
        maukas_false = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(edullinen_false, False)
        self.assertEqual(maukas_false, False)
        # No sales happened
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)
        # money in cashier not increased                     
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)


