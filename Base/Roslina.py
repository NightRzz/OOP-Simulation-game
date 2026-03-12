from abc import ABC
import random
from Base.Organizm import Organizm


class Roslina(Organizm, ABC):
    MIN_WIEK_ROZSIEWU: int = 2

    def standard_akcja_rozsiew(self, szansa: int):
        if self.wiek < self.MIN_WIEK_ROZSIEWU:
            return
        self._rozsiane = random.randint(0, szansa - 1) == 0

    def multi_akcja_rozsiew(self, rolls: int, szansa: int):
        if self.wiek < self.MIN_WIEK_ROZSIEWU:
            return
        self._rozsiane = any(random.randint(0, szansa - 1) == 0 for _ in range(rolls))
