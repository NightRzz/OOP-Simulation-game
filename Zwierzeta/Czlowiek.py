from Base.Zwierze import Zwierze

_KEY_UP      = 38
_KEY_DOWN    = 40
_KEY_LEFT    = 37
_KEY_RIGHT   = 39
_KEY_ABILITY = 49

_ABILITY_STRENGTH_BONUS = 5
_ABILITY_DURATION       = 6
_ABILITY_COOLDOWN_READY = 10


class Czlowiek(Zwierze):
    DEFAULT_SILA = 5

    def __init__(self, print_log, x=0, y=0, sila=DEFAULT_SILA, wiek=0, cooldown=6, licznik=0, wlacz=False):
        super().__init__(x, y, 'C', "Czlowiek", sila, 4, print_log, wiek)
        self._cooldown = cooldown
        self._licznik = licznik
        self._wlacz = wlacz

    @property
    def cooldown(self) -> int:
        return self._cooldown

    @cooldown.setter
    def cooldown(self, value: int):
        self._cooldown = value

    @property
    def licznik(self) -> int:
        return self._licznik

    @licznik.setter
    def licznik(self, value: int):
        self._licznik = value

    @property
    def wlacz(self) -> bool:
        return self._wlacz

    @wlacz.setter
    def wlacz(self, value: bool):
        self._wlacz = value

    def _tick_ability(self):
        if self.wlacz:
            if self.licznik < _ABILITY_DURATION:
                pass  # ability is active, no tick drain
            else:
                self.sila -= _ABILITY_STRENGTH_BONUS
                self.wlacz = False
                self.licznik = 0
                self.cooldown = 0
                self.print_log("Umiejetnosc czlowieka przestala dzialac")
        else:
            self.cooldown += 1

    def _activate_ability(self):
        if self.cooldown < _ABILITY_COOLDOWN_READY:
            self.print_log("Umiejetnosc czlowieka nie gotowa")
        elif not self.wlacz:
            self.print_log("Umiejetnosc czlowieka wlaczona")
            self.sila += _ABILITY_STRENGTH_BONUS
            self.wlacz = True

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        self._tick_ability()
        key = keycode or 0
        if key == _KEY_UP and self.x > 0:
            self.x -= 1
        elif key == _KEY_DOWN and self.x < wysokosc - 1:
            self.x += 1
        elif key == _KEY_LEFT and self.y > 0:
            self.y -= 1
        elif key == _KEY_RIGHT and self.y < szerokosc - 1:
            self.y += 1
        elif key == _KEY_ABILITY:
            self._activate_ability()
        self.print_log(f"Ruszasz sie na pole {self.x} {self.y} z sila {self.sila}")
        if self.wlacz:
            self.licznik += 1

    def kolizja(self, other, plansza, szerokosc, wysokosc):
        return self.standard_kolizja(other, plansza, szerokosc, wysokosc)
