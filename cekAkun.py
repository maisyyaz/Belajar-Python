#! bin/python3

username = input("Username: ")


if username == "PeinAkatsuki":
    password = input("Masukkan password: ")
    if password != "1sampai10":
        while password != "1sampai10":
            print("Password Salah")
            password = input("Masukkan password: ")
    print("Anda berhasil login")
else:
    print("siapa anda?")