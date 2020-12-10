sisi = int(input('mau berapa sisi: '))
data_angka = [[0 for i in range(sisi)] for j in range(sisi)]

print('Output:')
for i in range(sisi):
    for j in range(sisi):
        if i == 0 or j == 0:
            data_angka[i][j] = 1
        else:
            data_angka[i][j] = data_angka[i][j - 1] + data_angka[i - 1][j]
        print(data_angka[i][j], end='\t')
    print()
"""
1 1 1
1 2 3
1 3 6
"""
