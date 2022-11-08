
class Kassapaate:
    
    def __init__(self):
        self.kassassa_rahaa = 100000
        self.edulliset = 0
        self.maukkaat = 0
        self.hinnat = [240, 400]

    def lisaa_lounas(self, hinta):
        if hinta == self.hinnat[0]:
            self.edulliset += 1
        else:
            self.maukkaat += 1

    def syo_kateisella(self, maksu, hinta):
        if maksu >= hinta and hinta in self.hinnat:
            self.kassassa_rahaa = self.kassassa_rahaa + hinta
            self.lisaa_lounas(hinta)
            return maksu - hinta
        return maksu
    
    def syo_kortilla(self, kortti, hinta):
        if kortti.saldo >= hinta and hinta in self.hinnat:                                             
            kortti.ota_rahaa(hinta)
            self.lisaa_lounas(hinta)
            return True             
        return False

    def syo_edullisesti_kateisella(self, maksu):
        return self.syo_kateisella(maksu, self.hinnat[0])

    def syo_maukkaasti_kateisella(self, maksu):
        return self.syo_kateisella(maksu, self.hinnat[1])

    def syo_edullisesti_kortilla(self, kortti):
        return self.syo_kortilla(kortti, self.hinnat[0])

    def syo_maukkaasti_kortilla(self, kortti):
        return self.syo_kortilla(kortti, self.hinnat[1])

    def lataa_rahaa_kortille(self, kortti, summa):
        if summa >= 0:
            kortti.lataa_rahaa(summa)
            self.kassassa_rahaa += summa
        return

