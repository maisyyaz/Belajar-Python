from customer import Customer


import random
import datetime

atm = Customer(0)

while True:
    pin = int(input('Masukkan pin anda: '))
    trial = 0

    while pin != int(atm.cekPin()) and trial < 3:
        pin = int(input('Pin anda salah. Silakan Masukkan lagi: '))

        trial += 1

        if trial == 3:
            print('Error. Silakan ambil kartu dan coba lagi..')
            exit()

    while True:
        print("Selamat datang di ATM Progate..")
        print("\n1 - Cek Saldo \t 2 - Debet \t 3 -Simpan \t4 - Ganti Pin \t5 - Keluar")

        pilihMenu = int(input('Silahkan pilih menu[1-5]: '))

        if pilihMenu == 1:
            print('Saldo anda sekarang: Rp.', atm.cekSaldo(), '\n')
        elif pilihMenu == 2:
            nominal = float(input('Masukan nominal saldo: '))
            ver_debet = input("Konfirmasi: Anda akan melakukan debet dengan nominal " + str(nominal) + " ? y/n ")

            if ver_debet == 'y':
                print('Saldo awal anda adalah', atm.cekSaldo())
            else:
                break

            if nominal < atm.cekSaldo():
                atm.debet(nominal)
                print("Transaksi debet berhasil!")
                print("Saldo sisa sekarang: Rp. ", atm.cekSaldo(), "\n")
            else:
                print("Maaf. Saldo anda tidak cukup untuk melakukan debet!")
                print("Silakan lakukan penambahan nominal saldo\n")

        elif pilihMenu == 3:
            nominal = float(input('Masukan nominal saldo: '))
            ver_deposit = input(
                "Konfirmasi: Anda akan melakukan penyimpanan dengan nominal {0} ? y/n ".format(str(nominal)))

            if ver_deposit == 'y':
                atm.deposit(nominal)
                print("Saldo anda sekarang adalah: Rp." + str(atm.checkBalance()) + "\n")
            else:
                break

        elif pilihMenu == 4:
            ver_pin = int(input('Masukan pin anda: '))
            while ver_pin != atm.cekPin():
                ver_pin = int(input('Pin anda salah, silakan masukkan pin: '))

            update_pin = int(input('Silahkan masukan pin baru: '))
            ver_newpin = int(input('Coba masukan pin baru: '))

            while update_pin != ver_newpin:
                print("maaf, pin anda salah! ")
                update_pin = int(input('Silahkan masukan pin baru: '))
                ver_newpin = int(input('Coba masukan pin baru: '))

            if update_pin == ver_newpin:
                atm.cust_pin = update_pin
                print("pin baru anda sukses!\n")

        elif pilihMenu == 5:
            print("\nResi tercetak otomatis saat anda keluar. \nHarap simpan tanda terima ini \nsebagai bukti "
                  "transaksi anda.")
            print("No. Rekord: ", random.randint(100000, 1000000))
            print("Tanggal: ", datetime.datetime.now())
            print("Saldo akhir: ", atm.cekSaldo())
            print("Terima kasih telah menggunakan ATM Progate!")
            exit()

        else:
            print('Error. Maaf, menu yang anda masukan tidak tersedia\n')
