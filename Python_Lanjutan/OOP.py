print("========== OOP ==========")

class kucing:
    # --- CONSTRUCTOR ---
    def __init__(self, nama: str, warna: str):
        # --- self ---
        self.nama = nama
        self.warna = warna


    # --- METHOD ---
    def bersuara(self):
        print(f"{self.nama} bersuara : Meooowwww ~~")

    def makan(self, makanan: str):
        print(f"{self.nama} yang berbulu {self.warna} sedang makan {makanan}")


kucing1 = kucing("Oyen", "Oranye")
kucing2 = kucing("Garong","Hitam")
kucing3 = kucing("Cucu", "Putih")

kucing1.bersuara()
kucing2.bersuara()

kucing2.makan("Tulang Ikan")
kucing3.makan("Tulang Ayam")

class kampus:
    def __init__(self, mahasiswa: str, semester: int, prodi: str, IPK: float):
        self.mahasiswa = mahasiswa
        self.semester = semester
        self.prodi = prodi
        self.IPK = IPK

    def sapaMahasiswa(self):
            print(f"\n\nHAIII..... Perkenalkan nama saya {self.mahasiswa}, dari prodi {self.prodi}")

    def ipk(self):
         print(f"\n===== KARTU HASIL STUDI =====\n")
         print(f"\nNama\t\t= {self.mahasiswa}")
         print(f"\nSEMESTER\t= {self.semester}")
         print(f"\nIPK\t\t= {self.IPK}")

kampus1 = kampus("Lufyanto", 1, "Teknologi Informasi", 4.00)


kampus1.sapaMahasiswa()
kampus1.ipk()


print("="*20)
print("\nAPLIKASI BANK DIGITAL\t\t\n")
print("="*20)

class akunBank:
    def __init__(self, pengguna: str, saldoAwal: float):
        self.user = pengguna
        self.__saldo = saldoAwal


    def setor(self, jumlah: float):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Setor senilai Rp.{jumlah:,.0f} berhasil")
        else:
            print(f"Jumlah setor harus lebih dari 0")


    def lihat_saldo(self):
        return self.__saldo


akun1 = akunBank("Lufyanto", 100000)

akun1.setor(200000)
print("Saldo: ", akun1.lihat_saldo())


