import datetime as dt

print("Isilah tanggal, bulan, tahun.")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Tanggal \t\t: "))
tahun = int(input("Tanggal \t\t: "))

ttl = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda adalah : {ttl}")
print(f"Hari kelahiran anda adalah : {ttl:%A}")

hari_ini = dt.date.today()
print(f"Hari ini Tanggal : {hari_ini}")
umur_hari = hari_ini - ttl
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365 ) / 30
print(f"Hari nya adalah : {umur_hari}")
print(f"Umur anda adalah : {umur_tahun} tahun, {umur_bulan_sisa} bulan")
