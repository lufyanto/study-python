#komparasi menghasilkan booelan

# >,<,>=,<=,==,!=,is,is not

a = 10
b = 5

x = a > b
print(x)
x = a < b
print(x)
x = a >= b
print(x)
x = a <= b
print(x)
x = a == b 
print(x)
x = a != b
print(x)

#IS , IS NOT

x = 5
y = 100
print("nilai x =",x ,",id = ", hex(id(x)))
print("nilai x =",y ,",id = ", hex(id(y)))

hasil = x is not y
print(hasil)

#OPERATOR BITWISE
#Operasi masing" bit

a = 5
b = 9

c = a| b

print("======================OR=================")
print("nilai : ",a,"binary :",format(a,'08b'))
print("nilai : ",b,"binary :",format(b,'08b'))
print("-------------------------------------(OR)")
print("nilai : ",c,"binary :",format(c,'08b'))
print("-----------------------------------------")

a = 5
b = 9

c = a & b

print("======================AND=================")
print("nilai : ",a,"binary :",format(a,'08b'))
print("nilai : ",b,"binary :",format(b,'08b'))
print("-------------------------------------(AND)")
print("nilai : ",c,"binary :",format(c,'08b'))
print("-----------------------------------------")

a = 5
c = ~a
print("======================NOT=================")
print("nilai : ",a,"binary :",format(a,'08b'))
print("-------------------------------------(NOT)")
print("nilai : ",c,"binary :",format(c,'08b'))
print("-----------------------------------------")

#SHIFTING
c = 9
a = c >> 3
b = c << 2

print("======================>><<=================")
print("nilai : ",a,"binary :",format(a,'08b'))
print("-------------------------------------(>>)")
print("nilai : ",b,"binary :",format(b,'08b'))
print("--------------------------------------(<<)")

#ASSIGNMENT
print("+++++++++++++++++++++++ASSIGNMENT+++++++++++++++++++++")

a = 5 #assignment

a = a +1
a += 1 #sama aja a = a + 1
print("Nilai a :", a)

b = 7
b = b - 1
b -= 1 #sama aja b = b-1
print("Nilai b :", b)

c = 2
c = c*2
c *= 2 #sama aja c = c * 2
print("Nilai c :", c)

d = 10
d = d/10
d /= 10 #sama aja d = d/2
print("Nilai d :",d)

