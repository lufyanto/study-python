data_1 = [1,2,3]
data_2 = [4,5,6]

data_2d = [data_1,data_2,7,8,9]

print(data_2d)

#Implementasi 
peserta_a = ["Ucup",18,"LK-LK"]
peserta_b = ["Denis", 19, "LK-LK"]
peserta_c = ["Putri", 18, "PR"]

list_peserta = [peserta_a,peserta_b,peserta_c]
print(list_peserta)

for peserta in list_peserta:
    print("=====PESERTA=====")
    print(f"Nama \t\t: {peserta[0]} \n")
    print(f"Umur \t\t: {peserta[1]} \n")
    print(f"JK \t\t: {peserta[2]} \n")

#Dengan reverensi

list_copy = list_peserta.copy()
print(list_copy)
peserta_a[0] = "Asep"
print(list_peserta)
print(list_copy)

print("\n========== NESTED LIST COPY ==========\n")

peserta_a = ["Ucup",18,"LK-LK"]
peserta_b = ["Denis", 19, "LK-LK"]
peserta_c = ["Putri", 18, "PR"]
list_peserta = [peserta_a,peserta_b,peserta_c]
list_copy = list_peserta.copy()

print(list_peserta)
print(list_copy)

print(hex(id(list_peserta)))
print(hex(id(list_copy)))

print("addres dari member")
print(hex(id(list_peserta[0])))
print(hex(id(list_copy[0])))

from copy import deepcopy
data_a = [1,2,3,4,5,6]
data_b = [7,8,9,10,11,12]

data_c = [data_a, data_b]

data_copy = deepcopy(data_c)

print("Data Gabungan = ", data_c)
print("ID = ", hex(id(data_c)))
print("Data Gabungan = ", data_copy)
print("ID = ", hex(id(data_copy)))

#COPY ---> list biasa
# import DEEPCOPY ---> list nested
