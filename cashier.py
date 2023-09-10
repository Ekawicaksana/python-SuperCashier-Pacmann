#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from tabulate import tabulate


# In[2]:


# Membuat class transaction untuk dictionary transaksi
class Transaction:
    def __init__(self):
        # Mendefinisikan dictionary transaksi
        self.list_item = {}
        self.input = True
    
    
    def add_item(self, name, qty, price):
        # Fungsi untuk menambahkan item ke dalam dictionary
        dict_add = {name: [qty, price]}
        self.list_item.update(dict_add)
        print(f"Item yang dibeli adalah: {self.list_item}.")
        
    
    def update_item_name(self, name, new_name):
        # Fungsi untuk memperbaharui nama item di dalam dictionary
        input_name = self.list_item[name]
        self.list_item.pop(name)
        self.list_item.update({new_name: input_name})
        print(self.list_item)
    
    
    def update_item_qty(self, name, new_qty):
        # Fungsi untuk memperbaharui qty item di dalam dictionary
        if type(new_qty) != int:
            print("Jumlah item harus berisikan angka!")
        else:
            self.list_item[name][0] = new_qty
            print(self.list_item)
    
    
    def update_item_price(self, name, new_price):
        # Fungsi untuk memperbaharui harga item di dalam dictionary
        if type(new_price) != int:
            print("Harga item harus berisikan angka!")
        else:
            self.list_item[name][0] = new_price
            print(self.list_item)
         
    
    def delete_item(self, name):
        #  Fungsi untuk menghapus salah satu item di dalam dictionary
        try:
            self.list_item.pop(name)
            print(f"Menghapus pesanan {name}.")
            print(self.list_item)
        except KeyError:
            print(f"{name} tidak ada dalam daftar pesanan.")
    
    
    def reset_transaction(self):
        # Fungsi untuk menghapus seluruh item di dalam dictionary
        self.list_item = self.list_item.clear
        print("Seluruh item telah berhasil terhapus")
    
    
    def print_item(self):
        # Menampilkan seluruh item di dictionary transaksi
        try:
            table_item = pd.DataFrame(self.list_item).T
            headers = ["Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"]
            print(tabulate(table_item, headers, tablefmt="github"))
        except:
            print("Belum ada pesanan.")
    
    
    def total_price(self):
        # Fungsi untuk menghitung dan menampilkan total bayar & diskon
        self.print_item()
        total_belanja = 0
        for item in self.list_item:
            total_belanja += self.list_item[item][1]
        
        # Menghitung total bayar dan diskon sesuai dengan total belanja
        if total_belanja > 500_000:
            diskon = int(total_belanja * 0.1)
            total_belanja = int(total_belanja - diskon)
            print(f"Selamat, Anda mendapatkan diskon 10% sebesar Rp {diskon}.")
            print(f"Total belanja Anda adalah Rp {total_belanja}.")
            
        elif total_belanja > 300_000:
            diskon = int(total_belanja * 0.08)
            total_belanja = int(total_belanja - diskon)
            print(f"Selamat, Anda mendapatkan diskon 8% sebesar Rp {diskon}.")
            print(f"Total belanja Anda adalah Rp {total_belanja}.")
            
        elif total_belanja > 200_000:
            diskon = int(total_belanja * 0.05)
            total_belanja = int(total_belanja - diskon)
            print(f"Selamat, Anda mendapatkan diskon 5% sebesar Rp {diskon}.")
            print(f"Total belanja Anda adalah Rp {total_belanja}.")
            
        else:
            print(f"Total belanja Anda adalah Rp {total_belanja}.")

