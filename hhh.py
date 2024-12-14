

class Shaxs:

    def __init__(self, isim, yosh, manzil):
        self.__isim = isim
        self.__yosh = yosh
        self.manzil = manzil


    def __shaxs_malumotlari(self):
        return f"{self.__ism}, {self.__yosh} yoshda, manzili: {self.manzil}"


    def malumotlar_ulish(self):
        return self.__shaxs_malumotlari()

    def unvini_aniqlash(self):
        return "Shaxs"


class Ishchi(Shaxs):

    def __init__(self, isim, yosh, manzil, lavozim, maosh):
        super().__init__(isim, yosh, manzil)
        self.lavozim = lavozim
        self.maosh = maosh

    def __hisoblu_maosh(self, uylik_saatlar, soatlik_tulov):
        return uylik_saatlar * soatlik_tulov


    def unvini_aniqlash(self):
        return "Oddiy Ishchi"

    @staticmethod
    def umumiy_ishchilar_malumotlari(ishchilar):
        return "\n".joini shchi.ishchi_malumotlari()


class Menejer(Ishchi):

    def __init__(self, isim, yosh, manzil, lavozim, maosh, butun_bulsim):
        super().__init__(isim, yosh, manzil, lavozim, maosh)
        self.__butun_bulsim = butun_bulsim


    def menejer_malumotlari(self):
        return f"{self.ishchilar_malumotlari()}, butun bulimi: {self.__butun_bulsim}"

    def unvuni_aniqlash(self):
        return "Menejer"



class Dasturchi(Ishchi):
    def __init__(self, isim, yosh, manzil, lavozim, maosh, dasturlar):
        super().__init__(isim, yosh, manzil, lavozim, maosh)
        self.__dasturlar = dasturlar


    def dasturchi_malumotlari(self):
        dasturlash = ", ".join(self.__dasturlar)
        return f"{self.umumiy_ishchilar_malumotlari()}, dasturlari: {dasturlari}"


    def unvini_aniqlash(self):
        return "Dasturchi"



menejer = Menejer("Mashhur", 35, "Toshkent", "Menejer", 5000, "Dasturiy Tuzilma")
dasturchi = Dasturchi("Dilshod", 28, "Samarqand", "Senior Dasturchi", 4000, ["Python", "Django", "Golang"])
ishchi = Ishchi("Azizbek", 30, "Andijon", "Texnik", 2500)

ishchilar = [menejer, dasturchi, ishchi]

print(Menejer.umumiy_ishchilar_malumotlari(ishchilar))
