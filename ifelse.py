#If dan Else Statement

## IF
nama = input("Siapa nama anda : ")

if nama == "Lufyanto":
    print(f"Selamat datang '{nama}'")

print("===== Program Selesai =====")

## ELSE

print("\n",10*"="," E RAPORT UNIVERSITAS THINKPED ", 10*"=")
Nama = input("Nama \t\t: ")
Nim = input("NIM \t\t: ")
ipk = float(input("IPK \t\t: "))

if ipk >= 3:
    print("Selamat anda lulus")
else:
    print("NT")

## ELIF
print("\n",10*"="," E RAPORT UNIVERSITAS THINKPED ", 10*"=")
Nama = input("Nama \t\t: ")
Nim = input("NIM \t\t: ")
Nilai = int(input("Nilai \t\t: "))

if Nilai >= 80:
    Grade = "A"
elif Nilai >= 69:
    Grade = "B"
elif Nilai >= 50:
    Grade = "C"
elif Nilai >= 20:
    Grade = "D"
else:
    Grade = "E"

print("\n",10*"="," E RAPORT UNIVERSITAS THINKPED ", 10*"=")
print(f"Nama \t\t: {Nama}")
print(f"NIM \t\t: {Nim}")
print(f"Nilai anda adalah \t\t: {Nilai} \tGrade({Grade})")
