import datetime
import os
import string
import random

mahasiswa_template = {
    'nama' : 'nama',
    'nim' : '00000000',
    'sks' : 0,
    'ttl' : datetime.datetime(1111,11,11)
}

data_mahasiswa = {}

while True:
    os.system("cls")

    print(f'{'SELAMAT DATANG DI UNIVERSITAS PANCAROBA' :^60}')
    print(f'{'MADE BY TI ON UNIVERSITAS PANCAROBA' :^60}')
    print("-"*60)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())

    mahasiswa['nama'] = input("Masukkan Nama Anda : ")
    mahasiswa['nim'] = input("Masukkan NIM Anda : ")
    mahasiswa['sks'] = int(input("Masukkan SKS Anda : "))
    TAHUN_LAHIR = int(input('Tahun Lahir YYYY :'))
    BULAN_LAHIR = int(input('Bulan  Lahir MM :'))
    TANGGAL_LAHIR = int(input('Tanggal Lahir DD :'))
    mahasiswa['ttl'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)


    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range (10)))
    data_mahasiswa.update({KEY:mahasiswa})

    print("-"*60)

    print(f'{"KEY":<20} {"NAMA":<30} {"SKS":<10} {"TGL LAHIR":>20}')

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks']
        LAHIR = data_mahasiswa[KEY]['ttl'].strftime('%x')

        print(f'{KEY:<20} {NAMA:<30} {SKS:<10} {LAHIR:>20}')

    is_not = input("Apakah sudah selesay (Y Lanjut / N Selesai :)")
    if is_not == "N":
        break