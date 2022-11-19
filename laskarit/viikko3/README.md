## Tehtava 1: Monopoli

```mermaid
 classDiagram
  class MonopoliSovellus{
  }
  class Nopat{
  }
  class Pelaaja{
    pelinappula
  }
  class Pelaajat{
  }
  Pelaajat ..> Pelaaja
  MonopoliSovellus ..> Pelaajat
  class Pelilauta{
    
  }
  class Ruutu{
  }
  Pelaaja  "0..1" -- "0..1" MonopoliSovellus
  Pelaaja  "2..8" ..>  Pelilauta
  Pelilauta "1" -- "*" MonopoliSovellus
  Nopat "2" -- MonopoliSovellus
  Ruutu "40" ..>   Pelilauta

```
## Tehtava 2: Laajennettu Monopoli

```mermaid
classDiagram
  class MonopoliSovellus{
  }
  class Nopat{
  }
  class Pelaaja{
    pelinappula
    sijainti_ruudulla
    kadun_omistus
    raha
  }
  class Pelaajat{
  }
  class Pelilauta{
    Aloitusruutu: sijainti
    Vankila: sijainti
    Ruudut: 40
    Pelinappulat: 2..8
  }
  class Ruutu{
  }
  class Aloitusruutu{
    toiminto
  }
  class Vankila{
    toiminto
  }
  class SattumaJaYhteismaa{
    ota_kortti()
  }
  class AsematJaLaitokset{
    toiminto
  }
  class NormaalitKadut{
    talot_max: 4 or 1 hotelli
    pelaaja_omistaa
    toiminto
  }
  class Talo{
  }
  class Hotelli{
  }
  class Rakennus{
  }
  class Kortit{
    toiminto
  }

  Pelilauta "1" -- "*" MonopoliSovellus
  Nopat "2" -- MonopoliSovellus
  Pelaaja "0..1" -- "0..1"MonopoliSovellus
  MonopoliSovellus ..> Pelaajat
  Kortit -- MonopoliSovellus

  Hotelli --> Rakennus
  Talo --> Rakennus
  Rakennus ..> NormaalitKadut

  Aloitusruutu --> Ruutu
  Vankila --> Ruutu
  SattumaJaYhteismaa --> Ruutu
  AsematJaLaitokset --> Ruutu
  NormaalitKadut --> Ruutu

  Pelaajat ..> Pelaaja
  Pelaaja "2..8" ..> Pelilauta

  Kortit <.. SattumaJaYhteismaa

  Ruutu "40" ..> Pelilauta
  

```

## Tehtava 3: Sekvenssikaavio

```mermaid
sequenceDiagram
    Main ->> nMachine: new nMachine()
    activate nMachine
    nMachine ->> nFuelTank: new FuelTank()
    nMachine ->> nFuelTank: tank fill(40)
    nMachine ->> nEngine: new Engine(tank(40))
    deactivate nMachine
    Main ->> nMachine: drive()
    activate nMachine
    nMachine ->> nEngine: start()
    activate nEngine
    nEngine ->> nFuelTank: consume(5)
    nEngine -->> nMachine: running=True
    nMachine ->> nEngine: use_energy()
    deactivate nMachine
    nEngine ->> nFuelTank: consume(10)
    deactivate nEngine
```

## Tehtava 4: Laajempi sekvenssikaavio


```mermaid
sequenceDiagram
    activate main
      main ->> laitehallinto: new HKLLaitehallinto
      main ->> rautatietori: new Lataajalaite
      main ->> ratikka6: new Lukijalaite
      main ->> bussi244: new Lukijalaite
      main ->> laitehallinto: lisaa_lataaja(rautatietori)
      main ->> laitehallinto: lisaa_lukija(ratikka6)
      main ->> laitehallinto: lisaa_lukija(bussi244)
      main ->> lippu_luukku: new Kioski
      main ->> lippu_luukku: osta_matkakortti("Kalle")
      activate lippu_luukku
        lippu_luukku ->> kallen_kortti: new Matkakortti("Kalle", 0, 0, 0)
        lippu_luukku -->> main: kallen_kortti
      deactivate lippu_luukku
      main ->> rautatietori: lataa_arvoa(kallen_kortti, 3)

      activate rautatietori
        rautatietori ->> kallen_kortti: kasvata_arvoa(3)
      deactivate rautatietori

      main ->> ratikka6: osta_lippu(kallen_kortti, 0)

      activate ratikka6
        ratikka6 ->> kallen_kortti: vahenna_arvoa(1.5)
        ratikka6 -->> main: True
      deactivate ratikka6

      main ->> bussi244: osta_lippu(kallen_kortti, 2)

      activate bussi244
        bussi244 -->> main: False
      deactivate bussi244

    deactivate main
  ```