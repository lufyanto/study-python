
sisi = 10

#Menggunakan for
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

#Menggunakan while

count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

# Ganjil saja

count = 1
while True:

    if count %2:
        print("*"*count) #Print jika ganjil
        count +=1
    else:
        count += 1 #Abaikan +1 jika genap
        continue

    if count > sisi: #Jika kondisi terpenuhi end
        break


#Segitiga sama kaki
count = 1
spasi = int(sisi/2)
while True:

    if count %2:
        print(" "*spasi,"*"*count) #Print jika ganjil
        count +=1
        spasi -=1
    else:
        count += 1 #Abaikan +1 jika genap
        continue

    if count > sisi: #Jika kondisi terpenuhi end
        break

#Segitiga Terbalik

print ("===========================\n")

sisi = 10
for i in range(1, sisi, +1):
    print(" " * (sisi - i)+"*"*(2*i-1))
for i in range(sisi-1,0,-1):
    print(" " * (sisi-i) + "*" *(2*i-1))

    
