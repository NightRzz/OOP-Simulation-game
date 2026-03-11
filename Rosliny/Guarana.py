from Base.Roslina import Roslina


class Guarana(Roslina):
    STRENGTH_BONUS = 3
    DEFAULT_SILA = 0

    def __init__(self, print_log, x=0, y=0, sila=DEFAULT_SILA, wiek=0):
        super().__init__(x, y, 'G', "Guarana", sila, 0, print_log, wiek)

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        self.standard_akcja_rozsiew(szansa=25)

    def kolizja(self, other, plansza, szerokosc, wysokosc):
        other.sila += self.STRENGTH_BONUS
        self.print_log(
            f"{self.imie} zostaje zjedzona przez {other.imie}"
            f" i zwieksza jego sile o {self.STRENGTH_BONUS} pkt."
            f" Obecna sila {other.imie} wynosi {other.sila}"
        )
        return other
