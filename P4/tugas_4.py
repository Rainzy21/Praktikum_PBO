# Parent Class
class Kendaraan:
    def __init__(self, merk, tahun_produksi, warna):
        self.__merk = merk
        self.__tahun_produksi = tahun_produksi
        self.__warna = warna

    def tampilkan_info(self):
        print(f"Merk: {self.__merk}")
        print(f"Tahun Produksi: {self.__tahun_produksi}")
        print(f"Warna: {self.__warna}")

    def nyalakan_mesin(self):
        print("Mesin kendaraan menyala.")


# Child Class Mobil
class Mobil(Kendaraan):
    def __init__(self, merk, tahun_produksi, warna, jumlah_pintu):
        super().__init__(merk, tahun_produksi, warna)
        self.__jumlah_pintu = jumlah_pintu

    def tampilkan_info(self):  # override
        super().tampilkan_info()
        print(f"Jumlah Pintu: {self.__jumlah_pintu}")

    def buka_pintu_bagasi(self):
        print("Pintu bagasi mobil dibuka.")


# Child Class Motor
class Motor(Kendaraan):
    def __init__(self, merk, tahun_produksi, warna, kapasitas_tangki):
        super().__init__(merk, tahun_produksi, warna)
        self.__kapasitas_tangki = kapasitas_tangki

    def nyalakan_mesin(self):  # override
        print("Brmm... Mesin motor dinyalakan dengan kick starter!")

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Kapasitas Tangki: {self.__kapasitas_tangki} liter")


# Bagian utama program
if __name__ == "__main__":
    # Membuat objek Mobil
    mobil1 = Mobil("Mazda RX-7", 2002, "Hitam", 4)
    print("=== Info Mobil ===")
    mobil1.tampilkan_info()
    mobil1.nyalakan_mesin()
    mobil1.buka_pintu_bagasi()

    print("\n=== Info Motor ===")
    # Membuat objek Motor
    motor1 = Motor("Honda Beat", 2022, "Merah", 4)
    motor1.tampilkan_info()
    motor1.nyalakan_mesin()
