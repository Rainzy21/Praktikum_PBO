import os
from datetime import datetime

class FileAnalyzer:
    def __init__(self, file_path):
        self.__file_path = file_path
        if os.path.exists(file_path): # mengecek apakah file ada.
            self.__file_ada = True
            self.__file_size = os.path.getsize(file_path) # mengambil ukuran file (byte).
        else:
            print(f"Error: File '{file_path}' tidak ditemukan.")
            self.__file_ada = False

    def get_file_size(self, unit="bytes"):
        if not self.__file_ada:
            return None
        if unit.lower() == "kb":
            return round(self.__file_size / 1024, 2)
        return self.__file_size

    def get_modification_time(self):
        if not self.__file_ada:
            return None
        timestamp = os.path.getmtime(self.__file_path) #mengambil waktu modifikasi terakhir.
        return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S") #mengubah waktu menjadi format terbaca.

    def analyze(self):
        if not self.__file_ada:
            print(f"File '{self.__file_path}' tidak dapat dianalisis karena tidak ditemukan.")
            return

        print("=== Laporan Analisis File ===")
        print(f"Nama File: {self.__file_path}")
        print(f"Ukuran: {self.get_file_size('KB')} KB")
        print(f"Waktu Modifikasi Terakhir: {self.get_modification_time()}")
        print("=============================")


# Bagian utama program
if __name__ == "__main__":
    file1 = FileAnalyzer("dokument.txt")
    file1.analyze() #mencetak hasil analisis dalam format rapi.

    print()  # spasi antar output

    file2 = FileAnalyzer("file_Hilang.txt")
    file2.analyze()
