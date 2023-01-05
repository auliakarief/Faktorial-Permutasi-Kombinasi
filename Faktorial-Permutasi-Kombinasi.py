import math

a = int(input("masukkan bilangan a : "))
b = int(input("masukkan bilangan b : "))

print(a,"! = ",math.factorial(a)," dan ",b,"! ",math.factorial(b),sep="")

permutasi = math.factorial(a)//math.factorial(a-b)
print("Permutasi (",a,",",b,") = ",permutasi,sep="")

kombinasi = math.factorial(a)//(math.factorial(b)*math.factorial(a-b))
print("Kombinasi (",a,",",b,") = ",kombinasi,sep="")

