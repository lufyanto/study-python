#Continue, pass, break
#Pass adalah dummy dia tidak dieksekusi

print("====== CONTINUE =====")

n = 0

print(f"Angka sekarang --->  {n}")

while n < 5:
    n += 1
    print(f"Angka saat ini ---> {n}") #AKSI PERTAMA
    if n == 3:
        print("LENOVO MANTAP")
        continue #kembali keatas
    print("==========") # AKSI KEDUA

print("====== BREAK =====")

x = int(input("Hitung sampai :  "))
y = 0

while y < x:
    y += 1
    print(f"Angke ke ---> {y}") #aksi pertama

    if y == 900:
        print("OKE KETEMU !") #aksi ketika kondisi sama
        break #print aksi kondisi lalu end

    print("==============") #aksi kedua

print("=== PROGRAM SELESAI ===")

