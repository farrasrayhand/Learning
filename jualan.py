import os

while True:
	saldo = 0
	print (Mau Top UP Saldo berapa?)
	print (1. Saldo 5000)
	print (2. Saldo 10000)
	print (3. Saldo 50000)
	print (4. Saldo 100000)
	a = int (input ('Masukkan Pilihan anda : '))

	if a == '1':
		saldo+5000
		print ('saldo anda = 'saldo)
		d = input('lagi? (y) : ')
		if d == 'y':
			continue
			os.system('cls||clear')
		else:
			break
	elif a == '2':
		saldo+5000
		print ('saldo anda = 'saldo)
		d = input('lagi? (y) : ')
		if d == 'y':
			continue
			os.system('cls||clear')
		else:
			break
	elif a == '3':
		saldo+5000
		print ('saldo anda = 'saldo)
		d = input('lagi? (y) : ')
		if d == 'y':
			continue
			os.system('cls||clear')
		else:
			break
	elif a == '4':
		print (a/b)
		d = input('lagi? (y) : ')
		if d == 'y':
			continue
			os.system('cls||clear')
		else:
			break
	else:
		os.system('cls||clear')
		print ('masukkan anda salah!')
		continue