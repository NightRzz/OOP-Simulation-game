from Base.Roslina import Roslina


class WilczeJagody(Roslina):
    DEFAULT_SILA = 99

    def __init__(self, print_log, x=0, y=0, sila=DEFAULT_SILA, wiek=0):
        super().__init__(x, y, 'J', "Wilcze Jagody", sila, 0, print_log, wiek)

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        self.standard_akcja_rozsiew(szansa=30)

    def kolizja(self, other, plansza, szerokosc, wysokosc):
        self.print_log(f"{other.imie} zjada {self.imie} i ginie")
        return self
