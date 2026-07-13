nama = "Lufy"
format_str = f"Hello {nama}"
print(format_str)

angka = 2007
format_str = f"Lahir Tahun {angka}"
print(format_str)

laptop = 500000000
format_str = f"Harganya {laptop:,}"
print(format_str)

ipk = 38.99
nilai = 100
lufy = f"IPK Lufy = {ipk:.2f}"
lu = f"Nilai Lufy = {nilai:+d}"
print(lufy)
print(lu)

harga = 3000000
jumlah = 9
total = f"Harga Total : Rp.{harga*jumlah:,}"
print(total)

angka = 135
f_binary = f"Binary = {bin(angka)}"
f_octal = f"Octal = {oct(angka)}"
f_hex = f"Hex = {hex(angka)}"

print(f_binary)
print(f_octal)
print(f_hex)
