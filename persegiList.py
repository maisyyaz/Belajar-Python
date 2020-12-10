sisi = int(input('mau berapa sisi: '))
data_angka = [[0 for i in range(sisi)] for j in range(sisi)]

print('Output:')
kiri = 0
kanan = sisi - 1
atas = 0
bawah = sisi - 1
hitung = 1

for i in range(sisi):
    for j in range(kiri, bawah + 1):
        data_angka[j][kiri] = hitung
        hitung += 1

    for j in range(kiri + 1, kanan + 1):
        data_angka[bawah][j] = hitung
        hitung += 1

    for j in range(kanan - 1, atas - 1, -1):
        data_angka[j][kanan] = hitung
        hitung += 1

    for j in range(kanan - 1, kiri, -1):
        data_angka[atas][j] = hitung
        hitung += 1

    kanan -= 1
    kiri += 1
    bawah -= 1
    atas += 1

for i in range(len(data_angka)):
    for j in range(len(data_angka)):
        print(data_angka[i][j], end='\t')
    print()
