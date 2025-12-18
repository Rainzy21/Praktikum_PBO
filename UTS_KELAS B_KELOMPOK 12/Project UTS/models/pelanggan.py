from datetime import datetime

class Pelanggan:
    def __init__(self, id_pelanggan, nama, no_hp):
        self.__id = id_pelanggan
        self.__nama = nama
        self.__no_hp = no_hp
        self.__console_dipinjam = None
        self.__waktu_sewa = None

    def get_nama(self):
        return self.__nama

    def sewa_console(self, console, laporan):
        if console.get_status() == "Tersedia":
            console.tandai_disewa()
            self.__console_dipinjam = console
            self.__waktu_sewa = datetime.now()
            laporan.catat(f"{self.__nama} menyewa {console.get_nama()} pada {self.__waktu_sewa.strftime('%d/%m/%Y %H:%M')}")
        else:
            laporan.catat(f"{self.__nama} gagal menyewa {console.get_nama()} karena sedang disewa.")

    def kembalikan_console(self, laporan):
        if self.__console_dipinjam:
            console = self.__console_dipinjam
            console.tandai_kembali()
            waktu_kembali = datetime.now()
            durasi = waktu_kembali - self.__waktu_sewa
            lama_jam = int(durasi.total_seconds() // 3600)
            laporan.catat(f"{self.__nama} mengembalikan {console.get_nama()} setelah {lama_jam} jam.")
            self.__console_dipinjam = None
            self.__waktu_sewa = None
        else:
            laporan.catat(f"{self.__nama} tidak sedang menyewa console.")
