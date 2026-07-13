import datetime


mahasiswa_1 = {
    'nama' : 'Lufyanto eka fahrezi',
    'nim' : '123456789',
    'sks_ok' : 140,
    'beasiswa' : True,
    'lahir' : datetime.datetime(2007,12,18)
}

mahasiswa_2 = {
    'nama' : 'Nizam Hasbi',
    'nim' : '123456788',
    'sks_ok' : 140,
    'beasiswa' : False,
    'lahir' : datetime.datetime(2008,1,2)
}

mahasiswa_3 = {
    'nama' : 'Raihan FS',
    'nim' : '123456777',
    'sks_ok' : 140,
    'beasiswa' : True,
    'lahir' : datetime.datetime(2008,10,2)
}

data_mahasiswa = {
    'MAH1' : mahasiswa_1,
    'MAH2' : mahasiswa_2,
    'MAH3' : mahasiswa_3
}

print("-"*60)

print(f'{"KEY":<5} {"NAMA":<20} {"SKS":<7} {"BEASISWA":<9} {"TGL LAHIR":>10}')
for mahasigma in data_mahasiswa:
    KEY = mahasigma

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_ok']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    TTL = data_mahasiswa[KEY]['lahir'].strftime("%x")
    print(f'{KEY:<5} {NAMA:<20} {SKS:<7} {BEASISWA:^9} {TTL:>10}')

