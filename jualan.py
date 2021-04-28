import os
import sys
import getpass
import pandas as pd
import openpyxl


book = openpyxl.load_workbook('data.xlsx')
sheet = book.active

pulsa_1 = int(sheet['E2'].value)
data_1 = int(sheet['F2'].value)
saldo_1 = int(sheet['G2'].value)
lanjut_pulsa = "n"
username = str(sheet['B2'].value)
password = str(sheet['C2'].value)
nama = str(sheet['D2'].value)
login = "gagal"

os.system('cls||clear')
print ("-----------------------------------------------------")
print ("------------JUAL BELI PULSA DAN PAKET DATA-----------")
print ("-----------------------------------------------------\n\n")
print ("Note : Aplikasi memiliki bug ketika melakukan transaksi, saldo, pulsa atau paket data tidak terupdate secara realtime\nJadi harus direstart dahulu aplikasinya agar transaksi yang sudah dilakukan terupdate pada sistem!\n\nCoded by : Muhammad Farras Rayhand\nNIM : 2041007\n\nuser : demo\npass : demo\n\n")
while login == "gagal":
	print("Silahkan login terlebih dahulu!")
	login_user = input("Masukkan Username : ")
	pass_user = getpass.getpass("Masukkan Password : ")
	if login_user == username and pass_user == password:
		os.system('cls||clear')
		print("Login Berhasil Selamat Datang!")
		login = "berhasil"
	else:
		input("Username atau Password Salah!")
		os.system('cls||clear')

while login == "berhasil":
	print("Halo",nama,"! Mau Pilih yang mana?")
	print("1. Pulsa")
	print("2. Paket Data")
	print("3. Cek Pulsa dan Paket Data dan Saldo")
	print("4. Top UP Saldo")
	print("5.Keluar")
	menu = (input ("Masukkan Pilihan anda : "))
	if menu == "1":
		os.system('cls||clear')
		print("Beli pulsa : ")
		print("1.Beli pulsa Rp.5.000")
		print("2.Beli Pulsa Rp.10.000")
		print("3.Beli Pulsa Rp.20.000")
		print("4.Kembali")
		a = (input("Silahkan pilih pulsa yang mau di beli : "))
		if a == "1":
			if saldo_1 >= 5000:
				sheet['G2'].value = saldo_1 - 5000
				sheet['E2'].value = pulsa_1+5000
				book.save('data.xlsx')
				print ("Anda berhasil membeli pulsa Rp.5000 total pulsa ", pulsa_1)
			else:
				print("Maaf saldo anda tidak cukup, Saldo anda :",saldo_1)
		elif a == "2":
			if saldo_1 >= 10000:
				sheet['G2'].value = saldo_1 - 10000
				sheet['E2'].value = pulsa_1+10000
				book.save('data.xlsx')
				print ("Anda berhasil membeli pulsa Rp.10000 total pulsa ", pulsa_1)
			else:
				print("Maaf saldo anda tidak cukup, Saldo anda :",saldo_1)
		elif a == "3":
			if saldo_1 >= 5000:
				sheet['G2'].value = saldo_1 - 20000
				sheet['E2'].value = pulsa_1+20000
				book.save('data.xlsx')
				print ("Anda berhasil membeli pulsa Rp.20000 total pulsa ", pulsa_1)
			else:
				print("Maaf saldo anda tidak cukup, Saldo anda :",saldo_1)
		else:
			os.system('cls||clear')
			continue
	elif menu == "2":
		os.system('cls||clear')
		print("1. 1GB = 5000 Pulsa")
		print("2. 3GB = 10000 Pulsa")
		print("3. 5GB = 20000 Pulsa")
		b = (input("Silahkan pilih kuota yang mau di beli : "))
		if b == "1":
			if pulsa_1 >= 5000:
				sheet['E2'].value = pulsa_1 - 5000
				sheet['F2'].value = data_1 + 1
				book.save('data.xlsx')
				print ("Anda berhasil membeli kuota 1GB total kuota", data_1,"GB")
			else:
				print("Maaf pulsa anda tidak cukup, Pulsa anda :",pulsa_1)
		elif b == "2":
			if pulsa_1 >= 10000:
				sheet['E2'].value = pulsa_1 - 10000
				sheet['F2'].value = data_1 + 3
				book.save('data.xlsx')
				print ("Anda berhasil membeli kuota 1GB total kuota", data_1,"GB")
			else:
				print("Maaf pulsa anda tidak cukup, Pulsa anda :",pulsa_1)
		if b == "3":
			if pulsa_1 >= 20000:
				sheet['E2'].value = pulsa_1 - 20000
				sheet['F2'].value = data_1 + 5
				book.save('data.xlsx')
				print ("Anda berhasil membeli kuota 1GB total kuota", data_1,"GB")
			else:
				print("Maaf pulsa anda tidak cukup, Pulsa anda :",pulsa_1)
	elif menu == "3":
		os.system('cls||clear')
		print("Pulsa anda : ",pulsa_1)
		print("Paket data anda : ",data_1,"GB")
		print("Saldo anda : ",saldo_1)
		input("Press Enter to continue...")
		os.system('cls||clear')
	elif menu == "4":
		os.system('cls||clear')
		print("1. Saldo Rp.50.000")
		print("2. Saldo Rp. 100.000")
		print("3. Kembali")
		d = (input("Silahkan pilih saldo yang mau di beli : "))
		if d == "1":
			sheet['G2'].value = saldo_1+50000
			book.save('data.xlsx')
			os.system('cls||clear')
			print("Saldo telah berhasil di TopUP, Saldo anda :", saldo_1)
		elif d == "2":
			sheet['G2'].value = saldo_1+100000
			book.save('data.xlsx')
			os.system('cls||clear')
			print("Saldo telah berhasil di TopUP, Saldo anda :", saldo_1)
		elif d == "3":
			os.system('cls||clear')
			continue
		else:
			print("Pilihan tidak tersedia!")
			os.system('cls||clear')
			continue
	elif menu == "5":
		break
	else:
		print("Pilihan tidak tersedia!")
		os.system('cls||clear')
		continue
