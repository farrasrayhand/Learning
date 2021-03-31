import os

while True:
	a = int (input ('Masukkan angka pertama : '))
	b = int (input ('Masukkan angka kedua : '))
	c = input('Masukkan jenis perhitungan (+, -, *, /) : ')

	if c == '+':
		print (a+b)
		d = input('lagi? (y) : ')
		if d == 'y':
			continue
			os.system('cls||clear')
		else:
			break
	elif c == '-':
		print (a-b)
		d = input('lagi? (y) : ')
		if d == 'y':
			continue
			os.system('cls||clear')
		else:
			break
	elif c == '*':
		print (a*b)
		d = input('lagi? (y) : ')
		if d == 'y':
			continue
			os.system('cls||clear')
		else:
			break
	elif c == '/':
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