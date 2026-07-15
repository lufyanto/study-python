#Lambda func

def f_kuadrat(angka):
    return angka ** 2

print(f"Hasil fungsi kuadrat = {f_kuadrat(19)}")

#KIta buat dengan lambda

kuadrat = lambda angka: angka ** 2
print(f"Hasil fungsi kuadrat dengan lambda = {kuadrat(19)}") #dengan 1 variable

pangkat = lambda num,pow: num ** pow
print(f"Hasil fungsi pangkat dengan lambda = {pangkat(2,3)}") #dengan 2 vaeiabel

'''FUNGSI NYA APA?'''

#sort untuk list
data_list = ["Lufy", "Eka", "Fahrezi"]
data_list.sort()
print(f"Sorted list = {data_list}")

#sort pakai lambda
data_list = ["Lufy", "Eka", "Fahrezi"]
data_list.sort(key=lambda nama:len(nama))
print(f"Sorted list by lambda = {data_list}")

#filter
data_angka = [1,1,1,1,2,2,2,3,3,4,4,5,6,7,7,7,8,9,9]

def kurang_lima(angka):
    return angka < 5


data_angka_baru = list(filter(kurang_lima,data_angka))
data_angka_baru = list(filter(lambda x:x<5,data_angka))
print(data_angka_baru)

#Kasus Genap
data_genap = list(filter(lambda x:(x%2==0),data_angka))
print(data_genap)

#Kasus Ganjil
data_ganjil = list(filter(lambda x:(x%2==1),data_angka))
print(data_ganjil)

'''Anonymous Function'''
# currying <- Haskell Curry

def pangkat(angka, n):
    hasil = angka ** n
    return hasil

data_hasil = pangkat(9,9)
print(f"Fungsi biasa = {data_hasil}")

#DENGAN CURRYING

def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"pangkat2 = {pangkat2(5)}")
pangkat3 = pangkat(3)
print(f"pangkat3 = {pangkat3(3)}")
print(f"pangkat bebas = {pangkat(4)(5)}")