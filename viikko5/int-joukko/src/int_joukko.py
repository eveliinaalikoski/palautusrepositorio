KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):

        if not isinstance(kapasiteetti, int) or kapasiteetti < 0 or not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kapasiteetti tai kasvatuskoko")  # heitin vaan jotain :D
        
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.lukujono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        if n in self.lukujono:
            return True
        return False

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            if self.alkioiden_lkm >= self.kapasiteetti:
                self._kasvata_listaa()
            self.lukujono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm += 1
            return True
        return False

    def _kasvata_listaa(self):
        uusi_lista = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kapasiteetti += self.kasvatuskoko
        uusi_lista[:self.alkioiden_lkm] = self.lukujono[:self.alkioiden_lkm]
        self.lukujono = uusi_lista

    def poista(self, luku):
        if not self.kuuluu(luku): return False
        indeksi = self.lukujono.index(luku)
        for index in range(indeksi, self.alkioiden_lkm-1):
            self.lukujono[index] = self.lukujono[index + 1]
        self.alkioiden_lkm -= 1
        self.lukujono[self.alkioiden_lkm] = 0
        return True

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.lukujono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a_taulu, b_taulu):
        apu_taulu = IntJoukko()
        for luku in a_taulu.to_int_list() + b_taulu.to_int_list():
            apu_taulu.lisaa(luku)
        return apu_taulu

    @staticmethod
    def leikkaus(a_taulu, b_taulu):
        apu_taulu = IntJoukko()
        for luku in a_taulu.to_int_list():
            if b_taulu.kuuluu(luku):
                apu_taulu.lisaa(luku)
        return apu_taulu

    @staticmethod
    def erotus(a_taulu, b_taulu):
        apu_taulu = IntJoukko()
        for luku in a_taulu.to_int_list():
            if not b_taulu.kuuluu(luku):
                apu_taulu.lisaa(luku)
        return apu_taulu

    def __str__(self):
        return "{" + ", ".join(str(luku) for luku in self.lukujono[:self.alkioiden_lkm]) + "}"
