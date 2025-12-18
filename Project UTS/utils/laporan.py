import os
from datetime import datetime

class Laporan:
    def __init__(self, nama_file="laporan.txt"):
        self.nama_file = nama_file
        self.log_data = []

    def catat(self, pesan):
        waktu = datetime.now().strftime("%d/%m/%Y %H:%M")
        log = f"[{waktu}] {pesan}"
        self.log_data.append(log)
        print(log)

    def simpan(self):
        folder = "output"
        if not os.path.exists(folder):
            os.mkdir(folder)

        path_file = os.path.join(folder, self.nama_file)
        with open(path_file, "w", encoding="utf-8") as file:
            file.write("=== LAPORAN AKTIVITAS RENTAL KONSOLE ===\n\n")
            for log in self.log_data:
                file.write(log + "\n")

        print(f"Laporan tersimpan di: {path_file}")
