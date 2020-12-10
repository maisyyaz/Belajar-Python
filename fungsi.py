#!bin/python3

def tambah(angka1, angka2):
    hasil = angka1 + angka2
    return hasil


def kali(angka1, angka2):
    hasil = angka1 * angka2
    return hasil


def kurang(angka1, angka2):
    hasil = angka1 - angka2
    return hasil


hitung1 = tambah(5, 7)
hitung2 = kurang(8, 3)
hitung3 = kali(5, 5)
campur = tambah(kurang(kali(2, 2), 2), 2)
print(hitung1)
print(hitung2)
print(hitung3)
print(campur)
