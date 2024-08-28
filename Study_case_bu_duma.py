# # study case kabisat
#
# a = 1596
#
# while a < 2024 :
#     if a == a:
#         a += 4
#         if a == 1700 & 1800:
#             print( str(a) + ' ini bukan tahun kabisat')
#         elif  a % 400 == 0:
#             print( str(a) + ' ini adalah tahun kabisat')
#         elif a % 100 == 0:
#             print(str(a) + ' ini bukan tahun kabisat')
#         elif a % 4 == 0:
#             print(str(a) + ' ini adalah tahun kabisat')
#     else:
#         a += 4
#
# # study case buku
#
# buku = input('masukan jumlah buku yang di beli: ')
#
# eksemplar = int(buku) * 10
# harga = eksemplar * 5000
#
# if eksemplar <= 100:
#
#     print('-----------------------------------------')
#     print('anda tidak mendapat kan diskon          |')
#     print('-----------------------------------------')
#     print('nominal yang harus anda bayar')
#     print('jumlah buku: ' + str(buku))
#     print('jumlah eksemplar: ' + str(eksemplar) )
#     print('nominal bayar: ' + str(harga) )
#     print('-----------------------------------------')
#
# elif eksemplar <= 200 :
#
#     diskon_1= harga * 5 / 100
#     diskon_2= harga * 15 / 100
#     diskon = diskon_2 + diskon_1
#     harga = harga - diskon
#
#     print('-----------------------------------------')
#     print('anda mendapat kan diskon                |')
#     print('-----------------------------------------')
#     print('100 pertama adalah 5%                   |')
#     print('100 selanjutnya adalah 15%              |')
#     print('-----------------------------------------')
#     print('nominal yang harus anda bayar')
#     print('jumlah buku: ' + str(buku))
#     print('jumlah eksemplar: ' + str(eksemplar) )
#     print('diskon 100 pertama: ' + str(diskon_1) )
#     print('diskon 100 selanjutnya: ' + str(diskon_2) )
#     print('nominal bayar: ' + str(harga) )
#     print('-----------------------------------------')
#
# elif eksemplar > 200:
#
#     diskon_1= harga * 7 / 100
#     diskon_2= harga * 17 / 100
#     diskon_3= harga * 27 / 100
#     diskon = diskon_2 + diskon_1 + diskon_3
#     harga = harga - diskon
#
#     print('-----------------------------------------')
#     print('anda mendapat kan diskon                |')
#     print('-----------------------------------------')
#     print('100 pertama adalah 7%                   |')
#     print('100 kedua adalah 17%                    |')
#     print('100 selanjutnya adalah 25%              |')
#     print('-----------------------------------------')
#     print('nominal yang harus anda bayar')
#     print('jumlah buku: ' + str(buku))
#     print('jumlah eksemplar: ' + str(eksemplar) )
#     print('diskon 100 pertama: ' + str(diskon_1) )
#     print('diskon 100 kedua: ' + str(diskon_2) )
#     print('diskon 100 selanjutnya: ' + str(diskon_3) )
#     print('nominal bayar: ' + str(harga) )
#     print('-----------------------------------------')
#
# nominal_bayar = input('bayar sesuai dengan harga: ')
#
# yg_dibayar = harga - int(nominal_bayar)
#
# if yg_dibayar == 0 :
#     print('Anda telah melunasi buku tersebut')
# else:
#     print('nominal anda kurang')
#     print('apakah anda ingin melakukan transaksi kembali ?')
#     print('1 Jika iyaa')
#     print('2 Jika tidak')
#
#     pernyataan = input('apakah anda ingin melanjutkan transaksi ? ')
#
#     if pernyataan == '1':
#         print('nominal yang kurang ' + str(yg_dibayar))
#         input_ulang = input('masukan nominal bayar: ')
#
#         lunas = int(input_ulang) - yg_dibayar
#
#         if lunas == 0:
#             print('anda telah melunasi sisa nya ')
#         else:
#             print('mohon bayar dengan uang yang pas , atau kembalikan buku!')
#     else:
#         print('mohon kembalikan buku ke rak nya')
#
#
# # mencari angka terbersar
# angka_1 = input('masukan angka pertama: ')
# angka_2 = input('masukan angka kedua: ')
# angka_3 = input('masukan angka ketiga: ')
#
# if angka_1 >= angka_2:
#     if angka_1 >= angka_3:
#         print('angka terbesar adalah 1 : ' + str(angka_1))
# elif angka_2 >= angka_3:
#     print('angka terbesar adalah 2 : ' + str(angka_2))
# elif angka_3:
#     print('angka terbesar adalah 3 : ' + str(angka_3))
#
# #mencari ganjil genap dan negatif positif
#
# bil = input('masukan no yang anda inginkan: ')
#
# if int(bil) == 0:
#     print('angka 0 tidak berlaku, harap masukan kembali data ')
#     bil = input('masukan no yang anda inginkan: ')
#     if int(bil) % 2 == 0:
#         print('angka ini adalah genap : ' + bil)
#         if bil > '0':
#             print('ini adalah bilangan positif : ' + bil)
#         elif bil < '0':
#             print('ini adalah bilangan NEGATIF : ' + bil)
#     elif int(bil) % 2 == 1:
#         print('angka ini adalah ganjil : ' + bil)
#         if bil > '0':
#             print('ini adalah bilangan positif : ' + bil)
#         elif bil < '0':
#             print('ini adalah bilangan NEGATIF : ' + bil)
# else:
#     if int(bil) % 2 == 0:
#         print('angka ini adalah genap : ' + bil)
#         if bil > '0':
#             print('ini adalah bilangan positif : ' + bil)
#         elif bil < '0':
#             print('ini adalah bilangan NEGATIF : ' + bil)
#     elif int(bil) % 2 == 1:
#         print('angka ini adalah ganjil : ' + bil)
#         if bil > '0':
#             print('ini adalah bilangan positif : ' + bil)
#         elif bil < '0':
#             print('ini adalah bilangan NEGATIF : ' + bil)
# on of lampu
# print('------------------------------------')
# print('masukan angka')
# print('masukan angka 0 jika anda ingin mematikan lampu')
# print('masukan angka 1 jika anda ingin menyalakan lampu')
# print('------------------------------------')
#
#
# kondisi_lampu = input('masukan angka saklar: ')
#
# if int(kondisi_lampu) == 0:
#     print('lampu anda mati')
# elif int(kondisi_lampu) == 1:
#     print('lampu anda menyala')
# else:
#     print('ada kesalahan coba masukan kembali')
#
#     kondisi_lampu = input('masukan angka saklar: ')
#
#     if int(kondisi_lampu) == 0:
#         print('lampu anda mati')
#     elif int(kondisi_lampu) == 1:
#         print('lampu anda menyala')
#
# #input 3 angka dan jika melebihi 100rb maka diskon 10%
# print('------------------------------------')
# print('masukan angka')
# print('------------------------------------')
#
#
# harga_barang1 = input('masukan barang pertama: ')
# harga_barang2 = input('masukan barang kedua: ')
# harga_barang3 = input('masukan barang ketiga: ')
#
# harga = int(harga_barang1) + int(harga_barang2) + int(harga_barang3)
#
# if harga > 100000:
#     diskon = harga * 10 / 100
#     after_disk = harga - diskon
#
#     print('anda mendapat kan diskon sebesar 10 %')
#     print('harga yang harus anda bayar: ' + str(after_disk))
#
# else:
#     print('harga yang harus anda bayar: ' + str(harga))
#
# #input 3 angka dan jika melebihi 100rb maka diskon 10%
# print('------------------------------------')
# print('masukan angka')
# print('------------------------------------')
#
#
# lembur = input('masukan jam lembur anda: ')
#
# if int(lembur) < 6:
#     print('Jam lembur anda : ' + str(lembur) + ' jam')
#     print('anda mendapat kan gaji lembur sebesar Rp. 100.000')
# elif int(lembur) == 6:
#     print('Jam lembur anda : ' + str(lembur) + ' jam')
#     print('anda mendapat kan gaji lembur sebesar Rp. 200.000')
# elif int(lembur) > 6:
#     print('Jam lembur anda : ' + str(lembur) + ' jam')
#     print('anda mendapat kan gaji lembur sebesar Rp. 300.000')
#
#
