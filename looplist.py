# Looping dari list

#for loop
print("\n===== FOR LOOP =====\n")
data = [1,3,2,4,5,6,8,9,7]

for angka in data:
    print(f"Angka ---> {angka}")

#for loop range
print("\n===== LOOP RANGE =====\n")
data_a = [10,11,9,8,6,7]

panjang = len(data_a)

for x in range(panjang):
    print(f"Angka ke -> {x}")

#while
print("\n===== WHILE =====\n")
data = [1,3,2,4,5,6,8,9,7]

panjang = len(data)
x = 0

while x < panjang:
    print(x)
    x += 1

#enumerate
print("\n===== ENUMERATE =====\n")
data = [1,2,3,4,5]

for index,data in enumerate(data):
    print(f"Index = {index} Data = {data**2}")

