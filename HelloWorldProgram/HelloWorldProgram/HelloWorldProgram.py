# -*- coding: cp1250 -*-
# HelloWorldProgram.py

print("Oto program:")

if __name__ == "__main__":
    while True:
        print("\n1) Hello, world!")
        print("2) Opis programu")
        print("0) Wyj�cie")
        wyb�r = input("Wybierz opcj�: ").strip()

        if wyb�r == "1":
            print("\nHello, world!\n")
        elif wyb�r == "2":
            print("\nProsty program konsolowy demonstruj�cy Git/GitHub workflow.\n")
        elif wyb�r == "0":
            print("\nDo zobaczenia!")
            break
        else:
            print("\nNieprawid�owa opcja, spr�buj ponownie.")

