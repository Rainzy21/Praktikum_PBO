class Karyawan:
    def __init__(self, nama, id_karyawan, gaji,):
        self.__nama = nama
        self.__id_karyawan = id_karyawan
        self.__gaji = gaji
        self.set_nama(nama)
        self.set_gaji(gaji)

    def get_info(self):
        return f"ID Karyawan: {self.__id_karyawan}, Nama: {self.__nama}, Gaji: {self.__gaji}"

    def get_id(self):
        return self.__id_karyawan

    def get_nama(self):
        return self.__nama

    def get_gaji(self):
        return self.__gaji

    def set_nama(self, nama_baru):
        if len(nama_baru) > 0:
            self.__nama = nama_baru
        else:
            print("Tidak boleh kosong atau Minimal 1 karakter")

    def set_gaji(self, gaji_baru):
        if gaji_baru > 0:
            self.__gaji = gaji_baru
        else:
            print("Gaji tidak boleh negatif atau Kurang dari 0")

k1 = Karyawan("Yanto", "K001", 5000000)

print("Data Awal:", k1.get_info())

print("\nCoba ubah gaji ke -5000000")
k1.set_gaji(-5000000)
print("Setelah dicoba:", k1.get_info())

print("\nCoba ubah nama jadi kosong")
k1.set_nama("")
print("Setelah dicoba:", k1.get_info())

print("\nUbah gaji ke 6000000")
k1.set_gaji(6000000)

print("\nData Terbaru:", k1.get_info())
