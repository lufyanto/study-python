#macam-macam data dalam pemrograman

#angka
a = 10 #integer/int
print(f"Variabel {a}", "Bertipe ", type(a))

b = 77.7 #float
print(f"Variabel {b}", "Bertipe ", type(b))

#Karakter
string = "Lufyanto"
print(f"Variabel {string}", "Bertipe ", type(string))

#Booelan (True/False)
status = True
print(f"Variabel {status}", "Bertipe ", type(status))

#Tipe data khusus COMPLEX

c = complex(7,8)
print(f"Variabel {c}", "Bertipe ", type(c))

#tipe data bahasa C

from ctypes import c_double, c_bool, c_int

cd = c_double(10.9)
print(f"Variabel {cd}", "Bertipe ", type(cd))

ci = c_int(11)
print(f"Variabel {ci}", "Bertipe ", type(ci))

#CASTING TIPE DATA
#CASTING = MERUBAH TIPE DATA

print("========== CASTING TIPE DATA =======")

a = 0
print(f"Variabel {a}", "Bertipe ", type(a))

b = float(a)
print(f"Variabel {b}", "Bertipe ", type(b))

c = bool(a) #True = 1/-1/"aaaa" False = 0/""
print(f"Variabel {c}", "Bertipe ", type(c))

d = str(a) #dia tidak bisa dioperasi (+,-,*,/,%,**,//)
print(f"Variabel {d}", "Bertipe ", type(d))

aa = False
ab = str(aa)
ac = int(aa)

print(f"Variabel {ab}", "Bertipe ", type(ab))
print(f"Variabel {ac}", "Bertipe ", type(ac))

