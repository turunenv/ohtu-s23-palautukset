from pelitehdas import PeliTehdas

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        pelityyppi = input()[-1:].lower()

        peli = PeliTehdas.luo_peli(pelityyppi)

        if not peli:
            break

        peli.pelaa()


if __name__ == "__main__":
    main()
