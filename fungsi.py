
#Pemanggilan tidak bisa di atas def, karena fungsi harus didefinisikan terlebih dahulu sebelum dipanggil

def hello_world():
    #Fungsi menampilkan hello world
    print("Hello, World!")
    print("Lufyanto Eka Fahrezi")

hello_world() #penampilan fungsi hello_world() pertama
hello_world() #penampilan fungsi hello_world() kedua

def fungsi():
    print("Ini adalah fungsi")

fungsi() #pemanggilan fungsi fungsi() pertama

print('\n',"="*40,"FUNGSI DENGAN ARGUMEN","="*40,'\n')

def halo_lufy(nama):
    print(f'Selamat datang {nama}')

halo_lufy("Lufyanto Eka Fahrezi") 
halo_lufy("Agus Sleding")

def tambah(angka_1, angka_2):
    hasil = angka_1 + angka_2
    print(f'Hasil dari {angka_1} + {angka_2} = {hasil}')

tambah(123,456)
tambah(789, 101112)

def say_hi(nama):
    data_peserta = nama.copy()
    for peserta in data_peserta:
        print(f'Selamat datang {peserta}')
    
nama_nama = ['Purbaya','Bahlil','Gibran','Prabowo','Anies']
say_hi(nama_nama)

print('\n',"="*40,"FUNGSI DENGAN RETURN","="*40,'\n')


def fungsi_kuadrat(input_angka):
    output_angka = input_angka**2
    return output_angka

y = fungsi_kuadrat(5)
print(y)

print(fungsi_kuadrat(99))

z = 11 * fungsi_kuadrat(3)
print(z)

def tambah(angka_1, angka_2):
    hasil = angka_1 + angka_2
    return hasil

tambah(300,200)
print(tambah(300,200))

print('\n',"="*40,"FUNGSI DENGAN DEFAULT ARGUMENT","="*40,'\n')

def hola_ganteng(nama = "Mas Bahlil"):
    print(f'Selamat datang {nama}')
hola_ganteng("Mas Gibran")
hola_ganteng() #pemanggilan fungsi hola_ganteng() tanpa argumen, maka akan menggunakan default argument

def asisten(nama = "User", Pesan = "Selamat datang"):
    print(f"Selamat datang {nama}, {Pesan}")

asisten('Lufyanto','Selamat datang di kelas Python')
asisten('Rahmat', 'Selamat datang di kelas Java')
asisten()

def hitung_pangkat(angka, pangkat):
    hasil = angka ** pangkat
    return hasil

print(hitung_pangkat(2,9))

hasil = hitung_pangkat(angka = 3, pangkat = 4)
print(hasil)

def fungsi(input1=1, input2=2, input3=3, input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(10,10,10,10))
print(fungsi(10,10,10))
print(fungsi(10,10))
print(fungsi(10))
