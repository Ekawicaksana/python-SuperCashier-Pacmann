# Project Python : SuperCashier-Pacmann
Pembuatan Project 1 Python di Pacmann AI - Eka Wicaksana Putra - AIML Engineering Batch 15

## Project Background
Andi adalah seorang pemilik supermarket besar di salah satu kota di Indonesia. Andi memiliki
rencana untuk melakukan perbaikan proses bisnis, yaitu Anda akan membuat sistem kasir yang
self-service di supermarket miliknya. Sehingga customer bisa langsung memasukkan item yang
dibeli, jumlah item yang dibeli, dan harga item yang dibeli dan fitur yang lain.
Sehingga customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket
tersebut. Setelah Andi melakukan riset, ternyata Andi memiliki masalah, yaitu Andi membutuhkan
Programmer untuk membuatkan fitur-fitur agar bisa sistem kasir self-service di Supermarket itu
bisa berjalan dengan lancar.

## Feature Requirements
1. Customer membuat ID Transaksi: dengan membuat objek dari class `trnsct_123 = Transaction()`
2. Customer memasukan nama, jumlah, dan harga dari item yang ingin dibeli dengan metode `add_item([<nama item>, <jumlah item>, <harga per item>])`
3. Customer dapat memperbaharui nama, jumlah, atau harga item namun tidak ingin menghapus data yang sudah ada dengan cara :
   - Update nama item: `update_item_name(<nama item>, <update nama item>)`
   - Update jumlah item: `update_item_qty(<nama item>, <update jumlah item>)`
   - Update harga item: `update_item_price(<nama item, <update harga item>>)`
4. Jika batal membeli item, customer dapat melakukan beberapa cara:
   - Menghapus salah satu item dari nama item: `delete_item(<nama item.)`
   - Langsung reset seluruh transaksi: `reset_transaction()`
5. Customer dapat melakukan pengecekan ulang pada item yang sudah diinput secara keseluruhan dengan method `check_order()`
6. Jika sudah selesai pengecekan dan transaksi siap untuk dihitung, dapat menggunakan method `total_price()`

## Module
**Tabulate** : Untuk mencetak format tabel agar hasil yang dikeluarkan dengan method memiliki visual yang lebih baik

## FlowChart
![Flowchart](https://github.com/Ekawicaksana/python-SuperCashier-Pacmann/blob/085604bd5aa0bbf425d0f233c43a8f05f91250cf/Screenshot%202023-09-10%20at%2019.22.08.png)

## Penjelasan Kode Program
- `Transaction()` : Class object untuk menyimpan seluruh fungsi yang telah ditentukan dalam memproses transaksi.
- `add_item()` : Fungsi untuk menambahkan dan menyimpan item.
- `update_item_name()` : Fungsi untuk memperbaharui nama item.
- `update_item_qty()` : Fungsi untuk memperbaharui jumlah item.
- `update_item_price()` : Fungsi memperbaharui harga item.
- `delete_item()` : Fungsi untuk menghapus satu atau lebih item.
- `reset_transaction()` : Fungsi untuk me-reset item yang telah diinput.
- `print_items()` : Fungsi untuk menampilkan daftar items yang telah diinput dan tersimpan.
- `total_price()` : Fungsi untuk menghitung dan menampilkan total belanja, diskon, dan total bayar.



## Test Case
### Test Case 1
Menambahkan Item
![Test Case 1](https://github.com/Ekawicaksana/python-SuperCashier-Pacmann/blob/01cd7a8aed4a8ff98ec7cd7e742d543b3786ef28/Folder/Test%20Case%201.png)

### Test Case 2
Memperbaharui Item
![Test Case 2](https://github.com/Ekawicaksana/python-SuperCashier-Pacmann/blob/7759a12f77d9e03c5740d4d3e86d33ee127bce4d/Folder/Test%20Case%202.png)

### Test Case 3
Menghapus Salah Satu Item
![Test Case 3](https://github.com/Ekawicaksana/python-SuperCashier-Pacmann/blob/2a2d66d9c612552d3325b8bc6dd237f1aa603ed7/Folder/Test%20Case%203.png)

### Test Case 4
Reset Seluruh Transaksi
![Test Case 4](https://github.com/Ekawicaksana/python-SuperCashier-Pacmann/blob/219596dea8dc7e5131deb32e799ce9ac619c8c59/Folder/Test%20Case%204.png)

### Test Case 5
Mencetak Item Yang Sudah Diinput
![Test Case 5](https://github.com/Ekawicaksana/python-SuperCashier-Pacmann/blob/8e834d7587336744f313c2d1c219c37dcd3e1f75/Folder/Test%20Case%205.png)

### Test Case 6
Menghitung Total Belanja
![Test Case 6](https://github.com/Ekawicaksana/python-SuperCashier-Pacmann/blob/c1259c9f2eb1cdc0789cf3c9f3f5b52441e0a1cb/Folder/Test%20Case%206.png)
