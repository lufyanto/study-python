#Operator Penugasan
x = 2
x+=2
print(x)

x = 5
x*=10
print(x)

#Looping dengan operator penugasan
x=0
while(x <= 5):
    print("HIDUP JOKOWI")
    x += 1
else:
    print("JOKOWI LENGSER")

#Operator Logika
#Rapot kelulusan sekolah
#Jika ada yg remedial 1 = TIDAK LULUS

# nama = input("Masukkan Nama Siswa-i => ")
# nis = str(input("Masukkan NIS => "))
# nilai_a = int(input("Masukkan Nilai Pertama => "))
# nilai_b = int(input("Masukkan Nilai Kedua => "))
# nilai_c = int(input("Masukkan Nilai Ketiga => "))
# nilai_d = int(input("Masukkan Nilai Keempat => "))
# nilai_e = int(input("Masukkan Nilai Kelima => "))

# if(nilai_a>=80 and nilai_b>=80 and nilai_c>=80 and nilai_d>=80 and nilai_e>=80):
#     hasil = "LULUS"
# else :
#     hasil = "TIDAK LULUS"

# print("="*30)
# print("RAPOT KELULUSAN SISWA")
# print("="*30)
# print(f"Nama: {nama}")
# print(f"NIS: {nis}")
# print(f"Nilai Pertama: {nilai_a}")
# print(f"Nilai Kedua: {nilai_b}")
# print(f"Nilai Ketiga: {nilai_c}")
# print(f"Nilai Keempat: {nilai_d}")
# print(f"Nilai Kelima: {nilai_e}")
# print(f"Hasil: {hasil}")

lebar = 50
tengah = 10

print("="*lebar)
print(f"Toko Mainan Anak".center(lebar))
nama = input("Masukkan Nama Pembeli => ")
kode_barang = input("Masukkan Kode Barang => ")
harga_barang = int(input("Masukkan Harga Barang => "))
jumlah_barang = int(input("Masukkan Jumlah Barang => "))
total_harga = harga_barang * jumlah_barang
print("\n")
print("="*lebar)
print(f"Nota Pembelian".center(lebar))
print("="*lebar)
print(f"Nama Pembeli\t: {nama}")
print(f"Kode Barang\t: {kode_barang}")
print(f"Harga Barang\t: {harga_barang}")
print(f"Jumlah Barang\t: {jumlah_barang}")
print(f"Total Harga\t: {total_harga}")