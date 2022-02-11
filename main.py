nama = []

# fungsi input
def data():
  x = 'y'
  while(x == 'y'):
    masukan = input('masukkan nama : ')
    nama.append(masukan)
    print('=====================')
    print('y : untuk lanjut input')
    print('t : untuk tidak')      
    x = input('  : ')
    print('=====================')
  if x == 't':
    umh()

# hasil sebagai penyimpanan yg user input
def hasil():  
  nilai = len(nama)
  if nilai != 0:
    print('')
    print('')
    for i in range(nilai):
      print(nama[i])
      print('============')
    print('')
    umh()
  elif nilai == 0:
    print('')
    print('===== data kosong =====')
    print('')
    umh()
    
# fungsi home
def umh():
  print('selamat datang di apps')
  print('what wich we can help? ')
  print('1 : masukkan data')
  print('2 : lihat data')
  print('99: selesai')
  masuk = input('pilihan anda = ')
  if int(masuk) == 1:
    data()
  elif int(masuk) == 2:
    hasil()
  elif int(masuk) == 99:
    print('')
    print('===== terimakasih =====')
    print('')
  else:
    print('')
    print('==== yang anda masukkan salah!! ====')
    print('')
    salah()

# jika ada kesalahan input user maka akan return ke fngsi umh
def salah():
  umh()



umh()