import tkinter as tk

window = tk.Tk()
window.title("Aplikasi Pertama")
window.geometry("400x300")
window.configure(bg="royalblue1")

teks_label = tk.Label(window, text="Halo User", font=("Times New Roman",20), fg="royalblue3")

teks_label.pack(pady=30)
teks_label.configure(bg="seashell1")

def tombol():
    teks_utama.config(text="Whatsaaaappp!", fg="red")


teks_utama = tk.Label(window, text="Diamond ef ef 99999", font=("Times New Roman",10) )
teks_utama.pack(pady=15)

tombol_aksi = tk.Button(window, text="Klik Here!", command=tombol ,bg="yellow", fg="black")
tombol_aksi.pack(pady=10)








window.mainloop()