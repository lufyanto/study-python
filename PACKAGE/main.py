import sains.matematika
from sains import fisika
from sains.fisika import gaya as joule
import time
import os

os.system('cls')

t_awal = time.time()
hasil = sains.matematika.tambah(1,2,3,4,5)
print(hasil)

hasil2 = sains.matematika.kali(10,20,30,40,50)
print(hasil2)
t_akhhir = time.time()

hasil3 = fisika.gaya(90,10)
print(hasil3)

gaya = joule(100,100)
print(gaya)

print("Kecepatan output ===> ",t_akhhir-t_awal)