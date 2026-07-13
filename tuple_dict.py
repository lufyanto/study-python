#Tuple

data_tp = (1,2,3,4,5)
print(data_tp)  #Tuple tidak dapat dirubah/diapa-apain

#Dictionary -> Associative array
#Identifier -> Key

data_dc = {
    "Lef":"Lufyanto Eka Fahrezi",
    "Ags":"Agus Ganteng",
    "Bdg":"Bandung",
    "ipk": 4
}
print(data_dc["Bdg"])

#Operator Dictionary

data_dict = {
    "cup" : "Ucup Surucup",
    "ags" : "Agus Surahman",
    "dung" : "Dudung Gaming"
}

#Panjang Dictionary
LENDICT = len(data_dict)
print(f"Panjang Dictionary ini adalah {LENDICT}")

#Mengecek key exist / bukan
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"Apakah {KEY}, ada di data ----> {CHECKKEY}")

#Mengakses value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("jkw","Key Tidak ada di Database")) #-----NONE/"" karena tidak ada di dictionary

#Update Data
data_pkkmb = {
    "agr" : "Anggrek",
    "mwr" : "Mawar",
    "psg" : "pisang"
}
print("\n",20*"=","DATA BELUM DI UPDATE",20*"=","\n")
print(data_pkkmb) 
data_pkkmb["mwr"] = "Mawr Hytam"
print("\n",20*"=","DATA SUDAH DI UPDATE",20*"=","\n")
print(data_pkkmb)
data_pkkmb.update({"apl":"Apel"}) #Memperbaharui
print(data_pkkmb) 
del data_pkkmb["apl"]
print(data_pkkmb) 

#looping
print("\n",20*"=","DICTIONARY LOOP",20*"=","\n")
teman_teman = {
    "Lufy" : "Lufyanto E F",
    "Nzm" : "Nizam H",
    "Irh" : "Irhmana",
    "Rai" : "Raihan",
}

for kawan in teman_teman: #-------> HANYA PRINT KEY SAJA
    print(kawan)

keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys(): #-----------> HANYA PRINT VALUE SAJA
    print(teman_teman.get(key))

keys = teman_teman.keys()
values = teman_teman.values()
print(values)

for value in teman_teman.values(): #-------------> HANYA PRINT VALUE AJA
    print(value)

items = teman_teman.items()
for item in teman_teman.items(): #-------------> PRINT DUA-DUA NYA
    print(item)

for key,value in teman_teman.items():
    print(f"KODE = {key}, USER = {value}")

#COPY DICTIONARY

daftar_genre = ["Fiksi Ilmiah", "Misteri", "Fantasi", "Biografi", "Sejarah"]

profil_buku = {
    "judul": "Laskar Pelangi",
    "penulis": "Andrea Hirata",
    "tahun_terbit": 2005,
    "jumlah_halaman": 529,
    "stok_tersedia": True,
    "genre": ["Drama", "Fiksi Remaja"] # Dictionary juga bisa menyimpan list di dalamnya
}

tipe = profil_buku

#POP DICTIONARY (ngapus)
data_judul = tipe.pop("judul")
print(tipe)





