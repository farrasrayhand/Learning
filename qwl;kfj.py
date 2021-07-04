import os
from os import system
import random
import getpass

system("title " + "Toko Farras 2041007")

login = 0

voucher_elektronik = ('antigaptek')
voucher_fashion = ('kaumbranded')
voucher_makanan = ('makanhepi')

accounts = {
    "username": "farras",
    "password": "2041007",
    "nama": "Muhammad Farras Rayhand",
    "saldo_emoney": 100000
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
        
