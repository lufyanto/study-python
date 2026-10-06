#String,Bilangan & Operator

var1 = 'Hello Python'
var2 = "Coding itu menyenangkan, bukan?"
print(var1)
print(var2)

#Mengakses Nilai String
#Mengakses Nilai String menggunakan INDEKS ([])
#Indeks selalu dimulai dari angka 0

print(f"Posisi Huruf ke-1 => {var1[0]}")
print(f"Penggalan kata => {var2[0:6]}")
#Rumus : variabel[awal:akhir-1(angka k-6 tidak terinput)]

#Meng-Update String
var_awal = 'Awalnya Andi kuliah di UI'
var_andi = var_awal[-2]

print(var_awal)
print(var_andi)

var_ubah = 'Dia gagal, dan memilih kuliah ' + var_awal[-2]+'BS'+ var_awal[-1]
print(var_ubah)

#Menggabungkan dan Menggadakan String
kata1 = "Lufy"
kata2 = "Kuliah"
kata3 = "UBSI Aja..."
gabungKata = kata1+' '+kata2+' '+kata3
print(gabungKata)

#Mengetahui Panjang String
kata_kata = "Hidup Adalah_anugerah1"
print(f"Panjang kalimat ini => {kata_kata} adalah [{len(kata_kata)}]")
# Note => spasi dan karakter spesial juga 

#Karakter Escape
# print("Hello, what's your name?")  <=== PASTI ERROR

print("What\'s your name?")
print('''What's your name?''')
print("\"what's\" your name?")
