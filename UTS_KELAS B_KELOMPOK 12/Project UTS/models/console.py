class Console:
    def __init__(self, id_console, nama, tipe, harga_sewa):
        self.__id = id_console
        self.__nama = nama
        self.__tipe = tipe
        self.__harga_sewa = harga_sewa
        self.__status = "Tersedia"

    def get_id(self):
        return self.__id

    def get_nama(self):
        return self.__nama

    def get_tipe(self):
        return self.__tipe

    def get_harga_sewa(self):
        return self.__harga_sewa

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def tandai_disewa(self):
        if self.__status == "Tersedia":
            self.__status = "Disewa"
        else:
            print(f"{self.__nama} sudah disewa")

    def tandai_kembali(self):
        self.__status = "Tersedia"

    def tampilkan_info(self):
        print(
            f"[{self.__id}] {self.__nama} - {self.__tipe} | Rp. {self.__harga_sewa}/hari | Status: {self.__status}"
        )
