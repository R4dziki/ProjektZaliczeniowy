# -*- coding: cp1250 -*-
# HelloWorldProgram.py

# Wersja 2.0.0 – breaking change: zamiast menu prosty prompt dla imienia użytkownika

if __name__ == "__main__":
    name = input("Jak masz na imię? ").strip()
    print(f"Witaj, {name}! To jest nowa wersja 2.0.0 bez menu.")

