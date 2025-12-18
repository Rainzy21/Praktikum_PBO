from datetime import datetime
from models.console import Console

class Nintendo(Console):
    def __init__(self, id_console, nama, harga_sewa, warna):
        super().__init__(id_console, nama, "Nintendo", harga_sewa)
        self.__warna = warna
    
    def tampilkan_info(self):
        waktu = datetime.now().strftime("%d/%m/%Y %H:%M")
        print(f"[Nintendo] {self.get_nama()} - Warna: {self.__warna} | Rp{self.get_harga_sewa()}/hari | Status: {self.get_status()} | Dicatat: {waktu}") 