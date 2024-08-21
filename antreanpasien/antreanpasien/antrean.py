import tkinter as tk
from tkinter import ttk
import csv
import pandas as pd

class AntreanPasien:
    def __init__(self, root):
        self.root = root
        self.root.title("Antrean")

        self.antrean = []

        # untuk tempat menginputkan data
        pasien_label = tk.Label(root, text="Nama pasien:")
        pasien_label.pack()
        self.pasien_entry = tk.Entry(root)
        self.pasien_entry.pack()

        alamat_label = tk.Label(root, text="Alamat:")
        alamat_label.pack()
        self.alamat_entry = tk.Entry(root)
        self.alamat_entry.pack()

        telp_label = tk.Label(root, text="No_telp:")
        telp_label.pack()
        self.telp_entry = tk.Entry(root)
        self.telp_entry.pack()

        # Button untuk menambah seluruh data yang telah diinputkan
        add_button = tk.Button(root, text="Submit", command=self.add_antrean)
        add_button.pack(pady=10)

        save_button = tk.Button(root, text="Simpan ke CSV", command=self.save_to_csv)
        save_button.pack(pady=10)

         # Fungsi dibawah ini untuk membuat tabel untuk menampilkan antrean 
        columns = ("Nama_pasien","Alamat","No_telp")
        self.tree = ttk.Treeview(root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(padx=10, pady=10)


        # Load data dari CSV
        self.load_antrean()

    def load_antrean(self):
        try:
            with open("Antrean_pasien.csv", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.tree.insert("", "end", values=(row["Nama_Pasien"], row["Alamat"], row["No_telp"]))
                    self.antrean.append(row)
        except FileNotFoundError:
            # untuk mengantisipasi jika file tidak ditemukan
            pass
   

    def add_antrean(self):
        # untuk Mendapatkan nilai dari data yang sudah diinputkan
        pasien = self.pasien_entry.get()
        alamat = self.alamat_entry.get()
        telp = self.telp_entry.get()
        # untuk menyimpan data diCSV
        self.antrean.append({"Nama_Pasien": pasien, "Alamat": alamat, "No_telp": telp })

        # Menambahkan data pengeluaran ke Treeview
        self.tree.insert("", "end", values=(pasien, alamat, telp))

        # untuk mengosongkan input data setelah ditambahkan
        self.pasien_entry.delete(0, tk.END)
        self.alamat_entry.delete(0, tk.END)
        self.telp_entry.delete(0, tk.END)
     
    def save_to_csv(self):
    # Membuat DataFrame dari data antrean
        df = pd.DataFrame(self.antrean)

    # Menyimpan DataFrame ke dalam file CSV tanpa menyertakan indeks
        df.to_csv("Antrean_pasien.csv", index=False)
        print("Data berhasil disimpan ke Antrean_pasien.csv")

if __name__ == "__main__":
    root = tk.Tk()
    app = AntreanPasien(root)
    root.mainloop()

