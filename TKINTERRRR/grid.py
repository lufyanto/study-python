import tkinter as tk

window = tk.Tk()
window.title("Grid Layout")
window.geometry("500x300")
window.configure(bg="lightblue")

def sapa():
    nama_input = kotak_input.get()
    teks_sapaan.config(text=f"Ahlan wa sahlan, {nama_input}! ", fg="white")




instruksi = tk.Label(window, text="Man' Ana....?", font=("Comic Sans MS",14),fg="white", bg="blue")
instruksi.grid(row=0, column=0, padx=10, pady=25, sticky="e")

kotak_input = tk.Entry(window, font=("Comic Sans MS",14),width=20)
kotak_input.grid(row=0, column=1, padx=10, pady=25)

tombol = tk.Button(window, text="Send..!", command=sapa, bg="blue", font=("Comic Sans MS",10),fg="white")
tombol.grid(row=1,column=0,columnspan=2,pady=10)

teks_sapaan = tk.Label(window, text="", font=("Comic Sans MS",16,"bold"),bg="blue")
teks_sapaan.grid(row=2,column=0,columnspan=2,pady=20)



window.mainloop()