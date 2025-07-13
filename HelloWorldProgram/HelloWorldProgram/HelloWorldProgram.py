# -*- coding: cp1250 -*-
# HelloWorldProgram.py

print("Oto program:")

if __name__ == "__main__":
    while True:
        print("\n1) Hello, world!")
        print("2) Opis programu")
        print("0) Wyjście")
        wybór = input("Wybierz opcję: ").strip()

        if wybór == "1":
            print("\nHello, world!\n")
        elif wybór == "2":
            print("\nProsty program konsolowy demonstrujący Git/GitHub workflow.\n")
        elif wybór == "0":
            print("\nDo zobaczenia!")
            break
        else:
            print("\nNieprawidłowa opcja, spróbuj ponownie.")

