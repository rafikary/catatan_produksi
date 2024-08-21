import tkinter as tk
from tkinter import ttk
import csv
import pandas as pd

class ProductionNotes:
    def __init__(self, root):
        self.root = root
        self.root.title("Catatan Produksi")

        self.produksi = []

        # Fungsi dibawah ini untuk membuat tabel untuk menampilkan produksi
        columns = ("Name_Mesin","Kondisi_Mesin","Jumlah_Produksi","Tanggal_Produksi")
        self.tree = ttk.Treeview(root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(padx=10, pady=10)

        # untuk tempat menginputkan data
        name_label = tk.Label(root, text="Name Mesin:")
        name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        kondisi_label = tk.Label(root, text="Kondisi Mesin:")
        kondisi_label.pack()
        self.kondisi_entry = tk.Entry(root)
        self.kondisi_entry.pack()

        jumlah_label = tk.Label(root, text="Jumlah_Produksi:")
        jumlah_label.pack()
        self.jumlah_entry = tk.Entry(root)
        self.jumlah_entry.pack()

        tanggal_label = tk.Label(root, text="Masukkan tanggal Produksi(Format: YYYY-MM-DD):")
        tanggal_label.pack()
        self.tanggal_entry = tk.Entry(root)
        self.tanggal_entry.pack()

        # Button untuk menambah seluruh data yang telah diinputkan
        add_button = tk.Button(root, text="Submit", command=self.add_produksi)
        add_button.pack(pady=10)

        save_button = tk.Button(root, text="Simpan ke CSV", command=self.save_to_csv)
        save_button.pack(pady=10)

        # Load data dari CSV
        self.load_produksi()

    def load_produksi(self):
        try:
            with open("catatan_produksi.csv", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.tree.insert("", "end", values=(row["Name_Mesin"], row["Kondisi_Mesin"], row["Jumlah_Produksi"], row["Tanggal_produksi"]))
                    self.produksi.append(row)
        except FileNotFoundError:
            # untuk mengantisipasi jika file tidak ditemukan
            pass
   

    def add_produksi(self):
        # untuk Mendapatkan nilai dari data yang sudah diinputkan
        name = self.name_entry.get()
        kondisi = self.kondisi_entry.get()
        jumlah = self.jumlah_entry.get()
        tanggal = self.tanggal_entry.get()

        # untuk menyimpan data diCSV
        self.produksi.append({"Name_Mesin": name, "Kondisi_Mesin": kondisi, "Jumlah_Produksi": jumlah, "Tanggal_produksi":tanggal})

        # Menambahkan data pengeluaran ke Treeview
        self.tree.insert("", "end", values=(name, kondisi, jumlah, tanggal))

        # untuk mengosongkan input data setelah ditambahkan
        self.name_entry.delete(0, tk.END)
        self.kondisi_entry.delete(0, tk.END)
        self.jumlah_entry.delete(0, tk.END)
        self.tanggal_entry.delete(0, tk.END)
   
    def save_to_csv(self):
    # Membuat DataFrame dari data produksi
        df = pd.DataFrame(self.produksi)

    # Menyimpan DataFrame ke dalam file CSV tanpa menyertakan indeks
        df.to_csv("catatan_produksi.csv", index=False)
        print("Data berhasil disimpan ke catatan_produksi.csv")

        # untuk mengosongkan input data setelah ditambahkan
        self.name_entry.delete(0, tk.END)
        self.kondisi_entry.delete(0, tk.END)
        self.jumlah_entry.delete(0, tk.END)
        self.tanggal_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProductionNotes(root)
    root.mainloop()

