from Animals import Animals


animal = Animals(["guguk", "meong", "singa"])


animal.index()

# Menampilkan animals dengan index: urutan

print("Menampilkan animals dengan index")
animal.show(2)
print()

# Menampilkan data animals
print("Menambahkan data animals")
animal.store("unta")
print()

# Menampilkan data animals
print("Menambahkan data animals")
animal.update(1, "gorila")
print()

# Menampilkan data animals
print("Menambahkan data animals")
animal.delete(0)
print()