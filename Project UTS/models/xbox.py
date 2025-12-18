from datetime import datetime
from models.console import Console

class Xbox(Console):
    def __init__(self, id_console, nama, harga_sewa, region):
        super().__init__(id_console, nama, "Xbox", harga_sewa)
        self.__region = region
    
    def tampilkan_info(self):
        waktu = datetime.now().strftime("%d/%m/%Y %H:%M")
        print(f"[Xbox] {self.get_nama()} (Region {self.__region}) - Rp{self.get_harga_sewa()}/hari | Status: {self.get_status()} | Dicatat: {waktu}")