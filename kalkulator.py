print(20*"=")
print("SELAMAT DATANG \nKALKULATOR SEDERHANA \nBY LUFYANTO")
print(20*"=","\n")

x = float(input("Masukkan angka pertama :"))
y = float(input("Masukkan angka kedua :"))

print("""
PILIHLAH OPERASI PERHITUNGAN DIBAWAH INI
1. Pertambahan
2. Pengurangan
3. Perkalian
4. Pembagian
5. Perpangkatan
6. Modulus
KETIK ANGKA 1,2,3,4,5,6
""")
operator = input()

if operator == "1":
    hasil = x + y
elif operator == "2":
    hasil = x - y
elif operator == "3":
    hasil = x * y
elif operator == "4":
    hasil = x / y
elif operator == "5":
    hasil = x ** y
elif operator == "6":
    hasil = x % y
else:
    print("OPERASI TIDAK SESUAI !!! \nPROGRAM SELESAI")

print(20*"=")
print("HASIL PERHITUNGAN \nKALKULATOR SEDERHANA \nBY LUFYANTO")
print(20*"=","\n")

print("Hasilnya adalah : ", hasil)

print("===== TERIMAKASIH =====")

