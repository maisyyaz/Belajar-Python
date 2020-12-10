#!bin/python3

def menu(nama, saldo):
    print(f"Selamat datang {nama} di Toko Pulsa Pyshare")
    print(f"Saldo anda {saldo}")
    print("[1] Beli Pulsa")
    print("[2] Cek Saldo")
    print("[3] Top Up Saldo ")

def beli_pulsa():
    print("[1] Pulsa 5.000")
    print("[2] Pulsa 10.000")
    print("[3] Pulsa 15.000")



nama = input("Masukan nama: ")
saldo = int(input("Masukkan saldo: "))
menu(nama, saldo)
pilih = input("Silahkan pilih (1/2/3): ")
