awalderet=int(input("masukan awal deret : "))
ahkirderet =int(input("masukan akhir deret :"))

for i in range (awalderet,ahkirderet):
    if i%3 !=0 and i%6 !=0 and i%2 != 0:
        print(i)