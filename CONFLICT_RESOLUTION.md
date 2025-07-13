# Conflict Resolution — HelloWorld Header

## 1. Środowisko
- Gałąź `main` po zmergowaniu zmian z `feature/header-design-a`
- Próba merge z `feature/header-design-b` wywołuje konflikt

## 2. Szczegóły konfliktu
- Plik: `HelloWorldProgram.py`
- Linia konfliktowa:
  ```diff
  <<<<<<< HEAD
      print("Oto program:")
  =======
      print("Oto mój program:")
  >>>>>>> feature/header-design-b
