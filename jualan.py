import os
import sys
import getpass
import pandas as pd
import openpyxl

book = openpyxl.load_workbook('data.xlsx')
sheet = book.active

pulsa_1 = int(sheet['E2'].value)
data_1 = sheet['F2']
lanjut_pulsa = "n"
username = str(sheet['B2'].value)
password = str(sheet['C2'].value)
nama = str(sheet['D2'].value)
login = "gagal"


while login == "gagal":
	os.system('cls||clear')
	print("Silahkan login terlebih dahulu!")
	login_user = input("Masukkan Username : ")
	pass_user = getpass.getpass("Masukkan Password : ")
	if login_user == username and pass_user == password:
		input("Login Berhasil Selamat Datang!")
		os.system('cls||clear')
		login = "berhasil"
	else:
		input("Username atau Password Salah!")
		os.system('cls||clear')

while login == "berhasil":
	print("Halo",nama,"! Mau Pilih yang mana?")
	print("1. Pulsa")
	print("2. Paket Data")
	print("3. Cek Pulsa dan Paket Data")
	print("4. Top UP Saldo")
	menu = int (input ("Masukkan Pilihan anda : "))
	if menu == 1:
		print("Beli pulsa : ")
		print("1.Beli pulsa Rp.5.000")
		print("2.Beli Pulsa Rp.10.000")
		print("3.Beli Pulsa Rp.20.000")
		print("4.Keluar aplikasi")
		a = int (input("Silahkan pilih pulsa yang mau di beli : "))
		if a == 1:
			sheet['E2'].value = pulsa_1+5000
			book.save('data.xlsx')
			print ("Anda berhasil membeli pulsa Rp.5000 total pulsa ", pulsa_1)
		elif a == 2:
			sheet['E2'].value = pulsa_1+10000
			book.save('data.xlsx')
			print ("Anda berhasil membeli pulsa Rp.10000 total pulsa ", pulsa_1)
		elif a == 3:
			sheet['E2'].value = pulsa_1+20000
			book.save('data.xlsx')
			print ("Anda berhasil membeli pulsa Rp.20000 total pulsa ", pulsa_1)
		else:
			break
	elif menu == 2:
		lanjut_kuota = "y"
	elif menu == 3:
		print("Pulsa anda : ",pulsa_1)
		print("Paket data anda : ",data_1.value)
		input("Press Enter to continue...")
		os.system('cls||clear')
	else:
		print("Pilihan tidak tersedia!")
		continue
