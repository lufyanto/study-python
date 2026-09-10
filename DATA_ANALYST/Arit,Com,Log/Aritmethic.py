import math


print("===== ARITMATIKA PYTHON =====\n")

# bilanganA = int(input("Masukkan Bilangan Pertama = "))

# print("----- HASIL -----\n")

# print(f"Hasilnya => {bilanganA**2}")

print("\n===== SOAL MATEMATIKA =====\n")
soalPertama = 80-90+75*5/(2+34)-2

print(f"Jawaban ==> {soalPertama}")

print(f"Hasil dari pangkat negatif => {-4 ** 2}")
print(f"Hasil dari pangkat negatif dengan tanda kurung => {(-4) ** 2}")
print(f"Pangkat negatif -----> {3 ** -3}")
print(f"Pangkat Pecahan ---> {27 ** (1/3), 3}")
print(math.isclose(27 ** (1/3), 3))

print("\nPerpangkatan dengan POW\n")
print("Hasil dari 3 pangkat 3 => ", pow(3,3))
print("Hasil dari -3 pangkat 3 => ", pow(-3,4))


print("\n\n===== DIVION PYTHON =====\n")


print("1. Division Biasa (/)")
print("Hasil dari 40 dibagi 4 => ", 40.0 / 4.0,)
print("Hasil dari 100 dibagi 30 => ", 100 / 30, "\n")
print("2. Division Double (Floor Division (//))")
print("Hasil dari 100 dibagi 30 => ", 100 // 30, "\n")
print("3. Modulus (%)")
print("Sisa bagi dari 8 dibagi 3 => ", 8 % 3 ,"\n")

a = 2
b = 7

print(a * (b // a) + (b % a))

# print("\n\n========== CEK PLAT GANJIL GENAP ==========\n")

# platKendaraan = float(input("Masukkan no Plat Kendaraan XXXX "))

# if platKendaraan % 2 == 0:
#     print("Plat anda GENAP")
# else :
#     print("plat anda GANJIL")


print(0.3/0.1)

print(f"Hasil bagi dari 11 dibagi 2 ", divmod(11, 2))
print(f"Hasil bagi dan sisa dari 100 / 7 ", divmod(100,7))

print("\n\n========== ROUND ROBIN SCHEDULING ==========\n\n")

print("----------------------------------------------------")

servers = ["Office", "Accounting", "Engginer", "Production", "Packing"]

for req_id in range(50):
    server = servers[req_id % len(servers)]
    print(f"[INFO] Request {req_id} -> {server} Complete.....")

cekTahunKabisat = 2028

if cekTahunKabisat % 4 == 0:
    print("Tahun Kabisat")
else :
    print("Bukan tahun kabisat")

