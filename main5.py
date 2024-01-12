royxat = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 8, 9, 7, 1]


takrorlanishlar = {}
toq_sonlar = set()

for son in royxat:
    if son % 2 != 0:
        if son in takrorlanishlar:
            takrorlanishlar[son] += 1
        else:
            takrorlanishlar[son] = 1
        toq_sonlar.add(son)

for son, takrorlar_soni in takrorlanishlar.items():
    if takrorlar_soni > 1:
        print(f"{son} soni {takrorlar_soni} marta toq sonlar orasida takrorlanganligi uchun chiqarildi")
