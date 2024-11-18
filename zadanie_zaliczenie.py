from abc import ABC, abstractmethod
from copy import deepcopy
from datetime import datetime

# Klasa Klient
class Klient:
    """
    Reprezentacja klienta.
    Atrybuty:
        imie, nazwisko, adres, email
    """

    def __init__(self, imie, nazwisko, adres, email):
        """
        Inicjalizuje dane klienta.
        Args:
            imie, nazwisko, adres, email
        """
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres
        self.email = email

    def __str__(self):
        """
        Zwraca dane klienta w formie tekstowej.
        """
        return f"Klient: {self.imie} {self.nazwisko}, adres: {self.adres}, email: {self.email}"

# Klasa Produkt (abstrakcyjna)
class Produkt(ABC):
    """
    Abstrakcyjna klasa produktu.
    Atrybuty:
        nazwa, opis, cena
    """

    def __init__(self, nazwa, opis, cena):
        """
        Inicjalizuje dane produktu.
        Args:
            nazwa, opis, cena
        """
        self.nazwa = nazwa
        self.opis = opis
        self.cena = cena

    @abstractmethod
    def __str__(self):
        """
        Zwraca reprezentację tekstową produktu.
        """
        pass

# Klasa Książka
class Ksiazka(Produkt):
    """
    Reprezentacja książki.
    Atrybuty:
        autor, rok_wydania
    """

    def __init__(self, nazwa, opis, cena, autor, rok_wydania):
        """
        Inicjalizuje dane książki.
        Args:
            autor, rok_wydania
        """
        super().__init__(nazwa, opis, cena)
        self.autor = autor
        self.rok_wydania = rok_wydania

    def __str__(self):
        """
        Zwraca reprezentację książki w formie tekstowej.
        """
        return f"Książka: {self.nazwa}, autor: {self.autor}, rok wydania: {self.rok_wydania}, cena: {self.cena}"

# Klasa Zamówienie
class Zamowienie:
    """
    Reprezentacja zamówienia.
    Atrybuty:
        klient, produkt, ilosc
    """
    
    class ZamowieniePoCenieComparer:
        """
        Porównuje zamówienia po cenie.
        """
        def __call__(self, zamowienie):
            """
            Zwraca cenę produktu w zamówieniu.
            """
            return zamowienie.produkt.cena

    def __init__(self, klient, produkt, ilosc):
        """
        Inicjalizuje dane zamówienia.
        Args:
            klient, produkt, ilosc
        """
        self.klient = klient
        self.produkt = produkt
        self.ilosc = ilosc

    def __str__(self):
        """
        Zwraca reprezentację zamówienia w formie tekstowej.
        """
        return f"Zamówienie: {self.ilosc} x {self.produkt}, Klient: {self.klient.imie} {self.klient.nazwisko}"

    def clone(self):
        """
        Klonuje zamówienie.
        """
        return deepcopy(self)

# Klasa Osoba
class Osoba:
    """
    Reprezentacja osoby.
    Atrybuty:
        imie, nazwisko, rok_urodzenia
    """

    def __init__(self, imie, nazwisko, rok_urodzenia):
        """
        Inicjalizuje dane osoby.
        Args:
            imie, nazwisko, rok_urodzenia
        """
        self.imie = imie
        self.nazwisko = nazwisko
        self.rok_urodzenia = rok_urodzenia

    def wiek(self):
        """
        Zwraca wiek osoby.
        """
        return datetime.now().year - self.rok_urodzenia

    def __str__(self):
        """
        Zwraca reprezentację osoby w formie tekstowej.
        """
        return f"{self.imie} {self.nazwisko} ({self.wiek()} lat)"

    def __lt__(self, other):
        """
        Porównuje osoby wg wieku, nazwiska, imienia.
        """
        if self.wiek() != other.wiek():
            return self.wiek() < other.wiek()
        if self.nazwisko != other.nazwisko:
            return self.nazwisko < other.nazwisko
        return self.imie < other.imie

# Testowanie
if __name__ == "__main__":
    # Tworzenie klientów
    klient1 = Klient("Joanna", "Kielan", "Warszawa, ul. Kondratowicza 1", "joanna.kielan@gmail.com")
    klient2 = Klient("Mateusz", "Lebkowski", "Warszawa, ul. Żurawia 4", "mateusz.lebkowski@gmail.com")

    # Tworzenie książek
    ksiazka1 = Ksiazka("Krzyżacy", "Lektura szkolna", 99.99, "Henryk Sienkiewicz", 1899)
    ksiazka2 = Ksiazka("Delirium", "Young Adult", 49.99, "Lauren Oliver", 2011)

    # Tworzenie zamówień
    zamowienie1 = Zamowienie(klient1, ksiazka2, 1)
    zamowienie2 = Zamowienie(klient2, ksiazka1, 2)

    print(zamowienie1)
    print(zamowienie2)

    # Tworzenie listy osób
    osoby = [
        Osoba("Joanna", "Kielan", 2000),
        Osoba("Mateusz", "Lebkowski", 2000),
        Osoba("Patryk", "Wiecek", 2000),
    ]

    osoby.sort()
    print("\nPosortowane osoby:")
    for osoba in osoby:
        print(osoba)

    # Tworzenie listy zamówień i sortowanie wg ceny
    zamowienia = [zamowienie1, zamowienie2]
    zamowienia.sort(key=Zamowienie.ZamowieniePoCenieComparer())
    print("\nPosortowane zamówienia wg ceny:")
    for zam in zamowienia:
        print(zam)

    # Klonowanie zamówienia
    zamowienie_klon = zamowienie1.clone()
    zamowienie_klon.ilosc = 4
    print("\nOryginalne zamówienie:")
    print(zamowienie1)
    print("\nSklonowane zamówienie:")
    print(zamowienie_klon)
