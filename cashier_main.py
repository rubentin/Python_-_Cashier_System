# libraries
from tabulate import tabulate
from datetime import datetime
import numpy as np


class Transaction:
    
    # atribut kelas untuk daftar produk di Toko Andi
    daftar_produk = {
        'Beras' : 50_000, 'Gula' : 20_000,'Tepung' : 10_000,
        'Minyak' : 40_000, 'Garam' : 15_000, 'Daging' : 80_000,
        'Susu' : 60_000, 'Telur' : 30_000, 'Bawang' : 25_000
    }
    
    # atribut kelas untuk menu option pada aplikasi Toko Andi
    menu_option = {
        1 : 'Tambah produk', 2 : 'Update nama produk', 3 : 'Update jumlah produk',
        4 : 'Update harga produk', 5 : 'Hapus produk', 6 : 'Reset transaksi',
        7 : 'Cek keranjang', 8 : 'Total Belanja', 9 : 'Cek diskon', 0 : 'End'
    }
    
    
    def __init__(self, nama):
        self.nama = nama
        random_number = str(np.random.randint(0, 9999, 1)[0])
        date = datetime.today().strftime('%Y-%m-%d')
        self.daftar_belanja = list()
        print(f'Halo, {self.nama.capitalize()}! Selamat datang di Toko Sembako Andi.')
        print(f'ID Transaksi : TR-{self.nama[:3].upper()}/{date}/{random_number}')
        
    
    def display_produk(self):
        headers = ['Nama Produk', 'Harga Satuan']
        print(tabulate(self.daftar_produk.items(), headers = headers))
        
        
    def display_option(self):
        headers = ['', 'Menu Option']
        print(tabulate(self.menu_option.items(), headers = headers))
    
        
    def add_item(self, nama_produk, jumlah_produk, harga_produk):
        self.nama_produk = nama_produk.capitalize()
        self.jumlah_produk = jumlah_produk
        self.harga_produk = harga_produk
        self.total_harga = self.harga_produk * self.jumlah_produk
        self.daftar_belanja.append([self.nama_produk, self.jumlah_produk, self.harga_produk, self.total_harga])
        print(f'Berhasil menambahkan {self.nama_produk} ke dalam keranjang.\n')
    
    
    def check_daftar_belanja(self):
        print('Daftar belanja Anda : ')
        print(tabulate(self.daftar_belanja, headers = ['Nama', 'Qty', 'Harga', 'Total']))
    
    
    def update_nama_produk(self, nama_produk, nama_produk_baru):
        try:
            self.daftar_belanja[self.return_index(nama_produk.capitalize())][0] = nama_produk_baru.capitalize()
            print('Berhasil mengganti nama produk.')
        except:
            print('Nama produk tidak ada dalam daftar belanja.\n')
    
    
    def update_jumlah_produk(self, nama_produk, jumlah_produk_baru):
        try:
            self.daftar_belanja[self.return_index(nama_produk.capitalize())][1] = jumlah_produk_baru
            self.daftar_belanja[self.return_index(nama_produk.capitalize())][3] =\
            self.daftar_belanja[self.return_index(nama_produk.capitalize())][2] * jumlah_produk_baru
            print('Berhasil mengganti jumlah produk.')
        except:
            print('Nama produk tidak ada dalam daftar belanja.\n')

    
    def update_harga_produk(self, nama_produk, harga_produk_baru):
        try:
            self.daftar_belanja[self.return_index(nama_produk.capitalize())][2] = harga_produk_baru
            self.daftar_belanja[self.return_index(nama_produk.capitalize())][3] =\
            self.daftar_belanja[self.return_index(nama_produk.capitalize())][1] * harga_produk_baru
            print('Berhasil mengganti harga produk.')
        except:
            print('Nama produk tidak ada dalam daftar belanja.\n')

    
    def delete_item(self, nama_produk):
        try:
            self.daftar_belanja.pop(self.return_index(nama_produk.capitalize()))
        except:
            print('Nama produk tidak ada dalam daftar belanja.\n')

    
    def return_index(self, nama_produk):
        for i in range(len(self.daftar_belanja)):
            if self.daftar_belanja[i][0] == nama_produk:
                return i
    
    
    def reset_transaksi(self):
        self.daftar_belanja.clear()
        
    
    def check_keranjang(self):
        temp = list()
        for i in range(len(self.daftar_belanja)):
            if self.daftar_belanja[i][0] not in self.daftar_produk.keys():
                print(f'\nProduk {self.daftar_belanja[i][0]} tidak terdapat pada daftar menu.')
            elif self.daftar_belanja[i][0] in self.daftar_produk.keys():
                if self.daftar_belanja[i][2] != self.daftar_produk[self.daftar_belanja[i][0]]:
                    print(f'\nHarga produk {self.daftar_belanja[i][0]} tidak sesuai.')
                elif self.daftar_belanja[i][2] == self.daftar_produk[self.daftar_belanja[i][0]]:
                    temp.append(self.daftar_belanja[i][0])
        if len(temp) == len(self.daftar_belanja) and all(item in self.daftar_produk.keys() for item in temp):
            print('\nPesanan sudah sesuai.')


    def total_belanja(self):
        self.total_price = 0
        for i in range(len(self.daftar_belanja)):
            self.total_price += self.daftar_belanja[i][3]
        print(f'\nTotal belanja Anda adalah Rp. {self.total_price}\n')
        
        
    def check_discount(self):
        if self.total_price > 500_000:
            disc = 10
            final_price = self.total_price * (1 - disc / 100)
            print(f'\nSelamat! Anda mendapat diskon sebesar {disc}%.')
            print(f'Total belanja Anda setelah diskon adalah Rp. {final_price:.0f}\n')
        elif self.total_price > 300_000:
            disc = 8
            final_price = self.total_price * (1 - disc / 100)
            print(f'\nSelamat! Anda mendapat diskon sebesar {disc}%.')
            print(f'Total belanja Anda setelah diskon adalah Rp. {final_price:.0f}\n')
        elif self.total_price > 200_000:
            disc = 5
            final_price = self.total_price * (1 - disc / 100)
            print(f'\nSelamat! Anda mendapat diskon sebesar {disc}%.')
            print(f'Total belanja Anda setelah diskon adalah Rp. {final_price:.0f}\n')
        else:
            final_price = self.total_price
            print('\nTotal belanja Anda belum mencapai batas minimum pemberian diskon.')
            print(f'Total belanja Anda adalah Rp. {self.total_price:.0f}\n')

            
            
# masukkan nama pelanggan
trans_123 = Transaction(input('Silakan masukkan nama: '))

while True:
    option_dipilih = input('Silakan masukkan option belanja: ')
    
    # 1 untuk menambah produk
    if option_dipilih == '1': 
        trans_123.add_item(input('masukkan nama produk: '),
                           int(input('masukkan jumlah produk: ')),
                           int(input('masukkan harga produk: ')))
        trans_123.check_daftar_belanja()
    
    # 2 untuk merubah nama produk
    elif option_dipilih == '2': 
        trans_123.update_nama_produk(input('masukkan nama produk: '), input('masukkan nama produk baru: '))
        trans_123.check_daftar_belanja()
    
    # 3 untuk merubah jumlah produk
    elif option_dipilih == '3':
        trans_123.update_jumlah_produk(input('masukkan nama produk: '), int(input('masukkan jumlah produk baru: ')))
        trans_123.check_daftar_belanja()
    
    # 4 untuk merubah harga produk
    elif option_dipilih == '4':
        trans_123.update_harga_produk(input('masukkan nama produk: '), int(input('masukkan harga produk baru: ')))
        trans_123.check_daftar_belanja()
    
    # 5 untuk menghapus item produk
    elif option_dipilih == '5':
        trans_123.delete_item(input('masukkan nama produk yang ingin dihapus: '))
        trans_123.check_daftar_belanja()
    
    # 6 untuk me-reset transaksi / menghapus semua produk dalam keranjang
    elif option_dipilih == '6':
        trans_123.reset_transaksi()
        trans_123.check_daftar_belanja()
    
    # 7 untuk check nama & harga produk dalam keranjang mengacu pada daftar produk
    elif option_dipilih == '7':
        trans_123.check_keranjang()
        trans_123.check_daftar_belanja()
    
    # 8 untuk melihat total belanja
    elif option_dipilih == '8':
        trans_123.total_belanja()
    
    # 9 untuk check diskon
    elif option_dipilih == '9':
        trans_123.check_discount()
    
    # 0 untuk keluar dari apps
    elif option_dipilih == '0':
        break
    
    else:
        print('Option tidak terdaftar! Silakan masukkan angka 0-9.')
