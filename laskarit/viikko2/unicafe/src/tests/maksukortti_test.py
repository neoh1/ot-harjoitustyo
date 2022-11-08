import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataus_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")

    def test_ota_rahaa_saldo_vahenee(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 8.00 euroa")

    def test_ota_rahaa_saldo_ei_muutu_jos_liian_vahan(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_ota_rahaa_bool(self):
        testF = self.maksukortti.ota_rahaa(1100)
        testT = self.maksukortti.ota_rahaa(800)
        self.assertEqual(testF, False)
        self.assertEqual(testT, True)


