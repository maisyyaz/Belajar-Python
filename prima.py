#! bin/python3
print("Ini adalah program bilangan prima")

batas = int(input("masukkan batas : "))
hitung = 1
i = 2
while hitung < batas:
    faktor = 0
    for j in range(1, i+1):
        if i % j == 0:
            faktor a+= 1
    if faktor < 3:
        print(i, end=' ')
    i += 1
    hitung += 1