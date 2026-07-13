
#Kumpulan data int
data_angka = [1,2,3,4,5]
print(data_angka)

#Kumpulan data str
data_str = ["Lufy", "Asep", "Bagus"]
print(data_str)

#Kumpulan data bool
data_bool = [True, False, True]
print(data_bool)

#range
x = range(0,100)
data = list(x)
print(data)

#list dengan for loop, comprehensif
list_for = [j**3 for j in range(0,20)]
print(list_for)

#list dengan for dan if
list_if = [j**3 for j in range(0,20) if j%2 != 0]
print(list_if)

print("\n",20*"=","MANIPULASI LIST",20*"=","\n")

data_main = ["Lufy", "Asep", "Agus", "Sukirman", "Bokir"]
data_n = data_main[-1]
print("Data yg dicari ---> ",data_n)

len_data = len(data_main)
print("Panjang data ---> ", len_data)

#Manipulasi
data_main = ["Lufy", "Asep", "Agus", "Sukirman", "Bokir"]

#Tambahin data (posisi)
data_main.insert(1,"Raihan") #var.insert(posisi,item)
print(data_main)

#Tambahin data (akhir)
data_main.append("Nizam")
print(data_main)

#Merging list and list
list1 = ["Pisang", "Rambutan", "Apel"]
list2 = ["Anggur", "Melon", "Rambutan"]

list1.append(list2)
print(list1)

#Merubah data
#Mengganti data
list2 = ["Anggur", "Melon", "Rambutan"]
list2[2] = "Manki"
print(list2)

#Menghapus data
#Data pilihan
list2 = ["Anggur", "Melon", "Rambutan"]
list2.remove("Anggur")
print(list2)

#Data terbelakang
list2 = [1,2,3,4,5]
list2.pop()
print(list2)


