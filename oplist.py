data = [1,1,2,2,3,3,3,3,4,5,5,5,6,6,6,7,7,8,8,9,9,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3]

#count data

print(f"Data 2 berjumlah = {data.count(2)}")
print(f"Data 5 berjumlah = {data.count(5)}")
print(f"Data 3 berjumlah = {data.count(3)}")

#ambil posisi data (Nyari posisi)
data = ["Ahmad", "Asep", "Agus", "Lufy"]
#Array = [0,1,2,3,dst.....]

nyari = data.index("Asep")
print("Posisi data yang dicari ---> ",nyari)

#sorting data
data_1 = [1,1,2,2,3,3,3,3,4,5,5,5,6,6,6,7,7,8,8,9,9,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3]
data_1.sort()
print(data_1)

#Reverse data
data_1.reverse()
print(data_1)

print("\n",30*"=","COPY LIST",20*"=","\n")

a = [1,2,3,4,5]

b = a #Masih berkesinambungan soalnya posisi HEX ID nya sama

a[1] = 2
b.reverse()

print(a)
print(b)

print("\n===== HEX ID 2 VARIABEL =====\n")
print(hex(id(a)))
print(hex(id(b)))
print("\n")
x = [1,2,3,4,5,6,7,8,9]
c = x.copy() #Berbeda karena hex id berbeda dan pemanggilan pun berbeda

print(x)
print(c)

print("\n===== HEX ID 2 VARIABEL =====\n")
print(hex(id(x)))
print(hex(id(c)))
