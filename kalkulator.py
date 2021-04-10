import os


while True:  
	print ('Kalkulator Sederhana')
	print ('1. Tambah')
	print ('2. Kurang')
	print ('3. Kali')
	print ('4. Bagi')

	a = input('Masukkan jenis perhitungan 1-4 : ')
	b = int (input ('Masukkan angka pertama : '))
	c = int (input ('Masukkan angka kedua : '))

	if a == '1':
		print (b+c)
		d = input('lagi? (y) | tidak? (press any key!) : ')
		if d == 'y':
			os.system('cls||clear')
			continue			
		else:
			break
	elif a == '2':
		print (b-c)
		d = input('lagi? (y) | tidak? (press any key!) : ')
		if d == 'y':
			os.system('cls||clear')
			continue
		else:
			break
	elif a == '3':
		print (b*c)
		d = input('lagi? (y) | tidak? (press any key!) : ')
		if d == 'y':
			os.system('cls||clear')
			continue
		else:
			break
	elif a == '4':
		print (b/c)
		d = input('lagi? (y) | tidak? (press any key!) : ')
		if d == 'y':
			os.system('cls||clear')
			continue
		else:
			break
	else:
		os.system('cls||clear')
		print ('masukkan anda salah!')
		continue
