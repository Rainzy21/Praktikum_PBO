#menyiapkan struktur Inheritance

#PARENT CLASS
class Bentuk:
    def gambar(self):
        #Method sengaja dibuat umum dan akan di override
        raise NotImplementedError("Subclass harus mengimplementasikan methode ini!")
    
#CHILD CLASS 1
class Persegi(Bentuk):
    def gambar(self):
        print("Menggambar Persegi: [][][]")

#CHILD CLASS 2
class Lingkaran(Bentuk):
    def gambar(self):
        print("menggambar Lingkaran: OOOOOO")

#CHILD CLASS 3
class Segitiga(Bentuk):
    def gambar(self):
        print("Mengambar Segitiga: /\\")

#CLASS YANG TIDAK BERHUBUNGAN (untuk duck typing)
class Teks:
    def gambar(self):
        print("Menulis Teks: 'Hello, Polymorphism!'")

#Sebuah fungsi yang menunjukkan perilaku polimorfik
def render_objek(objek_untuk_digambar):
    print("Mencoba me-render objek...")
    objek_untuk_digambar.gambar()

#bagian utama program
persegi = Persegi()
lingkaran = Lingkaran()
segitiga = Segitiga()
teks_biasa = Teks() #objek ini Bukan dari turunan bentuk

print("\n--- Menggunakan fungsi polimorfik ---")
render_objek(persegi)
render_objek(lingkaran)
render_objek(segitiga)

print("\n--- Demonstrasi Duck Typing ---")
render_objek(teks_biasa) #fungsi tetap bekerja