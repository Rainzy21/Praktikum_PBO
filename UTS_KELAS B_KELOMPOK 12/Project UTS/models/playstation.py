from datetime import datetime
from models.console import Console


class Playstation(Console):
    def __init__(self, id_console, nama, harga_sewa, versi):
        super().__init__(id_console, nama, "PlayStation", harga_sewa)
        self.__versi = versi

    def tampilkan_info(self):
        waktu = datetime.now().strftime("%d/%m/%Y %H:%M")
        print(
            f"[PS] {self.get_nama()} (Versi {self.__versi}) - Rp{self.get_harga_sewa()}/hari | Status: {self.get_status()} | Dicatat: {waktu}"
        )
