import csv
import random
import tkinter as tk
from tkinter import ttk, messagebox

from Base.Roslina import Roslina
from Base.Zwierze import Zwierze
from Rosliny.Barszcz import Barszcz
from Rosliny.Guarana import Guarana
from Rosliny.Mlecz import Mlecz
from Rosliny.Trawa import Trawa
from Rosliny.WilczeJagody import WilczeJagody
from Zwierzeta.Antylopa import Antylopa
from Zwierzeta.CyberOwca import CyberOwca
from Zwierzeta.Czlowiek import Czlowiek
from Zwierzeta.Lis import Lis
from Zwierzeta.Owca import Owca
from Zwierzeta.Wilk import Wilk
from Zwierzeta.Zolw import Zolw

_FACTORY: dict[str, type] = {
    'A': Antylopa, 'O': Owca,  'W': Wilk,  'L': Lis,  'Z': Zolw,
    'T': Trawa,    'M': Mlecz, 'J': WilczeJagody,
    'G': Guarana,  'B': Barszcz,
    'C': Czlowiek, 'K': CyberOwca,
}

_COLORS: dict[str, str] = {
    'A': '#A88319', 'O': '#EDC3C7', 'W': '#75736E', 'L': '#D98A02',
    'Z': '#BDA573', 'T': '#07F20B', 'M': '#E1E81A', 'J': '#0B083D',
    'G': '#DB6556', 'B': '#B0DEA2', 'K': '#00CCFF', 'C': '#F2E5CB',
}

_INITIAL_SPAWNS: list[tuple[str, int]] = [
    ('W', 2), ('C', 1), ('A', 1), ('L', 1), ('Z', 2),
    ('T', 1), ('K', 1), ('M', 1), ('J', 1), ('B', 1),
    ('O', 1), ('G', 2),
]

_SAVE_FILE = 'save.txt'
_DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Swiat:
    def __init__(self, szerokosc: int, wysokosc: int):
        self.__szerokosc = szerokosc
        self.__wysokosc = wysokosc
        self.__plansza: list[list] = [[None] * szerokosc for _ in range(wysokosc)]
        self.__gra: list = []

        self.__root = tk.Tk()
        self.__root.title("Yuriy Dyedyk 201316")

        self._grid_frame = tk.Frame(self.__root)
        self._grid_frame.pack()

        self._log = tk.Text(self.__root, width=50, height=10)
        self._log.pack()

    def print_log(self, message: str):
        self._log.insert(tk.END, message + '\n')

    def _clear_log(self):
        self._log.delete('1.0', tk.END)

    def _make(self, x: int, y: int, org_id: str, sila=None, wiek: int = 0, **extra):
        cls = _FACTORY.get(org_id)
        if cls is None:
            return None
        if sila is None:
            sila = getattr(cls, 'DEFAULT_SILA', 0)
        if issubclass(cls, Czlowiek):
            return cls(self.print_log, x, y, sila, wiek, **extra)
        return cls(self.print_log, x, y, sila, wiek)

    def initialize_grid(self):
        for w in self._grid_frame.winfo_children():
            w.destroy()
        occupied = {(o.x, o.y): o for o in self.__gra if o is not None}
        for i in range(self.__wysokosc):
            for j in range(self.__szerokosc):
                btn = tk.Button(self._grid_frame, height=2, width=4)
                btn.grid(row=i, column=j)
                org = occupied.get((i, j))
                if org is not None:
                    btn.config(text=org.id, bg=_COLORS[org.id])
                else:
                    btn.config(command=lambda x=i, y=j: self._pick_organism(x, y))

    def update_grid(self):
        self.initialize_grid()

    def _pick_organism(self, x: int, y: int):
        ids    = list(_FACTORY.keys())
        labels = [cls.__name__ for cls in _FACTORY.values()]

        def ok():
            idx = combo.current()
            if idx >= 0:
                org = self._make(x, y, ids[idx])
                if org:
                    self.__plansza[x][y] = org
                    self.__gra.append(org)
                    self.update_grid()
            top.destroy()

        top = tk.Toplevel(self.__root)
        top.title("Wybierz organizm")
        tk.Label(top, text="Wybierz organizm:").pack()
        combo = ttk.Combobox(top, values=labels, state='readonly')
        combo.pack()
        tk.Button(top, text="OK", command=ok).pack()

    def generuj(self):
        spawn_list = [oid for oid, n in _INITIAL_SPAWNS for _ in range(n)]
        random.shuffle(spawn_list)
        for oid in spawn_list:
            self._place_random(oid)
        self.__gra = [o for row in self.__plansza for o in row if o is not None]

    def _place_random(self, org_id: str):
        for _ in range(self.__szerokosc * self.__wysokosc * 4):
            x = random.randrange(self.__wysokosc)
            y = random.randrange(self.__szerokosc)
            if self.__plansza[x][y] is None:
                self.__plansza[x][y] = self._make(x, y, org_id)
                return

    def wykonajTure(self, keycode=None):
        self._clear_log()
        self._prepare_turn()

        for i in range(len(self.__gra) - 1, -1, -1):
            org = self.__gra[i]
            if org is None:
                continue
            px, py = org.x, org.y
            org.begin_turn()
            org.akcja(self.__plansza, self.__gra, self.__szerokosc, self.__wysokosc, keycode)
            nx, ny = org.x, org.y

            if isinstance(org, Roslina) and org.rozsiane:
                self._disperse_plant(org)
            elif self.__plansza[nx][ny] is None or (nx == px and ny == py):
                self.__plansza[nx][ny] = org
                if (nx, ny) != (px, py):
                    self.__plansza[px][py] = None
            elif isinstance(org, Zwierze):
                self._resolve_collision(org, i, px, py)

        for org in self.__gra:
            if org is not None:
                org.end_turn()
        self.update_grid()

    def _prepare_turn(self):
        self.__gra = [o for row in self.__plansza for o in row if o is not None]
        self.__gra.sort(key=lambda o: (-o.inicjatywa, -o.wiek))

    def _resolve_collision(self, attacker, idx: int, px: int, py: int):
        tx, ty = attacker.x, attacker.y
        defender = self.__plansza[tx][ty]

        if attacker.czy_rozmnaza_sie(defender):
            for dx, dy in _DIRECTIONS:
                nx, ny = px + dx, py + dy
                if (0 <= nx < self.__wysokosc and 0 <= ny < self.__szerokosc
                        and self.__plansza[nx][ny] is None):
                    offspring = self._make(nx, ny, attacker.id)
                    self.__plansza[nx][ny] = offspring
                    self.__gra.append(offspring)
                    self.print_log(f"{attacker.imie} rozmnozyl sie na pole {nx} {ny}")
                    return
            attacker.x = px
            attacker.y = py
            return

        winner = defender.kolizja(attacker, self.__plansza, self.__szerokosc, self.__wysokosc)
        self.__plansza[tx][ty] = winner

        if winner is attacker:
            for j, g in enumerate(self.__gra):
                if g is defender:
                    self.__gra[j] = None
                    break
            self.__plansza[px][py] = None
        else:
            if not defender.zolwodparlatak:
                self.__gra[idx] = None
                self.__plansza[px][py] = None
            else:
                attacker.x = px
                attacker.y = py

    def _disperse_plant(self, org):
        dx, dy = random.choice(_DIRECTIONS)
        nx, ny = org.x + dx, org.y + dy
        if (0 <= nx < self.__wysokosc and 0 <= ny < self.__szerokosc
                and self.__plansza[nx][ny] is None):
            seedling = self._make(nx, ny, org.id)
            self.__plansza[nx][ny] = seedling
            self.__gra.append(seedling)
            self.print_log(f"{org.imie} rozsial sie na pole {nx} {ny}")

    def save_world_to_file(self):
        try:
            czlowiek = next((o for o in self.__gra if o is not None and isinstance(o, Czlowiek)), None)
            c_licznik  = czlowiek.licznik  if czlowiek else 0
            c_cooldown = czlowiek.cooldown if czlowiek else 0
            c_wlacz    = czlowiek.wlacz    if czlowiek else False
            with open(_SAVE_FILE, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([self.__wysokosc, self.__szerokosc, c_licznik, c_cooldown, c_wlacz])
                for org in self.__gra:
                    if org is not None:
                        writer.writerow([org.x, org.y, org.sila, org.id, org.wiek])
            messagebox.showinfo("Zapis", "Zapisano stan gry do pliku!")
        except IOError as e:
            messagebox.showerror("Zapis", f"Błąd: {e}")

    def wczytaj(self, file_path: str = _SAVE_FILE):
        try:
            with open(file_path, newline='') as f:
                reader = csv.reader(f)
                header = next(reader)
                self.__wysokosc = int(header[0])
                self.__szerokosc = int(header[1])
                licznik  = int(header[2])
                cooldown = int(header[3])
                wlacz    = header[4].strip().lower() == 'true'
                self.__gra.clear()
                self.__plansza = [[None] * self.__szerokosc for _ in range(self.__wysokosc)]
                for row in reader:
                    x, y, sila = int(row[0]), int(row[1]), int(row[2])
                    org_id, wiek = row[3], int(row[4])
                    cls = _FACTORY.get(org_id)
                    extra = dict(cooldown=cooldown, licznik=licznik, wlacz=wlacz) if cls and issubclass(cls, Czlowiek) else {}
                    org = self._make(x, y, org_id, sila=sila, wiek=wiek, **extra)
                    if org:
                        self.__plansza[x][y] = org
                        self.__gra.append(org)
            messagebox.showinfo("Wczytaj", "Zapis gry zostal wczytany!")
            self._clear_log()
            self.update_grid()
        except (IOError, ValueError) as e:
            messagebox.showerror("Błąd", f"Nie można wczytać: {e}")

    def start(self):
        self.generuj()
        self.initialize_grid()
        btn_frame = tk.Frame(self.__root)
        btn_frame.pack(pady=4)
        tk.Button(btn_frame, text="Wykonaj Turę", command=self.wykonajTure).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="Zapisz",       command=self.save_world_to_file).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="Wczytaj",      command=lambda: self.wczytaj()).pack(side=tk.LEFT, padx=4)
        for key, code in [('<Left>', 37), ('<Up>', 38), ('<Right>', 39), ('<Down>', 40), ('1', 49)]:
            self.__root.bind(key, lambda e, c=code: self.wykonajTure(c))
        self.__root.mainloop()


if __name__ == "__main__":
    szerokosc = int(input("Podaj szerokosc mapy: "))
    wysokosc  = int(input("Podaj wysokosc mapy: "))
    Swiat(szerokosc, wysokosc).start()
