nama = input("Masukkan Nama :")
absen = input("No Absen :")

if absen == "10":
    mt  = [4*4, 4*4, 3*4, 3*4, 2*4, 2*4]

    ms = sum(mt)
    ipk = ms/18

    print("==== KHS UBSI ====")

    print(f"Nama Mahasiswa : {nama}")
    print(f"No Absen = {absen}")
    print(f"IPK Anda = ", {ipk})

else:
    print("MAAF NAMA ANDA TIDAK ADA DI DATABASE")





