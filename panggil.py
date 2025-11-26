import bangunruang as br
import bangundatar as bd

print("~~~ Bangun Ruang ~~~")
print(f"volum kubus dengan sisi 3 adalah {br.kubus(3)}")
print(f"volum balok adalah {br.balok(4,5,2)}")
print(f"volum prisma segitiga adalah {br.prisma(5,4,5)}")
print(f"volum tabung adalah {br.tabung(6,9)}")
print(f"volum kerucut adalah {br.kerucut(5,10)}")

print("~~~ Bangun Datar ~~~")
print(f"luas persegi adalah{bd.persegi(4)}")
print(f"luas persegi panjang adalah{bd.persegi_panjang(10,5)}")
print(f"luas segitiga adalah{bd.segitiga(4,3)}")
print(f"luas lingkaran{bd.lingkaran(7)}")
print(f"luas jajargenjang adalah {bd.jajargenjang(4,7)}")
