'''GLOBAL dan LOCAL SPOT'''

nama_global = "Lufyanto"

#Akses var dalam fungsi
def fungsi():
    print(f"fungsi menampilkan {nama_global}")

fungsi()

#Akses variabel dalam loop

for i in range (0,5):
    print(f"Loop ke-{i} - {nama_global}")

#percabangan
if True:
    print(f"if menampilkan {nama_global}")

'''LOCAL'''
def fungsi2():
    nama_local = "Nizam Hasbi" # <--- Lokal scope

fungsi2()

def say_lufy():
    print("Hello ", nama)

nama = 'otong'
say_lufy()

#Merubah variabel global

angka = 0
name = 'Lufy'

def ubah(nilai_baru, nama_baru):
    global angka
    global name

    angka = nilai_baru
    name = nama_baru

print(f"Sebelum {angka,name}")
ubah(100,'Lufyanto')
print(f"Sesudah {angka,name}")

##Contoh

angka = 5

for i in range(5,15):
    angka += 1
    angka_dummy = 5

print(angka)
print(angka_dummy)

if True:
    angka = 5
    angka_dummy = 10

print(angka)
print(angka_dummy)

