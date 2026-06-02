#!/usr/bin/env python3

print("Kalkulator")
print("1 - Dodawanie")
print("2 - Odejmowanie")
print("3 - Mnożenie")
print("4 - Dzielenie")

wybor = input("Wybierz czynność: ")

liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))

if wybor == "1":
    wynik = liczba1 + liczba2
    print("Wynik:", wynik)

elif wybor == "2":
    wynik = liczba1 - liczba2
    print("Wynik:", wynik)

elif wybor == "3":
    wynik = liczba1 * liczba2
    print("Wynik:", wynik)

elif wybor == "4":
    if liczba2 != 0:
        wynik = liczba1 / liczba2
        print("Wynik:", wynik)
    else:
        print("Nie można dzielić przez zero.")

else:
    print("Nieprawidłowy wybór.")
