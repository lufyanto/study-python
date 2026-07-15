'''KWARGS'''

'''FUNGSI BIASA'''

def fungsi(nama,tinggi,berat):
    print(f"{nama} Punya tinggi {tinggi} dan berat {berat}")

fungsi("Lufyanto", 161, 54)

'''FUNGSI DENGAN KWARGS'''
def fungsi(**kwargs):
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} Punya tinggi {tinggi} dan berat {berat}")

fungsi(nama="Lufy",tinggi=160,berat=50)

#STUDI KASUS

def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka

    else:
        print("Pilihan tidak tersedia")

    return output
    


hasil = math(10,20,30,40,50,option="tambah")
print(hasil)

hasil = math(10,20,30,40,50,option="kali")
print(hasil)