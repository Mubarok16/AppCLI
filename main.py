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
      print(i+1,nama[i])
      print('============')
    print('')
  elif nilai == 0:
    print('')
    print('===== data kosong =====')
    print('')
  print('1 : edit data')
  print('2 : hapus data')
  print('99: kembali ke rumah')
  masukan = input('pilihan mu? : ')
  if int(masukan) == 1:
    edit()
  elif int(masukan) == 2:
    hapus()
  elif int(masukan) == 99:
    print('')
    umh()
  else:
    print('')
    print('== salah input!! ==')
    print('')
    hasil()
    
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
    umh()

# fungsi remove
def hapus():
  y = len(nama)
  if y == 0:
    hasil()
  else:
    print('')
    delete = input('No data yang ingin di hapus : ')
    x = int(delete) - 1
    print('===== '+nama[x]+' telah dihapus dari list =====')
    del nama[x]
    hasil()

# fungsi edit list
def edit():
  y = len(nama)
  if y == 0:
    hasil()
  else:  
    print('')
    nomer = input('No data yang ingin di edit = ')
    change = input('masukkan perubahan = ')
    x = int(nomer) - 1
    print('=== '+nama[x]+' berhasil di rubah menjadi '+change+' ===')
    nama[x] = change
    hasil()
  
umh()