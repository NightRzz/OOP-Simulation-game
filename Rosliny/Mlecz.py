from Base.Roslina import Roslina


class Mlecz(Roslina):
    DEFAULT_SILA = 0

    def __init__(self, print_log, x=0, y=0, sila=DEFAULT_SILA, wiek=0):
        super().__init__(x, y, 'M', "Mlecz", sila, 0, print_log, wiek)

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        self.multi_akcja_rozsiew(rolls=3, szansa=8)

    def kolizja(self, other, plansza, szerokosc, wysokosc):
        return other
