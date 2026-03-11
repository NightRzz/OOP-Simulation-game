from abc import ABC

from Base.Organizm import Organizm


class Roslina(Organizm, ABC):

    def standard_akcja_rozsiew(self, szansa: int):
        import random
        self._rozsiane = random.randint(0, szansa - 1) == 0
