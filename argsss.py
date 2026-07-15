'''*ARGS'''

def fungsi(nama,tinggi,berat):
    print(f"{nama} Punya tinggi {tinggi} dan berat {berat}")

fungsi("Budi", 170, 60)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} Punya tinggi {tinggi} dan berat {berat}")

fungsi(["Budianto", 175, 50])

#Kenalan sama *args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} Punya tinggi {tinggi} dan berat {berat}")

fungsi("Asep",160,78)

#studi kasus *args

def tambah(*data):
    #Tipe datanya tuple
    output = 100
    for angka in data:
        output += angka
    return output
    


hasil = tambah(10,20,30,40,50)
print(f"Hasil penjumlahan = {hasil}")

hasil = tambah(10,20,30,40,50,60,70,80,90,100)
print(f"Hasil penjumlahan = {hasil}")