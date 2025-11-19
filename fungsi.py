#nomor 4:fungsi untuk menampilkan bilangan ganjil yang kurang argumens
def bilangan(angka):
    for i in range (1,angka):
        if i % 2 != 0:
            print(i, end=", ")

bilangan(20)


print()
#nomor 3: keterangan 
def nilai(n=0):
    if n <= 60:
        print("tidak lulus")
    elif n > 60 and n <= 100:
        print("lulus")
    else:
        print("tidak diketahui")

nilai(80)



print()
#nomor 2:fungsi bernama is_genap:bilangan bulat

def is_genap(n):
    return n % 2 == 0

print(is_genap(2))



#nomor 1:fungsi celcius_ke_fahreinheit
print()
def celcius_ke_fahrenheit(celcius):
    return (celcius*9/5)+32

print(celcius_ke_fahrenheit(0))   #output:32.0
print(celcius_ke_fahrenheit(100)) #output:212.0












