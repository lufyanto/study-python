import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Aplikasi TTK")
window.geometry("500x350")
window.configure(bg="azure2")

def cek():
    nama_input = string_nama.get().strip()

    if nama_input == "":
        teks_sapaan.config(text="Isi dulu namanya, Bosku! .....",fg="red")
    elif nama_input == "Lufyanto Eka Fahrezi":
        teks_sapaan.config(text="Selamat Datang Bos Besar")
    else:
        teks_sapaan.config(text=f"Kamu orang baru ya..., salam kenal {nama_input}")


string_nama = tk.StringVar()

intruksi = ttk.Label(window, text="Siapakah anda?", font=("Arial",12))
intruksi.grid(row=0, column=0, padx=20, pady=25, sticky="e")

kotak_input = ttk.Entry(window, font=("Arial", 12), width=20, textvariable=string_nama)
kotak_input.grid(row=0, column=1, padx=20, pady=25)

tombol = ttk.Button(window, text="Check", command=cek)
tombol.grid(row=1, column=0, columnspan=2, pady=15)

teks_sapaan = tk.Label(window, text="", font=("Arial", 14, "bold", "italic"), bg="azure3")
teks_sapaan.grid(row=2, column=0, columnspan=2, pady=25)

window.mainloop()