import os
from os import system
import random
import getpass

system("title " + "Toko Farras 2041007")

login = 0

voucher_elektronik = ('antigaptek','jamanmodern')
voucher_fashion = ('kaumbranded','belibaju')
voucher_makanan = ('makanhepi','makankenyang')

accounts = {
    "username": "farras",
    "password": "2041007",
    "nama": "Muhammad Farras Rayhand",
    "saldo_emoney": 900000
    }

def menu():
    os.system('cls||clear')
    print("-----------------------------------------------------")
    print("----------------TOKO PADIA---------------")
    print("-----------------------------------------------------\n")
    print("Saldo anda :", accounts["saldo_emoney"])
    print("\n")
    print("Silahkan pilih menu yang ada!")
    print("1. Beli Handphone - Rp. 1.000.000 (Elektronik)")
    print("2. Beli Baju Olahraga - Rp. 150.000 (Fashion)")
    print("3. Beli Bakso - Rp.25.000 (Makanan)")
    print("4. Tambah Saldo E-Money")
    print("5. Cek Promo")
    print("6. Keluar")

def promo_today():
    print("Promo Hari ini adalah : ")
    print("1. antigaptek = Promo diskon 5% hanya untuk kategori Elektronik")
    print("2. kaumbranded = Promo diskon 8% hanya untuk kategori Fashion")
    print("3. makanhepi = Promo diskon 10% hanya untuk kategori Makanan")

def signin():
    global login_username
    global login_password
    os.system('cls||clear')
    print(login)
    print("Silahkan Login Terlebih dahulu!")
    login_username = str(input("Masukkan Username : "))
    login_password = str(getpass.getpass("Masukkan Password : "))

def konfirmasi_beli(produk, nominal):
    print("Anda akan membeli", produk)
    print("Seharga Rp.", nominal)

def voucher_elektronik1(nominal):
    global konfirmasi
    global voucher_elektronik
    konfirmasi = str(input("apakah anda ingin menggunakan voucher? tekan y, jika tidak tekan tombol apa saja : "))
    if konfirmasi == "y":
        input_voucher = (input("Masukkan Kode Voucher : "))
        if input_voucher in voucher_elektronik:
            used = list(voucher_elektronik)
            used.remove(input_voucher)
            voucher_elektronik = tuple(used)
            diskon = nominal * 0.05
            harga = nominal - diskon
            if accounts["saldo_emoney"] >= nominal:
                saldo = accounts["saldo_emoney"] - harga
                accounts["saldo_emoney"] = saldo
                print("Anda mendapatkan diskon sebesar 5% dari harga", nominal,"menjadi", harga)
                print("Pembelian berhasil, Saldo anda sisa :", accounts["saldo_emoney"])
                input("")
            else:
                os.system('cls||clear')
                input("Saldo anda tidak cukup!")

        else:
            os.system('cls||clear')
            input("Voucher salah atau sudah digunakan!")
    else:
        if accounts["saldo_emoney"] >= nominal:
            saldo = accounts["saldo_emoney"] - nominal
            accounts["saldo_emoney"] = saldo
            print("Pembelian anda Berhasil!", "Saldo anda sisa :", accounts["saldo_emoney"])
            input("")
        else:
            os.system('cls||clear')
            input("Saldo anda tidak cukup!")

def voucher_fashion2(nominal):
    global konfirmasi
    global voucher_fashion
    konfirmasi = str(input("apakah anda ingin menggunakan voucher? tekan y, jika tidak tekan tombol apa saja : "))
    if konfirmasi == "y":
        input_voucher = (input("Masukkan Kode Voucher : "))
        if input_voucher in voucher_fashion:
            used = list(voucher_fashion)
            used.remove(input_voucher)
            voucher_fashion = tuple(used)
            diskon = nominal * 0.08
            harga = nominal - diskon
            if accounts["saldo_emoney"] >= nominal:
                saldo = accounts["saldo_emoney"] - harga
                accounts["saldo_emoney"] = saldo
                print("Anda mendapatkan diskon sebesar 8% dari harga", nominal,"menjadi", harga)
                print("Pembelian berhasil, Saldo anda sisa :", accounts["saldo_emoney"])
                input("")
            else:
                os.system('cls||clear')
                input("Saldo anda tidak cukup!")

        else:
            os.system('cls||clear')
            input("Voucher salah atau sudah digunakan!")
    else:
        if accounts["saldo_emoney"] >= nominal:
            saldo = accounts["saldo_emoney"] - nominal
            accounts["saldo_emoney"] = saldo
            print("Pembelian anda Berhasil!", "Saldo anda sisa :", accounts["saldo_emoney"])
            input("")
        else:
            os.system('cls||clear')
            input("Saldo anda tidak cukup!")

def voucher_makanan3(nominal):
    global konfirmasi
    global voucher_makanan
    konfirmasi = str(input("apakah anda ingin menggunakan voucher? tekan y, jika tidak tekan tombol apa saja : "))
    if konfirmasi == "y":
        input_voucher = (input("Masukkan Kode Voucher : "))
        if input_voucher in voucher_makanan:
            used = list(voucher_makanan)
            used.remove(input_voucher)
            voucher_makanan = tuple(used)
            diskon = nominal * 0.10
            harga = nominal - diskon
            if accounts["saldo_emoney"] >= nominal:
                saldo = accounts["saldo_emoney"] - harga
                accounts["saldo_emoney"] = saldo
                print("Anda mendapatkan diskon sebesar 10% dari harga", nominal,"menjadi", harga)
                print("Pembelian berhasil, Saldo anda sisa :", accounts["saldo_emoney"])
                input("")
            else:
                os.system('cls||clear')
                input("Saldo anda tidak cukup!")

        else:
            os.system('cls||clear')
            input("Voucher salah atau sudah digunakan!")
    else:
        if accounts["saldo_emoney"] >= nominal:
            saldo = accounts["saldo_emoney"] - nominal
            accounts["saldo_emoney"] = saldo
            print("Pembelian anda Berhasil!", "Saldo anda sisa :", accounts["saldo_emoney"])
            input("")
        else:
            os.system('cls||clear')
            input("Saldo anda tidak cukup!")

def emoney(paket):
    saldo_emoney = accounts["saldo_emoney"] + paket
    accounts["saldo_emoney"] = saldo_emoney
    print("Saldo E-Money anda sudah ditambahkan Total Saldo :", accounts["saldo_emoney"])
    input("Tekan enter untuk kembali!")

while login < 3:
    signin()
    if login_username == accounts["username"] and login_password == accounts["password"]:
        login_status = "berhasil"
        login = 0
        break
    else:
        os.system('cls||clear')
        input("Masukkan Anda Salah!")
        login += 1
        continue

if login == 3:
    os.system('cls||clear')
    input("Akun anda Terblokir!")
    exit()

while login_status == "berhasil":
    menu()
    pilih_menu = (input("Masukkan Pilihan anda : "))
    if pilih_menu == "1":
        os.system('cls||clear')
        konfirmasi_beli("Handphone", 1000000)
        voucher_elektronik1(1000000)
    elif pilih_menu == "2":
        os.system('cls||clear')
        konfirmasi_beli("Baju Olahraga", 150000)
        voucher_fashion2(150000)
    if pilih_menu == "3":
        konfirmasi_beli("Bakso", 25000)
        voucher_makanan3(25000)
    if pilih_menu == "4":
        os.system('cls||clear')
        print("Halo", accounts["nama"], "! Mau Pilih yang mana?")
        print("1. Saldo 50.000")
        print("2. Saldo 100.000")
        print("3. Kembali")
        pesan_saldo = (input("Masukkan Pilihan Anda : "))
        if pesan_saldo == "1":
            emoney(50000)
        elif pesan_saldo == "2":
            emoney(100000)
        elif pesan_saldo == "3":
            continue
        else:
            os.system('cls||clear')
            print("Masukkan Anda Salah!")
            input("Tekan enter untuk kembali!")
    if pilih_menu == "5":
        os.system('cls||clear')
        promo_today()
        input("")
    if pilih_menu == "6":
        exit()

