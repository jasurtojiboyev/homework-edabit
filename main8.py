def belgilar_soni(shakllar):
    belgi_soni = 0
    for shakl in shakllar:
        belgi_soni += len(shakl)
    return belgi_soni

# Misol:
shakllar_royxati = input("shakil kriting :")
soni = belgilar_soni(shakllar_royxati)
print(f"Shakllar uchun belgi soni: {soni}")
