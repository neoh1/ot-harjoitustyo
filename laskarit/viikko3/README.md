## Tehtava 1: Monopoli
```mermaid
 classDiagram
  class MonopoliSovellus{
    game_run()
    nopan_heitto()
    lisaa_pelaaja()
  }
  class Nopat{
      2
  }
  class Pelaaja{
    pelinappula
  }
  class Pelaajat{
    pelaajat_min: 2
    pelaajat_max: 8
  }
  Pelaaja --> Pelaajat
  class Pelilauta{
    1
    Ruudut: 40
    
  }
  class Ruudut{
    40
  }
  Pelaajat --> MonopoliSovellus
  Pelilauta --> MonopoliSovellus
  Nopat --> MonopoliSovellus
  Ruudut --> Pelilauta
  ```