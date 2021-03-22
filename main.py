# zad1
# import random
# import sys
#
# plik = open('dane.txt', 'w+', encoding='utf8')
# lista = []
# for a in range(10):
#     a = random.randrange(500)
#     lista.append(a)
#
# parzyste = [b for b in lista if b % 2 == 0 and b != 0]
# print(parzyste)
#
# plik.write(str(parzyste))
#
# plik.close()
# zad2
# plik = open('dane.txt','r+')
# linia = plik.readline()
# print(linia)
# zad3
# import sys
# with open('tekst.txt', 'a+') as plik:
#         print("Wpisz tekst")
#         dane = sys.stdin.readline()
#         plik.writelines(dane)
#         # for linia in plik:
#         #     print(linia,end='')
# plik = open('tekst.txt', 'r')
# linie = plik.readlines()
# print(linie)
# zad4
# class NaZakupy:
#     """Klasa NaZakupy"""
#     def __init__(self, n, i, j, c):
#         self.n = n
#         self.i = float(i)
#         self.j = j
#         self.c = float(c)
#     def wyswietl_produkt(self):
#         return self.n
#     def ile_produktu(self):
#         return str(self.i)+str(self.j)
#     def ile_kosztuje(self):
#         return self.i*self.c
#
# obiekt = NaZakupy("arbuz",4,"kg",11)
# print(obiekt.wyswietl_produkt())
# print(obiekt.ile_produktu())
# print(obiekt.ile_kosztuje())
# zad5
# class Ciagi:
#     def __init__(self, a1, r, n):
#         self.a1 = float(a1)
#         self.a2 = float(a1+r)
#         self.a3 = float(a1+2*r)
#         self.r = float(r)
#         self.n = float(n)
#     def wyswietl_dane(self):
#         print(self.a1)
#         print(self.a2)
#         print(self.a2)
#         print(self.r)
#         print(self.n)
#     def pobierz_elementy(self, a1, a2, a3):
#         self.a1 = float(a1)
#         self.a2 = float(a2)
#         self.a3 = float(a3)
#     def pobierz_parametry(self, a1, r, n):
#         self.a1 = float(a1)
#         self.r = float(r)
#         self.n = float(n)
#     def policz_sume(self):
#         suma = ((2 * self.a1 + (self.n - 1) * self.r) / 2) * self.n
#         print(suma)
#     def policz_elementy(self):
#         print(self.a1 + (self.n - 1) * self.r)
#
#
# obiekt = Ciagi()
# print(obiekt.wyswietl_dane())
# print(obiekt.pobierz_parametry(1,2,7))
# print(obiekt.pobierz_elementy(1,3,5))
# print(obiekt.policz_sume())
# print(obiekt.policz_elementy())
# zad6
# class Robaczek:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def idz_w_gore(self, ile):
#         self.y+=ile
#     def idz_w_prawo(self, ile):
#         self.x+=ile
#     def idz_w_lewo(self, ile):
#         self.x-=ile
#     def idz_w_dol(self, ile):
#         self.y-=ile
#     def pokaz_gdzie_jestes(self):
#         print("x" + str(self.x))
#         print("y" + str(self.y))
#
# obiekt = Robaczek(0,0)
#
# print(obiekt.idz_w_gore(1))
# print(obiekt.pokaz_gdzie_jestes())
# print(obiekt.idz_w_prawo(1))
# print(obiekt.idz_w_dol(1))
# print(obiekt.idz_w_lewo(1))
# print(obiekt.pokaz_gdzie_jestes())

