from models.playstation import Playstation
from models.xbox import Xbox
from models.nintendo import Nintendo
from models.pelanggan import Pelanggan
from utils.laporan import Laporan

if __name__ == "__main__":
    # Inisialisasi laporan
    laporan = Laporan()

    # Membuat objek konsol
    ps5 = Playstation("C001", "PlayStation 5", 70000, "Digital Edition")
    xbox = Xbox("C002", "Xbox Series X", 65000, "Asia")
    switch = Nintendo("C003", "Nintendo Switch OLED", 50000, "Putih")

    # Membuat pelanggan
    andi = Pelanggan("P001", "Andi", "08123456789")
    budi = Pelanggan("P002", "Budi", "08129876543")

    print("=== DAFTAR KONSOLE ===")
    for k in [ps5, xbox, switch]:
        k.tampilkan_info()

    print("\n=== SIMULASI TRANSAKSI ===")
    andi.sewa_console(ps5, laporan)
    budi.sewa_console(ps5, laporan)
    andi.kembalikan_console(laporan)
    budi.sewa_console(ps5, laporan)
    budi.kembalikan_console(laporan)

    laporan.simpan()