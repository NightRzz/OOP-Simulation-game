from Base.Roslina import Roslina
from Base.Zwierze import Zwierze
from Zwierzeta.CyberOwca import CyberOwca


class Barszcz(Roslina):
    DEFAULT_SILA = 10

    def __init__(self, print_log, x=0, y=0, sila=DEFAULT_SILA, wiek=0):
        super().__init__(x, y, 'B', "Barszcz Sosnowskiego", sila, 0, print_log, wiek)

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        self._exterminate_neighbours(plansza, gra)
        self.standard_akcja_rozsiew(szansa=50)

    def kolizja(self, other, plansza, szerokosc, wysokosc):
        if isinstance(other, CyberOwca):
            self.print_log(f"{other.imie} zjada {self.imie}")
            return other
        return self

    def _exterminate_neighbours(self, plansza, gra):
        neighbours = {(self._x + dx, self._y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]}
        for i, org in enumerate(gra):
            if (org is not None
                    and isinstance(org, Zwierze)
                    and not isinstance(org, CyberOwca)
                    and (org.x, org.y) in neighbours):
                self.print_log(f"{org.imie} umiera przez Barszcz Sosnowskiego")
                plansza[org.x][org.y] = None
                gra[i] = None
