class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.status_pinjam = False

    def tampilkan_info(self):
        status = "Dipinjam" if self.status_pinjam else "Tersedia"
        print(f"Judul       : {self.judul}")
        print(f"Penulis     : {self.judul}")
        print(f"Tahun Terbit: {self.tahun_terbit}")
        print(f"Status      : {status}")
        print("_" * 40)

    def pinjam_buku(self):
        if not self.status_pinjam:
            self.status_pinjam = True
            print(f"Buku '{self.judul}' telah dipinjam.")
        else:
            print(f"Buku '{self.judul}' sudah dalam status pinjam.")
        
    def kembalikan_buku(self):
        if self.status_pinjam:
            self.status_pinjam = False
            print(f"Buku '{self.judul}' telah dikembalikan.")
        else:
            print(f"Buku '{self.judul}' memang sudah tersedia.")

if __name__ == "__main__":
    buku1 = Buku("Laut Bercerita", "Leila S. Chudori", 2017)
    buku2 = Buku("Madilog", "Tan Malaka", 1943)

    print("Informasi Awal Buku:")
    buku1.tampilkan_info()
    buku2.tampilkan_info()

    print("Simulasi Peminjaman:")
    buku1.pinjam_buku()
    buku1.tampilkan_info()

    print("Simulasi Pengembalian:")
    buku1.kembalikan_buku()
    buku1.tampilkan_info()