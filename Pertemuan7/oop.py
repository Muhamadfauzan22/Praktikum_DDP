class Person:

    # property :=>variable
    nama = ""
    alamat = ""
    jurusan = ""

    # Method :=> function
    def tampilkan_data(self):
        print(f"Nama: {self.nama}")
        print(f"Alamat: {self.alamat}")
        print(f"Jurusan: {self.jurusan}")
    
person = Person()

# Assignment => isi nilai / value dalam property

person.nama = "Budi"
person.alamat = "Jakarta"
person.jurusan = "Teknik Informatika"


# panggil method / fungsi

person.tampilkan_data()

print()

Person2 = Person()

Person2.nama = "Joko"
Person2.alamat = "Depok"
Person2.jurusan = "Sistem Informasi"

Person2.tampilkan_data()
