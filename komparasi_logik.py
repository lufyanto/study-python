#---0+++5---8+++11---

angka = int(input("Masukkan angka yang\nlebih besar dari 0\natau\nkurang besar dari 5\n"))

print("=" * 20)
lb = angka > 0
print(lb)
lk = angka < 5
print(lk)

log = lb or lk
print(log)

print("")
print("_"*20)
print("")

angka = int(input("Masukkan angka yang\nlebih besar dari 8\natau\nkurang besar dari 11\n"))

print("=" * 20)
lb = angka > 8
print(lb)
lk = angka < 11
print(lk)

log = lb and lk
print(log)
