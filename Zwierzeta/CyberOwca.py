import random
from Base.Zwierze import Zwierze


class CyberOwca(Zwierze):
    DEFAULT_SILA = 11

    def __init__(self, print_log, x=0, y=0, sila=DEFAULT_SILA, wiek=0):
        super().__init__(x, y, 'K', "CyberOwca", sila, 4, print_log, wiek)

    def _find_nearest_barszcz(self, plansza, szerokosc, wysokosc):
        from Rosliny.Barszcz import Barszcz
        nearest, best_dist = None, float('inf')
        for x in range(wysokosc):
            for y in range(szerokosc):
                org = plansza[x][y]
                if isinstance(org, Barszcz):
                    dist = abs(self._x - x) + abs(self._y - y)
                    if dist < best_dist:
                        best_dist, nearest = dist, org
        return nearest

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        target = self._find_nearest_barszcz(plansza, szerokosc, wysokosc)
        if target:
            if target.x < self._x:
                self._x -= 1
            elif target.x > self._x:
                self._x += 1
            elif target.y < self._y:
                self._y -= 1
            elif target.y > self._y:
                self._y += 1
        else:
            dx, dy = random.choice([(0, -1), (0, 1), (1, 0), (-1, 0)])
            nx, ny = self._x + dx, self._y + dy
            if 0 <= nx < wysokosc and 0 <= ny < szerokosc:
                self._x, self._y = nx, ny

    def kolizja(self, other, plansza, szerokosc, wysokosc):
        return self.standard_kolizja(other, plansza, szerokosc, wysokosc)
