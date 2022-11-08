from maksukortti import Maksukortti
from kassapaate import Kassapaate


def main():
    unicafe_exactum = Kassapaate()
    kortti = Maksukortti(10000)

    unicafe_exactum.syo_edullisesti_kortilla(kortti)
    unicafe_exactum.syo_kateisella(1000, 240)
    print(kortti)


if __name__ == "__main__":
    main()
