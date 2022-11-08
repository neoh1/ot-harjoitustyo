from maksukortti import Maksukortti
from lounas import Lounas



class KorttiMaksutapa:
    """ korttimaksu """

    def __init__(self, kortti):
        self.kortti = kortti

    def maksu(self, hinta):
        """ lounaan hinta vahennetaan kortilta 
        palauttaa True, jos raha summan otto onnistui.
        """
        return self.kortti.ota_rahaa(hinta)


class KateinenMaksutapa(KorttiMaksutapa):
    """ kateismaksu,
       melkein sama toiminta kuin maksukortti ja KorttiMaksutapa luokalla,
       mutta asiakkaiden kateismaaria ei tarvitse tietaa, pelkastaan antamaa maaraa.
       Käsitellään käteistä pseudo-korttina.
    """

    def __init__(self, sentit: int):
        """
        Kassapaattelle annettu raha senteissä 
        """
        super().__init__(Maksukortti(sentit))


class Kassapaate:
    """
    unicafen kassapaatteen metodit;
    - lounaiden mynti
    - annosmaarien kirjanpito
    - kortin lataus
    """

    def __init__(self, kassassa_rahaa=1000_00):
        """ default aloitus kassan raha maara on 1000e """
        self.kassassa_rahaa = kassassa_rahaa
        self.edulliset = 0
        self.maukkaat = 0

    @property
    def kassassa_rahaa(self):
        """ palauttaa kassan raha maaran """
        return self.__kassassa_rahaa

    @kassassa_rahaa.setter
    def kassassa_rahaa(self, uusi_maara):
        """ rahan maara kassassa """
        if uusi_maara >= 0:
            self.__kassassa_rahaa = uusi_maara
        else:
            raise ValueError("Kassa ei voi olla negatiivinen")

    def osta_lounas(self, lounas, maksutapa):
        """ Jos maksu menee lapi niin lisataan raha kassaan
            ja edullisiin tai maukkaisiin yksi
        """
        if maksutapa.maksu(lounas.value):
            if lounas.name == "EDULLINEN":
                self.edulliset += 1
            else:
                self.maukkaat += 1
            self.__kassassa_rahaa += lounas.value
            # jos maksettiin käteisella niin palautetaan jäävä raha
            if isinstance(maksutapa, KateinenMaksutapa):
                palautettava_raha = maksutapa.kortti.saldo
                maksutapa.kortti.saldo = 0
                return palautettava_raha

    def lataa_rahaa_kortille(self, kortti, summa):
        """ lataa summan kortille ja kassaan jos se on positiivinen luku """
        if summa<0:
            raise ValueError("Et voi ladata negatiivista rahaa kortille")
        else:
            kortti.lataa_rahaa(summa)
            self.kassassa_rahaa += summa


