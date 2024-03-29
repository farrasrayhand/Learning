import os
from os import system
import random
import getpass

system("title " + "Aplikasi Voucher Listrik")

menu = "yes"
login = "gagal"

voucher_5000 = ('1gaX2e','2343PU','3Md2fH','408hyj','5uywbY')
voucher_10000 = ('6XbiP9','7uF4fJ','81NoZe','9hw7Jt','10doTX')
voucher_25000 = ('11Tqqa','12HpzM','13GU9w','14MnDk','15wx2Y')
voucher_50000 = ('16ReXP','17dT3Y','187Czn','19wugy','20EcZz')
voucher_100000 = ('212pCP','22d9yU','23mNmk','240f5o','25f70U')

accounts = {
    "username": "farras",
    "password": "2041007",
    "nama": "Muhammad Farras Rayhand",
    "saldo_listrik": 50000,
    "saldo_emoney": 10000,
    "nomor_listrik" : "19216811"
    }

def beli_voucher(paket, nominal):
    saldo_emoney = accounts["saldo_emoney"] - paket
    accounts["saldo_emoney"] = saldo_emoney
    print("Selamat! Pembelian anda berhasil! Voucher Listrik anda :", random.choice(nominal))
    print("Sisa Saldo anda :", accounts["saldo_emoney"])
    input("Tekan enter untuk kembali!")

def redeem_voucher(paket):
    saldo_listrik = accounts["saldo_listrik"] + paket
    accounts["saldo_listrik"] = saldo_listrik
    print("Selamat! Kode Voucher anda berhasil di Reedem! Total Saldo Token Listrik anda : ", accounts["saldo_listrik"])
    input("Tekan enter untuk kembali!")

def emoney(paket):
    saldo_emoney = accounts["saldo_emoney"] + paket
    accounts["saldo_emoney"] = saldo_emoney
    print("Saldo E-Money anda sudah ditambahkan Total Saldo :", accounts["saldo_emoney"])
    input("Tekan enter untuk kembali!")

def signin():
    global login_username
    global login_password
    os.system('cls||clear')
    print("Silahkan Login Terlebih dahulu!")
    login_username = str(input("Masukkan Username : "))
    login_password = str(getpass.getpass("Masukkan Password : "))

while menu == "yes":
    os.system('cls||clear')
    print("-----------------------------------------------------")
    print("----------------APLIKASI TOKEN LISTRIK---------------")
    print("-----------------------------------------------------\n")
    print("Username :",accounts["username"])
    print("Password :",accounts["password"])
    print("Nomor Listrik :", accounts["nomor_listrik"])
    print("\n")
    print("Silahkan pilih menu yang ada!")
    print("1. Beli Voucher Listrik")
    print("2. Reedem Voucher Listrik")
    print("3. Top UP E-Money")
    print("4. Cek Info")
    print("5. Ganti Password")
    print("6. Keluar")
    menu_utama = (input ("Masukkan Pilihan Anda : "))
    if menu_utama == "1":
        while login == "gagal":
            signin()
            if login_username == accounts["username"] and login_password == accounts["password"]:
                os.system('cls||clear')
                print("Halo", accounts["nama"],"!\nSaldo E-Money anda Sisa :", accounts["saldo_emoney"],"\nMau Pilih yang mana?")
                print("1. Voucher 5.000")
                print("2. Voucher 10.000")
                print("3. Voucher 25.000")
                print("4. Voucher 50.000")
                print("5. Voucher 100.000")
                print("6. Kembali")
                pesan_voucher = (input("Masukkan Pilihan Anda : "))
                if pesan_voucher == "1":
                    if accounts["saldo_emoney"] >= 5000:
                        beli_voucher(5000, voucher_5000)
                        break
                    else:
                        print("Saldo anda tidak cukup! Silahkan Top UP Saldo E-Money anda!")
                        input("Tekan enter untuk kembali!")
                        break
                elif pesan_voucher == "2":
                    if accounts["saldo_emoney"] >= 10000:
                        beli_voucher(10000, voucher_10000)
                        break
                    else:
                        print("Saldo anda tidak cukup! Silahkan Top UP Saldo E-Money anda!")
                        input("Tekan enter untuk kembali!")
                        break
                elif pesan_voucher == "3":
                    if accounts["saldo_emoney"] >= 25000:
                        beli_voucher(25000, voucher_25000)
                        break
                    else:
                        print("Saldo anda tidak cukup! Silahkan Top UP Saldo E-Money anda!")
                        input("Tekan enter untuk kembali!")
                        break
                elif pesan_voucher == "4":
                    if accounts["saldo_emoney"] >= 50000:
                        beli_voucher(50000, voucher_50000)
                        break
                    else:
                        print("Saldo anda tidak cukup! Silahkan Top UP Saldo E-Money anda!")
                        input("Tekan enter untuk kembali!")
                        break
                elif pesan_voucher == "5":
                    if accounts["saldo_emoney"] >= 100000:
                        beli_voucher(100000, voucher_100000)
                        break
                    else:
                        print("Saldo anda tidak cukup! Silahkan Top UP Saldo E-Money anda!")
                        input("Tekan enter untuk kembali!")
                        break
                elif pesan_voucher == "6":
                    break
                else:
                    os.system('cls||clear')
                    input("Masukkan Anda Salah!")
                    break
            else:
                input("Username atau Password Salah!")
                os.system('cls||clear')
                break
    elif menu_utama == "2":
        while login == "gagal":
            signin()
            if login_username == accounts["username"] and login_password == accounts["password"]:
                os.system('cls||clear')
                reedem = (input("Login Berhasil! Silahkan Masukkan Kode Voucher Anda : "))
                if reedem in voucher_5000:
                    redeem_voucher(5000)
                    used = list(voucher_5000)
                    used.remove(reedem)
                    voucher_5000 = tuple(used)
                    break
                elif reedem in voucher_10000:
                    redeem_voucher(10000)
                    used = list(voucher_10000)
                    used.remove(reedem)
                    voucher_10000 = tuple(used)
                    break
                elif reedem in voucher_25000:
                    redeem_voucher(25000)
                    used = list(voucher_25000)
                    used.remove(reedem)
                    voucher_25000 = tuple(used)
                    break
                elif reedem in voucher_50000:
                    redeem_voucher(50000)
                    used = list(voucher_50000)
                    used.remove(reedem)
                    voucher_50000 = tuple(used)
                    break
                elif reedem in voucher_100000:
                    redeem_voucher(100000)
                    used = list(voucher_100000)
                    used.remove(reedem)
                    voucher_100000 = tuple(used)
                    break
                else:
                    print("Kode Voucher anda salah atau sudah terpakai!")
                    input("Tekan enter untuk kembali!")
                    break
            else:
                input("Username atau Password Salah!")
                os.system('cls||clear')
                break
    elif menu_utama == "3":
        while login == "gagal":
            signin()
            if login_username == accounts["username"] and login_password == accounts["password"]:
                os.system('cls||clear')
                print("Halo", accounts["nama"], "! Mau Pilih yang mana?")
                print("1. Saldo 50.000")
                print("2. Saldo 100.000")
                print("3. Kembali")
                pesan_saldo = (input("Masukkan Pilihan Anda : "))
                if pesan_saldo == "1":
                    emoney(50000)
                    break
                elif pesan_saldo == "2":
                    emoney(100000)
                    break
                elif pesan_saldo == "3":
                    break
                else:
                    os.system('cls||clear')
                    print("Masukkan Anda Salah!")
                    input("Tekan enter untuk kembali!")
                    break
            else:
                input("Username atau Password Salah!")
                os.system('cls||clear')
                break
    elif menu_utama == "4":
        os.system('cls||clear')
        num_listrik = str(input("Masukkan Nomor Listrik anda : "))
        if num_listrik == accounts["nomor_listrik"]:
            print("Nama :",accounts["nama"])
            print("Username :",accounts["username"])
            print("Nomor Listrik :",accounts["nomor_listrik"])
            print("Saldo E-Money :",accounts["saldo_emoney"])
            print("Saldo Token Listrik :", accounts["saldo_listrik"])
            input("Tekan enter untuk kembali!")
        else:
            os.system('cls||clear')
            print("Nomor Tidak Terdaftar!")
            input("Tekan enter untuk kembali!")
            continue
    elif menu_utama == "5":
        while login == "gagal":
            signin()
            if login_username == accounts["username"] and login_password == accounts["password"]:
                os.system('cls||clear')
                new_pass = str(getpass.getpass("Masukkan Password Baru : "))
                accounts["password"] = new_pass
                print("Password baru anda adalah :",accounts["password"])
                input("Tekan enter untuk kembali!")
                break
            else:
                input("Username atau Password Salah!")
                os.system('cls||clear')
                break
    elif menu_utama == "6":
        break
    else:
        os.system('cls||clear')
        print("Masukkan Anda Salah!")
        input("Tekan enter untuk kembali!")
        continue
