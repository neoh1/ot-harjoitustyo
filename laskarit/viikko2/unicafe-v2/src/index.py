from maksukortti import Maksukortti
from kassapaate import Kassapaate, KorttiMaksutapa, KateinenMaksutapa
from lounas import Lounas

def main():
    unicafe_exactum = Kassapaate()
    kortti = Maksukortti(10000)
    unicafe_exactum.osta_lounas(Lounas.MAUKAS, KorttiMaksutapa(kortti))
    unicafe_exactum.osta_lounas(Lounas.EDULLINEN, KateinenMaksutapa(1000))
    print(kortti)


if __name__ == "__main__":
    main()
