import tkinter as tk

window = tk.Tk()
window.title("Assalam'alaikum Sobat")
window.geometry("500x400")
window.configure(bg="lightgreen")

def sapa():
    nama_input = kotak_input.get()

    teks_sapaan.config(text=f"Halo, {nama_input}!", fg="darkgreen")

instruksi = tk.Label(window, text="Siapa nama antum : ", font=("Arial",18),fg="white", bg="green")
instruksi.pack(pady=25)

kotak_input = tk.Entry(window, font=("arial", 18), width=30)
kotak_input.pack(pady=10)

tombol = tk.Button(window, text="Klik here", command= sapa, bg="red", fg="white")
tombol.pack(pady=10)

teks_sapaan = tk.Label(window, text="", font=("Arial",18, "bold"), bg="lightgreen")
teks_sapaan.pack(pady=20)

window.mainloop()
