import math

class Hinh:
    def __init__(self, dodai, chieucao):
        self.dodai = dodai
        self.chieucao = chieucao

class Round(Hinh):

    def chuvi(self):
        return 2 * math.pi * self.dodai
    def dientich(self):
        return math.pi * self.dodai ** 2

class hv(Hinh):

    def chuvi(self):
        return 4 * self.dodai
    def dientich(self):
        return self.dodai ** 2

class tam_giac(Hinh):

    def chuvi(self):
        return 3 * self.dodai
    def dientich(self):
        return (math.sqrt(3) / 4) * self.dodai ** 2

class luc_giac(Hinh):

    def chuvi(self):
        return 6 * self.dodai
    def dientich(self):
        return (3 * math.sqrt(3) / 2) * self.dodai ** 2

class ngu_giac(Hinh):

    def chuvi(self):
        return 5 * self.dodai
    def dientich(self):
        return (1 / 4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.dodai ** 2

class bat_giac(Hinh):

    def chuvi(self):
        return 8 * self.dodai
    def dientich(self):
        return 2 * (1 + math.sqrt(2)) * self.dodai ** 2

class TruTron(Round):

    def thetich(self):
        return self.dientich() * self.chieucao

class TruVuong(hv):

    def thetich(self):
        return self.dientich() * self.chieucao

class TruTamGiac(tam_giac):

    def thetich(self):
        return self.dientich() * self.chieucao

class TruLucGiac(luc_giac):

    def thetich(self):
        return self.dientich() * self.chieucao

class TruNguGiac(ngu_giac):

    def thetich(self):
        return self.dientich() * self.chieucao

class TruBatGiac(bat_giac):

    def thetich(self):
        return self.dientich() * self.chieucao

canh = float(input("Nhập cạnh / bán kính: "))
chieucao = float(input("Nhập chiều cao: "))

tron = TruTron(canh, chieucao)
vuong = TruVuong(canh, chieucao)
tam_giac = TruTamGiac(canh, chieucao)
luc_giac = TruLucGiac(canh, chieucao)
ngu_giac = TruNguGiac(canh, chieucao)
bat_giac = TruBatGiac(canh, chieucao)

print(f"Hình tròn: Chu vi = {tron.chuvi()} Diện tích = {tron.dientich()} Thể tích khối trụ tròn = {tron.thetich()}")
print(f"Hình vuông: Chu vi = {vuong.chuvi()} Diện tích = {vuong.dientich()} Thể tích khối trụ vuông = {vuong.thetich()}")
print(f"Tam giác đều: Chu vi = {tam_giac.chuvi()} Diện tích = {tam_giac.dientich()} Thể tích khối trụ tam giác đều = {tam_giac.thetich()}")
print(f"Lục giác đều: Chu vi = {luc_giac.chuvi()} Diện tích = {luc_giac.dientich()} Thể tích khối trụ lục giác đều = {luc_giac.thetich()}")
print(f"Ngũ giác đều: Chu vi = {ngu_giac.chuvi()} Diện tích = {ngu_giac.dientich()} Thể tích khối trụ ngũ giác đều = {ngu_giac.thetich()}")
print(f"Bát giác đều: Chu vi = {bat_giac.chuvi()} Diện tích = {bat_giac.dientich()} Thể tích khối trụ bát giác đều = {bat_giac.thetich()}")
