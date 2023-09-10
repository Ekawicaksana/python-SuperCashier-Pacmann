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


## 
