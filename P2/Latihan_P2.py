class Mahasiswa:
    def __init__(self, input_nama, input_nim, input_prodi):
        self.nama = input_nama
        self.nim = input_nim
        self.prodi = input_prodi
        print(f"Objek Mahasiswa dengan nama {self.nama} telah dibuat!")

    def sapa(self):
        print(f"Halo! Nama saya {self.nama}. Senang berkenalan!")

    def tampilkan_info(self):
        print("--- Informasi Mahasiswa ---")
        print(f"Nama    : {self.nama}")
        print(f"NIM     : {self.nim}")
        print(f"Prodi   : {self.prodi}")
        print("---------------------------")
        
otong = Mahasiswa("Otong Surotong", 12345, "Teknik Informatika")
ucup = Mahasiswa("Ucup Surucup", 67890, "Teknik Komputer")

print("\n--- Interaksi dengan objek ---")
otong.sapa()
ucup.sapa()

print("\n--- Data Mahasiswa ---")
print(f"Data Mahasiswa 1: {otong.nama} - {otong.nim}- {otong.prodi}")
print(f"Data Mahasiswa 2: {ucup.nama} - {ucup.nim} - {ucup.prodi}")