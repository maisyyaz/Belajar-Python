#!bin/python3

kambing = input("Masukan Jumlah Kambing: ")
jmlKambing = 100
waktu = 0

semester = 12 / 6
persen = jmlKambing * 5 / 100
awalKambing = jmlKambing

while jmlKambing < int(kambing):
    jmlKambing = jmlKambing + persen * semester
    waktu += 1

# tipe data tuple
# print(kambing , "ekor kambing memerlukan waktu" , waktu , "tahun dari" , awalKambing , "ekor kambing")
print("%s ekor kambing memerlukan waktu %s tahun dari %s ekor kambing" % (kambing, waktu, awalKambing))