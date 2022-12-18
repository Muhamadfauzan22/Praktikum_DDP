def hello():
    print("Hello,World")

hello()

# Function dengan parameter

def sayHello(name):
    print(f"Hello, nama saya {name}")

sayHello("Budi")
sayHello("Joko")

def tambah(bilanganPertama, bilanganKedua):
    total = bilanganPertama + bilanganKedua
    print(total)

tambah(10, 5)

# Buat fungsi yang bisa membuat perkalian dan pembagian

def perkalian(bilanganPertama, bilanganKedua):
    total = bilanganPertama * bilanganKedua
    print(total)


def pembagian(bilanganPertama, bilanganKedua):
    total = bilanganPertama / bilanganKedua
    print(total)


perkalian(10,5)
pembagian(10,5)