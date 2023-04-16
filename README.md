# Project Background
Andi adalah seorang pemilik supermarket besar di kota besar di Indonesia. Dalam mengambangkan bisnisnya, 
Andi berencana untuk membuat sistem kasir self-service yang bisa diakses setiap pelangganya di mana saja. 
Setiap pelanggan dapat membuat ID transaksi, add item, update item, delete item, reset transaksi, check order, check total belanja, dan check diskon.

Karena keterbatasan sumber daya yang dimiliki, Andi kesulitan untuk merealisasikan rencana tersebut. 
Atas dasar tersebut, project sistem kasir ini dibuat dalam membantu Andi mewujudkan rencana pengembangan bisinis supermarketnya.


# Batasan Masalah
Project sistem kasir ini mencakup pembuatan program kasir sederhana dan merupakan pilot project sistem kasir self-service di supermarket Andi. 
Batasan masalah dalam pengerjaan project ini adalah sbb:
  1.	Sistem kasir self-service diterapkan pada department bahan pokok pangan.
  2.	Feature requirements hanya mengakomodasi kebutuhan yang ditetapkan.
  3.	Tidak ada pencatatan histori transaksi.
  4.	Asumsi bahwa setiap pelanggan melakukan input data sesuai dengan tipe data yang dibutuhkan.
  5.	Debugging tidak mendalam.


# Feature Requirements
  •	Transaksi
    •	Nama 
    •	ID transaksi 
    •	Daftar produk
    •	Menu option

    •	Shopping:
    •	Add item (nama, jumlah, harga produk)
    •	Mengganti nama, jumlah, atau produk (update)
    •	Menghapus produk di keranjang
    •	Reset transaksi
    •	Check order dalam keranjang (mengacu pada daftar produk)
    •	Check total belanja
    •	Check discount
      •	> 200,000 disc 5%
      •	> 300,000 disc 8%
      •	> 500,000 disc 10%
      
![image](https://user-images.githubusercontent.com/96375074/232269056-f4856322-fb6f-4d27-9710-05ca4f8583dd.png)

## membuat transaksi ID
![image](https://user-images.githubusercontent.com/96375074/232310078-310813f5-a973-4230-81d4-50989c67cdd0.png)

## add item
![image](https://user-images.githubusercontent.com/96375074/232311890-6b73521a-1fb4-472d-9908-440a65fb4f82.png)

## update produk
![image](https://user-images.githubusercontent.com/96375074/232312836-b4cd8a9f-eb37-439f-93f5-c0b6752e8c1d.png)

## delete item
![image](https://user-images.githubusercontent.com/96375074/232312982-01c4968f-b76a-48af-9d9d-703106dca651.png)

## reset transaksi
![image](https://user-images.githubusercontent.com/96375074/232313222-7a561111-6ea3-48a0-9417-8e0328f39677.png)

## check transaksi
![image](https://user-images.githubusercontent.com/96375074/232313140-afbf5d4d-efac-4446-826e-c2fafd8e74c2.png)


# Flowchart
![image](https://user-images.githubusercontent.com/96375074/232314878-7b6c2d3e-b9de-4fe8-9dad-c40726a12a73.png)


# Test Case
## Test case 1
![image](https://user-images.githubusercontent.com/96375074/232313415-a1d46924-63d7-4506-9dfc-b52a9c3445eb.png)

## Test case 2
![image](https://user-images.githubusercontent.com/96375074/232313518-5aac82a4-c214-4180-95e7-c394397452de.png)

## Test case 3
![image](https://user-images.githubusercontent.com/96375074/232313695-2a47cc44-02a3-4b50-a3b4-d72cb51cf866.png)

## Test case 4
![image](https://user-images.githubusercontent.com/96375074/232314080-f61558d1-549f-4ed7-9eb3-7daa3b50751e.png)


# Kesimpulan
Project sistem kasir sederhana ini telah berhasil memfasilitasi kebutuhan Andi dalam mengembangkan bisnis supermarket nya.

Pilot project ini masih belum sempurna dan terdapat kekurangan dalam mengantisipasi error.
Dalam pengembangan ke depan, diharapkan dapat melakukan debugging secara lebih spesifik.
