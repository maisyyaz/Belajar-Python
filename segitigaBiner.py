#! bin/python3
print("Ini adalah program segitiga biner dengan bentuk segitiga")
string = ""
baris = 10
gerak = 1

while gerak <= baris - 1:
    kolom = gerak
    awal = 1
    while kolom >= awal:
        if awal % 2 == 0:
            string += "0 "
        else:
            string += "1 "
        awal += 1
    string += "\n"
    gerak += 1
while gerak >= 1:
    kolom = gerak
    awal = 1
    while kolom >= awal:
        if awal % 2 == 0:
            string += "0 "
        else:
            string += "1 "
        awal += 1
    string += "\n"
    gerak -= 1
print(string)

