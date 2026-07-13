#Menggunakan tanda \
print('Marilah kita shalat jum\'at')
print('isn\'t/Is Not')

#backlash \
print("Data python : C:\\UBSI\\Pemrograman\\string.py")

#tab \t
print("Jarang sholat = \t jauh dari ALLAH")

#backspace
print("Sering sholat = \b dekat dari ALLAH")

#newline \n
print("Nama : LUFYANTO E F \nKelas : 17.1B.24")

#Operasi dan manipulasi string

#1. Menyambung String (CONCATENAT)

first = "Messi"
center = "Referee"
last = "FIFA"
a = "Jujur"

sentence = first +" "+ center +" "+ last
print(sentence)

#2. Operasi Menghitung panjang string (len)

panjang = (len(first))
print(panjang)

#mengecek string didalam string

status = last in sentence
print(f"Apakah Argentina curang \nJawaban = {status}")
status = a in sentence
print(f"Apakah Argentina jujur \nJawaban = {status}")

#mengulang string
print("Argentina = FIFA\n"*10)

#index (mencari)
print("Index ke-0 : "+ sentence[0])
print("Index ke-(-1) : "+ sentence[-1])
print("Index ke 1-7 : "+ sentence[1:8])
print("Index ke 1,3,5,7,9 : "+ sentence[1:10:2])

# item paling kecil
a = "Messi"
print("Paling kecil :" + min(a))
print("Paling besar :" + max(a))

asc = ord("M")
print(str(asc))

#Methode

data = "Messi anak fifa"
jumlah = data.count("s")
print(f"Jumlah 's' pada kata {data} berjumlah {jumlah}")

a = data.upper()
print(a)

a = data.lower()
print(a)

x = "AKU SUKA KAMU"
aku = x.isupper()
print(aku)

"""
isalpha() Mengecek semuanya huruf
isalnum() Huruf dan angka
isdecimal() angka
isspace() spasi, tab, newline \n
istiitle() semua kata dimulai dengan huruf besar
"""

judul = "Hidup Jokowi"
cek = judul.istitle()
print(cek)

#startswith / endswith

cek_a = "Hidup Jokowi".startswith("Hidup")
print(cek_a)
cek_b = "Hidup Jokowi".endswith("Jokowi")
print(cek_b)

# Penggabungan komponen join() split()
# List kumpulan data
pisah = ["Lufyanto", "Eka", "Fahrezi"]
gabung = ' '.join(pisah)
print(pisah)
print(gabung)

gabungan = "Lufyanto Eka Fahrezi"
pisah = gabungan.split(" ")
print(pisah)

# alokasi karakter rjust(), ljust(), center()

kanan = "kanan".rjust(15,"=")
print("'"+kanan+"'")
kanan = "kiri".ljust(15,"=")
print("'"+kanan+"'")
kanan = "tengah".center(15,"=")
print("'"+kanan+"'")

s=kanan.strip("=") #untuk menghilangkan "="
print("'"+s+"'")
