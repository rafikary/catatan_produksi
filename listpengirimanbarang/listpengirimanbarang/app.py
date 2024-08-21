import tkinter as tk
from tkinter import ttk
import csv
import pandas as pd

class ShippingList:
    def __init__(self, root):
        self.root = root
        self.root.title("List Pengiriman")

        self.pengiriman = []

        # Fungsi dibawah ini untuk membuat tabel untuk menampilkan Pengiriman
        columns = ("No_Pengiriman","Nama_Pengirim","Berat_Barang","Tujuan","Nama_Penerima")
        self.tree = ttk.Treeview(root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(padx=10, pady=10)

        # untuk tempat menginputkan data
        no_label = tk.Label(root, text="No Pengiriman:")
        no_label.pack()
        self.no_entry = tk.Entry(root)
        self.no_entry.pack()

        namapengirim_label = tk.Label(root, text="Nama Pengirim:")
        namapengirim_label.pack()
        self.namapengirim_entry = tk.Entry(root)
        self.namapengirim_entry.pack()

        berat_label = tk.Label(root, text="Berat Barang:")
        berat_label.pack()
        self.berat_entry = tk.Entry(root)
        self.berat_entry.pack()

        tujuan_label = tk.Label(root, text="Tujuan/Alamat:")
        tujuan_label.pack()
        self.tujuan_entry = tk.Entry(root)
        self.tujuan_entry.pack()

        namapenerima_label = tk.Label(root, text="Nama_Penerima:")
        namapenerima_label.pack()
        self.namapenerima_entry = tk.Entry(root)
        self.namapenerima_entry.pack()

        # Button untuk menambah seluruh data yang telah diinputkan
        add_button = tk.Button(root, text="Submit", command=self.add_pengiriman)
        add_button.pack(pady=10)

        save_button = tk.Button(root, text="Simpan ke CSV", command=self.save_to_csv)
        save_button.pack(pady=10)

        # Load data dari CSV
        self.load_pengiriman()

    def load_pengiriman(self):
        try:
            with open("list_pengiriman.csv", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.tree.insert("", "end", values=(row["No_Pengiriman"], row["Nama_Pengirim"], row["Berat_Barang"], row["Tujuan"], row["Nama_Penerima"]))
                    self.pengiriman.append(row)
        except FileNotFoundError:
            # untuk mengantisipasi jika file tidak ditemukan
            pass
   

    def add_pengiriman(self):
        # untuk Mendapatkan nilai dari data yang sudah diinputkan
        no = self.no_entry.get()
        namapengirim = self.namapengirim_entry.get()
        berat = self.berat_entry.get()
        tujuan = self.tujuan_entry.get()
        namapenerima = self.namapenerima_entry.get()

        # untuk menyimpan data diCSV
        self.pengiriman.append({"No_Pengiriman": no, "Nama_Pengirim": namapengirim, "Berat_Barang": berat, "Tujuan":tujuan, "Nama_Penerima":namapenerima })

        # Menambahkan data pengeluaran ke Treeview
        self.tree.insert("", "end", values=(no, namapengirim, berat, tujuan, namapenerima))

        # untuk mengosongkan input data setelah ditambahkan
        self.no_entry.delete(0, tk.END)
        self.namapengirim_entry.delete(0, tk.END)
        self.berat_entry.delete(0, tk.END)
        self.tujuan_entry.delete(0, tk.END)
        self.namapenerima_entry.delete(0, tk.END)
   
    def save_to_csv(self):
    # Membuat DataFrame dari data produksi
        df = pd.DataFrame(self.pengiriman)

    # Menyimpan DataFrame ke dalam file CSV tanpa menyertakan indeks
        df.to_csv("list_pengiriman.csv", index=False)
        print("Data berhasil disimpan ke list_pengiriman.csv")


if __name__ == "__main__":
    root = tk.Tk()
    app = ShippingList(root)
    root.mainloop()

